import tkinter as tk
from tkinter import ttk

def OpenConfirmationDialog(parent, dati):
    def confirm():
        nonlocal confirmed
        confirmed = True
        dialog.destroy()

    def goBack():
        nonlocal confirmed
        confirmed = False
        dialog.destroy()

    confirmed = False
    dialog = tk.Toplevel(parent)
    dialog.title("Riepilogo")

    tk.Label(dialog, text="Conferma i dettagli della corsa:", font=("Arial", 12)).pack(pady=10)

    for key, value in dati.items():
        tk.Label(dialog, text=f"{key.capitalize()}: {value}").pack(anchor="w", padx=20)

    ttk.Button(dialog, text="Confirm", command=confirm).pack(side="left", padx=20, pady=20)
    ttk.Button(dialog, text="Back", command=goBack).pack(side="right", padx=20, pady=20)

    dialog.transient(parent)
    dialog.grab_set()
    parent.wait_window(dialog)

    return confirmed
