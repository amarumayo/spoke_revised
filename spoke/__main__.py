import tkinter as tk
from tkinter import ttk
from spoke.ui import App


def ask_choice(root: tk.Tk) -> str | None:
    # Use a plain Python container so we can store real None
    result: dict[str, str | None] = {"choice": None}

    popup = tk.Toplevel(root)
    popup.title("Choose Wheel Type")
    popup.geometry("250x150")

    ttk.Label(popup, text="Choose one:").pack(padx=20, pady=15)

    def set_choice(value: str) -> None:
        result["choice"] = value
        popup.destroy()

    def cancel() -> None:
        # Explicitly mark as cancelled
        result["choice"] = None
        popup.destroy()

    # Handle clicking the X button
    popup.protocol("WM_DELETE_WINDOW", cancel)

    ttk.Button(
        popup,
        text="Front Wheel",
        command=lambda: set_choice("front"),
    ).pack(pady=5)

    ttk.Button(
        popup,
        text="Rear Wheel",
        command=lambda: set_choice("rear"),
    ).pack(pady=5)

    # Make popup modal
    popup.transient(root)
    popup.grab_set()
    popup.update_idletasks()
    popup.wait_visibility()

    root.wait_window(popup)

    # Return the real Python value (str or None)
    return result["choice"]


def main() -> None:
    print("RUNNING MAIN")

    # Invisible but alive root
    root = tk.Tk()
    root.overrideredirect(True)
    root.geometry("0x0+0+0")

    # Run popup
    choice = ask_choice(root)
    print("Popup closed:", choice)

    # If user clicked X → exit program cleanly
    if choice is None:
        root.destroy()
        return

    # Launch main app
    app = App(root, choice)

    # Closing the app closes the entire program
    def on_app_close():
        app.destroy()
        root.destroy()

    app.protocol("WM_DELETE_WINDOW", on_app_close)

    root.mainloop()


if __name__ == "__main__":
    main()
