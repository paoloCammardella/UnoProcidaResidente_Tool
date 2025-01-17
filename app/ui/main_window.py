import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from PIL import Image, ImageTk
from app.services.firebase_service import save_trip
from app.ui.confirmation_dialog import OpenConfirmationDialog

def start_UI():
    def handle_save():
        dati = {
            "nomeNave": type_combobox.get(),
            "portoPartenza": departure_combobox.get(),
            "portoArrivo": arrival_combobox.get(),
            "oraPartenza": ora_partenza_entry.get(),
            "oraArrivo": ora_arrivo_entry.get(),
            "dataInizioEsclusione": inizio_esclusione_entry.get(),
            "dataFineEsclusione": fine_esclusione_entry.get(),
            "giorniSettimana": [giorno.get() for giorno in giorno_selezionato]
        }

        ora_partenza_h, ora_partenza_m = dati["oraPartenza"].split(":")
        ora_arrivo_h, ora_arrivo_m = dati["oraArrivo"].split(":")

        inizio_esclusione_day, inizio_esclusione_month, inizio_esclusione_year = dati["dataInizioEsclusione"].split("/")
        fine_esclusione_day, fine_esclusione_month, fine_esclusione_year = dati["dataFineEsclusione"].split("/")

        formatted_dati = {
            "nomeNave": dati["nomeNave"],
            "oraPartenza": int(ora_partenza_h),
            "minutiPartenza": int(ora_partenza_m),
            "oraArrivo": int(ora_arrivo_h),
            "minutiArrivo": int(ora_arrivo_m),
            "portoPartenza": dati["portoPartenza"],
            "portoArrivo": dati["portoArrivo"],
            "giorniInizioEsclusione": int(inizio_esclusione_day),
            "meseInizioEsclusione": int(inizio_esclusione_month),
            "annoInizioEsclusione": int(inizio_esclusione_year),
            "giorniFineEsclusione": int(fine_esclusione_day),
            "meseFineEsclusione": int(fine_esclusione_month),
            "annoFineEsclusione": int(fine_esclusione_year),
            "giorniSettimana": dati["giorniSettimana"]
        }

        if not (ora_partenza_h.isdigit() and ora_partenza_m.isdigit()):
            messagebox.showerror("Errore", "Formato ora partenza non valido. Usa hh:mm.")
            return

        if not (ora_arrivo_h.isdigit() and ora_arrivo_m.isdigit()):
            messagebox.showerror("Errore", "Formato ora arrivo non valido. Usa hh:mm.")
            return

        if dati["portoPartenza"] == dati["portoArrivo"]:
            messagebox.showerror("Errore", "I porti di partenza e arrivo devono essere diversi!")
            return

        confirmed = OpenConfirmationDialog(root, dati)
        if confirmed:
            try:
                save_trip(**formatted_dati)
                messagebox.showinfo("Successo", "Corsa salvata con successo!")
                type_combobox.set("")
                departure_combobox.set("")
                arrival_combobox.set("")
                ora_partenza_entry.delete(0, tk.END)
                ora_arrivo_entry.delete(0, tk.END)
                giorno_selezionato.set([0] * 7)
            except Exception as e:
                messagebox.showerror("Errore", f"Impossibile salvare la corsa: {e}")

    def show_calendar(entry_field):
        def select_date(selected_date):
            entry_field.delete(0, tk.END)
            entry_field.insert(0, selected_date)
            calendar_window.destroy()

        calendar_window = tk.Toplevel(root)
        calendar_window.overrideredirect(True)

        calendar_window.geometry(f"+{root.winfo_x() + 100}+{root.winfo_y() + 100}")

        calendar = Calendar(calendar_window, selectmode="day", date_pattern="dd/mm/yyyy")
        calendar.pack(padx=10, pady=10)
        select_button = tk.Button(calendar_window, text="Seleziona", command=lambda: select_date(calendar.get_date()))
        select_button.pack(pady=5)

    ports = ['Napoli', 'Procida', 'Pozzuoli', 'Ischia', 'Napoli Porta di Massa', 'Napoli Mergellina', 'Casamicciola',
             'Monte di Procida']
    trasports = ['Aliscafo Caremar', 'Aliscafo SNAV', 'Traghetto Caremar', 'Traghetto LazioMar', 'Gestur', 'Medmar',
                 'Ippocampo', 'Scotto Line', 'Aliscafo Alilauro']

    root = tk.Tk()
    root.title("Uno Procida")
    root.geometry("600x600")

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=3)
    root.columnconfigure(2, weight=1)

    for i in range(13):
        root.rowconfigure(i, weight=1)

    tk.Label(root, text="Mezzo di trasporto:").grid(row=2, column=0, pady=10, padx=10, sticky="w")
    type_combobox = ttk.Combobox(root, values=trasports)
    type_combobox.grid(row=2, column=1, padx=10, sticky="ew")

    tk.Label(root, text="Porto partenza:").grid(row=3, column=0, pady=10, padx=10, sticky="w")
    departure_combobox = ttk.Combobox(root, values=ports)
    departure_combobox.grid(row=3, column=1, padx=10, sticky="ew")

    tk.Label(root, text="Porto arrivo:").grid(row=4, column=0, pady=10, padx=10, sticky="w")
    arrival_combobox = ttk.Combobox(root, values=ports)
    arrival_combobox.grid(row=4, column=1, padx=10, sticky="ew")

    tk.Label(root, text="Ora partenza (hh:mm):").grid(row=5, column=0, pady=10, padx=10, sticky="w")
    ora_partenza_entry = tk.Entry(root)
    ora_partenza_entry.grid(row=5, column=1, padx=10, sticky="ew")

    tk.Label(root, text="Ora arrivo (hh:mm):").grid(row=6, column=0, pady=10, padx=10, sticky="w")
    ora_arrivo_entry = tk.Entry(root)
    ora_arrivo_entry.grid(row=6, column=1, padx=10, sticky="ew")

    tk.Label(root, text="Giorni inizio esclusione:").grid(row=7, column=0, pady=10, padx=10, sticky="w")
    inizio_esclusione_entry = tk.Entry(root)
    inizio_esclusione_entry.grid(row=7, column=1, padx=10, sticky="ew")

    tk.Label(root, text="Giorni fine esclusione:").grid(row=8, column=0, pady=10, padx=10, sticky="w")
    fine_esclusione_entry = tk.Entry(root)
    fine_esclusione_entry.grid(row=8, column=1, padx=10, sticky="ew")

    tk.Label(root, text="Giorno della settimana:").grid(row=9, column=0, pady=10, padx=10, sticky="w")

    checkbox_frame = tk.Frame(root)
    checkbox_frame.grid(row=9, column=1, padx=10, sticky="w")

    giorno_selezionato = [tk.IntVar() for _ in range(7)]
    giorni_settimana = ["Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom"]

    for i, giorno in enumerate(giorni_settimana):
        cb = tk.Checkbutton(checkbox_frame, text=giorno, variable=giorno_selezionato[i])
        cb.pack(side="left", padx=5)

    save_button = tk.Button(root, text="Salva", command=handle_save)
    save_button.grid(row=10, column=0, columnspan=3, pady=20)

    root.mainloop()
