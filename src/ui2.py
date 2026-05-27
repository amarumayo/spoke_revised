import tkinter as tk
from tkinter import ttk
from components import Hub, Rim, Wheel
from validators import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.hub = Hub()
        self.rim = Rim()
        self.wheel = Wheel(hub=self.hub, rim=self.rim)
                
        self.title("Spoke Calculator")
        self.geometry("500x600")

        # Main form frame
        self.form = ttk.Frame(self)
        self.form.pack(fill="x", padx=20, pady=20)

        # Configure 2 equal columns
        for col in range(2):
            self.form.columnconfigure(col, weight=1)        

        # Column headers
        ttk.Label(self.form, text="Hub", anchor="center").grid(
            row=0, column=0, sticky="ew", pady=(0, 10)
        )
        ttk.Label(self.form, text="Rim", anchor="center").grid(
            row=0, column=1, sticky="ew", pady=(0, 10)
        )
        
        # HUB COLUMN (col 0)
        self.field_lfo = InputField(
            self.form, label="Left Flange Offset:", key="lfo", target="hub",
            validators=[is_required, is_numeric, is_positive]
        )
        self.field_lfo.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        self.field_rfo = InputField(
            self.form, label="Right Flange Offset:", key="rfo", target="hub",
            validators=[is_required, is_numeric, is_positive]
        )    
        self.field_rfo.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

        self.field_old = InputField(
            self.form, label="Lock Nut to Lock Nut:", key="old", target="hub",
            validators=[is_required, is_numeric, is_positive]
        )
        self.field_old.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

        self.field_dl = InputField(
            self.form, label="L. Spoke Circle Diameter:", key="dl", target="hub",
            validators=[is_required, is_numeric, is_positive]

        )
        self.field_dl.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

        self.field_dr = InputField(
            self.form, label="R. Spoke Circle Diameter:", key="dr", target="hub",
            validators=[is_required, is_numeric, is_positive]

        )
        self.field_dr.grid(row=5, column=0, sticky="ew", padx=5, pady=5)

        self.field_shd = InputField(
            self.form, label="Spoke Hole Diameter:", key="shd", target="hub",
            validators=[is_required, is_numeric, is_positive]

        )
        self.field_shd.grid(row=6, column=0, sticky="ew", padx=5, pady=5)

        # RIM COLUMN (col 1)
        self.field_erd = InputField(
            self.form, label="Effective Rim Diameter:", key="erd", target="rim",
            validators=[is_required, is_numeric, is_positive]
        )
        self.field_erd.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.field_num_spokes = InputField(
            self.form, label="Number of Spokes:", key="num_spokes", target="rim",
            validators=[is_required, is_numeric, is_positive]
        )
        self.field_num_spokes.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        self.field_num_crosses = InputField(
            self.form, label="Number of Crosses:", key="num_crosses", target="rim",
            validators=[is_required, is_numeric, is_positive]
        )
        self.field_num_crosses.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        # Submit button
        self.submit_btn = ttk.Button(self, text="Submit", command=self.on_submit)
        self.submit_btn.pack(pady=10)

        # Results box
        self.results = tk.Text(self, height=10)
        self.results.tag_config("error", foreground="red") # red text for errors
        self.results.pack(fill="both", expand=True, padx=20, pady=10)

    def on_submit(self):
        self.results.delete("1.0", "end")

        fields = [
            ("Left Flange Offset", self.field_lfo),
            ("Right Flange Offset", self.field_rfo),
            ("Lock Nut to Lock Nut", self.field_old),
            ("L. Spoke Circle Diameter", self.field_dl),
            ("R. Spoke Circle Diameter", self.field_dr),
            ("Spoke Hole Diameter", self.field_shd),
            ("Effective Rim diameter", self.field_erd),
            ("Number of Spokes", self.field_num_spokes),
            ("Number of Crosses", self.field_num_crosses)
        ]

        errors = []
        for name, field in fields:
            if not field.is_valid():
                field.mark_invalid()
                errors.append(f"{name} must be a positive number.")
            else:
                field.mark_valid()
                
                # populate hub or rim field 
                target_obj = getattr(self, field.target)
                setattr(target_obj, field.key, float(field.get()))                

        if errors:
            self.results.insert("end", "Validation failed:\n" + "\n".join(errors) + "\n", "error")
            return

        self.results.insert("end", "success", "error")
        self.rim

        self.wheel


class InputField(ttk.Frame):
    def __init__(self, parent, label, key=None, target=None, validators=None, **kwargs):
        super().__init__(parent)

        self.label = ttk.Label(self, text=label, width=20)
        self.label.grid(row=0, column=0, sticky="w")
        self.entry = ttk.Entry(self, **kwargs)
        self.entry.grid(row=0, column=1, sticky="ew")

        # maps to Hub or Spoke
        self.key = key  
        self.target = target


        # for validation X
        self.icon = ttk.Label(self, text="", foreground="red")
        self.icon.grid(row=0, column=2, padx=5)

        self.columnconfigure(1, weight=1)
        self.validators = validators or []

    def is_valid(self) -> bool:
        value = self.get()
        for func in self.validators:
            if not func(value):
                return False
        return True
        
    def get(self) -> str:
        return self.entry.get()

    def mark_invalid(self):
        self.icon.config(text="❌")

    def mark_valid(self):
        self.icon.config(text="✔️", foreground="green")