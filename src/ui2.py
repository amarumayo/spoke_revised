import tkinter as tk
from tkinter import ttk
from components import Hub, Wheel
from validators import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.hub = Hub()
        self.wheel = Wheel(self.hub)
                
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
            self.form, label="Left Flange Offset:", key="lfo",
            validators=[is_required, is_numeric, is_positive]
        )
        self.field_lfo.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        self.field_rfo = InputField(
            self.form, label="Right Flange Offset:", key="rfo",
            validators=[is_required, is_numeric, is_positive]
        )    
        self.field_rfo.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

        self.field_old = InputField(self.form, "lock nut to lock nut:")
        self.field_old.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

        self.field_dl = InputField(self.form, "L. Spoke Circle Diameter:")
        self.field_dl.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

        self.field_rl = InputField(self.form, "R. Spoke Circle Diameter:")
        self.field_rl.grid(row=5, column=0, sticky="ew", padx=5, pady=5)

        self.field_shd = InputField(self.form, "Spoke Hole Diameter:")
        self.field_shd.grid(row=6, column=0, sticky="ew", padx=5, pady=5)

        # RIM COLUMN (col 1)
        self.field_erd = InputField(self.form, "Effective Rim Diameter:")
        self.field_erd.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.field_num_spokes = InputField(self.form, "Number of Spokes:")
        self.field_num_spokes.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        self.field_crosses = InputField(self.form, "Number of Crosses:")
        self.field_crosses.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

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
            ("Right Flange Offset", self.field_rfo)
        ]

        errors = []
        for name, field in fields:
            if not field.is_valid():
                field.mark_invalid()
                errors.append(f"{name} must be a positive number.")
            else:
                field.mark_valid()
                # populate hub field (should be wheel)
                setattr(self.hub, field.key, float(field.get()))                

        if errors:
            self.results.insert("end", "Validation failed:\n" + "\n".join(errors) + "\n", "error")
            return

        self.results.insert("end", "success", "error")


class InputField(ttk.Frame):
    def __init__(self, parent, label, key=None, validators=None, **kwargs):
        super().__init__(parent)

        self.label = ttk.Label(self, text=label, width=20)
        self.label.grid(row=0, column=0, sticky="w")
        self.entry = ttk.Entry(self, **kwargs)
        self.entry.grid(row=0, column=1, sticky="ew")

        self.key = key  # maps to Hub or Spoke


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