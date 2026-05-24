import tkinter as tk
from tkinter import ttk

from authorization import Authorization

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.auth = Authorization()
        # TODO new up the components; hub, rim, wheel

        self.title("Spoke App")
        self.geometry("450x500")
        self._build_ui()
        self._check_auth()

    def _build_ui(self):
        
        self.rowconfigure(0, weight=0)   
        self.rowconfigure(1, weight=1)   
        self.columnconfigure(0, weight=1)

        # Notebook ---
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 0))
        
        # Tab 1 ---
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Tab One")
        
        # Layout: left side expands, right side stays tight
        self.tab1.columnconfigure(0, weight=1)
        self.tab1.columnconfigure(1, weight=0)

        self.button1 = ttk.Button(
            self.tab1, text="Button One", state="disabled", command=self._on_tab1_click
        )
        self.button1.grid(row=0, column=1, padx=10, pady=10, sticky="ne")

         # Tab 2 ---
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Tab Two")
        self.tab2.columnconfigure(0, weight=1)
        self.tab2.columnconfigure(1, weight=0)

        self.button2 = ttk.Button(
            self.tab2, text="Button Two", state="disabled", command=self._on_tab2_click
        )
        self.button2.grid(row=0, column=1, padx=10, pady=10, sticky="ne")
        
        # shared log box ---
        self.log = tk.Text(self, height=6, state="disabled")
        self.log.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    
    # Logger ---
    def _log(self, message: str):
        self.log.configure(state="normal")
        self.log.insert("end", message + "\n")
        self.log.configure(state="disabled")
        self.log.see("end")

    # Button callbacks ---
    def _on_tab1_click(self):
        try:
            self.auth.require_authorization()
            self._log("Tab 1 button clicked")
        except PermissionError as e:
            self._log(str(e))

    def _on_tab2_click(self):
        try:
            self.auth.require_authorization()
            self._log("Tab 2 button clicked")
        except PermissionError as e:
            self._log(str(e))

    # ui level auth ---
    def _check_auth(self):
        this_user = self.auth.get_current_user()
        self._log(f"current user is {this_user}")
        self._log("checking authorization...")

        if self.auth.is_user_authorized(this_user):
            self._log('user is authorized')
            self._enable_features()
        else:
            self._log('user is not authorized')

    def _enable_features(self):
        self.button1.configure(state="active")
        self.button2.configure(state="active")






