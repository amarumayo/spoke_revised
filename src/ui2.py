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
        self.geometry("585x500")

        # Main form frame
        self.form = ttk.Frame(self)
        self.form.pack(fill="x", padx=20, pady=20)

        # Configure 2 equal columns
        for col in range(2):
            self.form.columnconfigure(col, weight=1, uniform="formcols")        

        # Column headers
        ttk.Label(self.form, text="Hub Specs", anchor="center").grid(
            row=0, column=0, sticky="ew", pady=(0, 10)
        )
        ttk.Label(self.form, text="Rim Specs", anchor="center").grid(
            row=0, column=1, sticky="ew", pady=(0, 10)
        )
        
        # HUB COLUMN (col 0)
        self.field_lfo = InputField(
            self.form, label="Left Flange Offset:", key="lfo", target="hub",
            validators=[is_required, is_positive]
        )
        self.field_lfo.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        self.field_rfo = InputField(
            self.form, label="Right Flange Offset:", key="rfo", target="hub",
            validators=[is_required, is_positive]
        )    
        self.field_rfo.grid(row=2, column=0, sticky="ew", padx=5, pady=5)

        self.field_old = InputField(
            self.form, label="Lock Nut to Lock Nut:", key="old", target="hub",
            validators=[is_required, is_positive]
        )
        self.field_old.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

        self.field_dl = InputField(
            self.form, label="L. Spoke Circle Diameter:", key="dl", target="hub",
            validators=[is_required, is_positive]

        )
        self.field_dl.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

        self.field_dr = InputField(
            self.form, label="R. Spoke Circle Diameter:", key="dr", target="hub",
            validators=[is_required, is_positive]

        )
        self.field_dr.grid(row=5, column=0, sticky="ew", padx=5, pady=5)

        self.field_shd = InputField(
            self.form, label="Spoke Hole Diameter:", key="shd", target="hub",
            validators=[is_required, is_positive]

        )
        self.field_shd.grid(row=6, column=0, sticky="ew", padx=5, pady=5)

        # RIM COLUMN (col 1)
        self.field_erd = InputField(
            self.form, label="Effective Rim Diameter:", key="erd", target="rim",
            validators=[is_required, is_positive]
        )
        self.field_erd.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        self.field_num_spokes = InputField(
            self.form, label="Number of Spokes:", key="num_spokes", target="rim",
            validators=[is_required, is_positive], field_type="combo", values=[28,32,36]
        )
        self.field_num_spokes.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        self.field_num_crosses = InputField(
            self.form, label="Number of Crosses:", key="num_crosses", target="rim",
            validators=[is_required, is_positive], field_type="combo", values=[0,1,2,3]
        )
        self.field_num_crosses.grid(row=3, column=1, sticky="ew", padx=5, pady=5)

        # store a list of fields  
        self.fields = [
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

        # button bar
        self.button_bar = ttk.Frame(self)
        self.button_bar.pack(pady=10)
        
        # Submit button
        self.calculate_btn = ttk.Button(self.button_bar, text="Calculate", command=self.on_calculate)
        self.calculate_btn.grid(row=0, column=0)

        self.clear_button = ttk.Button(self.button_bar, text="Clear", command=self.on_clear)
        self.clear_button.grid(row=0, column=1, pady=10)

        # Results box
        self.results = tk.Text(self, height=10)
        self.results.tag_config("error", foreground="red") # red text for errors
        self.results.pack(fill="both", expand=True, padx=20, pady=10)

    def on_clear(self):
        self.results.insert("end", "clear button pressed!")

        for name, field in self.fields:
            field.clear()
        
        self.results.delete("1.0", "end")

        self.hub = Hub()
        self.rim = Rim()
        self.wheel = Wheel(self.hub, self.rim)

    def poplate_model(self, field):
        """
        Assign the validated numeric value from an InputField to the
        appropriate model object (Hub or Rim).

        The field determines:
        - which model to update (via field.target: "hub" or "rim")
        - which attribute to set on that model (via field.key)
        - the numeric value to assign (converted from the field's text)
        """
        target_obj = getattr(self, field.target)
        setattr(target_obj, field.key, float(field.get())) 

    def on_calculate(self):
        self.results.delete("1.0", "end")

        errors = []
        for name, field in self.fields:
            if not field.is_valid():
                field.mark_invalid()
                errors.append(f"{name} must be a positive number.")
            else:
                field.mark_valid()
                self.poplate_model(field)                                 

        if errors:
            self.results.insert("end", "\n".join(errors) + "\n", "error")
            return

        right, left = self.wheel.make_calc()
        self.results.insert("end", f"Right Spoke Length: {right}\nLeft Spoke Length: {left}")


class InputField(ttk.Frame):
    def __init__(self, parent, label, key, target, 
    validators=None, field_type="entry", values=None, **kwargs
):
        super().__init__(parent)

       # maps to Hub or Spoke
        self.key = key  
        self.target = target

        self.field_type = field_type
        
        self.label = ttk.Label(self, text=label, width=30)
        self.label.grid(row=0, column=0, sticky="w")
        
        # combo or entry box
        if field_type == 'entry':
            self.entry = ttk.Entry(self, width=12, **kwargs)
        elif field_type == "combo":
            self.entry = ttk.Combobox(self, width = 12, values=values, state="readonly")
        self.entry.grid(row=0, column=1, sticky="ew")
        
        # for validation X
        self.icon = ttk.Label(self, text="", foreground="red", width=4)
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

    def clear(self):
        if self.field_type == "entry":
            self.entry.delete(0, "end")
        if self.field_type == "combo":
            self.entry.set("")

        # clear validation icon
        self.icon.config(text="")

        