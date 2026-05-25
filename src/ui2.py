import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Spoke Calculator")
        self.geometry("800x600")

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
        self.field_lfo = InputField(self.form, "Left Flange Offset:")
        self.field_lfo.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

        self.field_rfo = InputField(self.form, "Right Flange Offset:")
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
        self.results.pack(fill="both", expand=True, padx=20, pady=10)

    def on_submit(self):
        # Example calculation
        lfo = self.field_lfo.get()
        rfo = self.field_rfo.get()
        old = self.field_old.get()

        result = f"LFO={lfo}, RFO={rfo}, OLD={old}\n"
        self.results.insert("end", result)


class InputField(ttk.Frame):
    def __init__(self, parent, label, **kwargs):
        super().__init__(parent)

        self.label = ttk.Label(self, text=label, width=20)
        self.label.grid(row=0, column=0, sticky="w")

        self.entry = ttk.Entry(self, **kwargs)
        self.entry.grid(row=0, column=1, sticky="ew")

        self.columnconfigure(1, weight=1)

    def get(self):
        return self.entry.get()
