import tkinter as tk
from tkinter import ttk, messagebox
from app.services.firebase_service import save_trip
from app.ui.confirmation_dialog import OpenConfirmationDialog
from app.utils.validators import update_arrival_options, format_time_entry, format_date_entry


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
            "giorniSettimana": get_selected_days_as_string(),
            "prezzoIntero": prezzo_intero_entry.get(),
            "prezzoRidotto": prezzo_ridotto_entry.get()

        }

        ora_partenza_h, ora_partenza_m = dati["oraPartenza"].split(":");
        ora_arrivo_h, ora_arrivo_m = dati["oraArrivo"].split(":");

        formatted_dati = {
            "nomeNave": dati["nomeNave"],
            "oraArrivo": ora_arrivo_h + ":" + ora_arrivo_m + ":00",
            "oraPartenza": ora_partenza_h + ":" + ora_partenza_m + ":00",
            "portoPartenza": dati["portoPartenza"],
            "portoArrivo": dati["portoArrivo"],
            "inizioEsclusione": dati["dataInizioEsclusione"],
            "fineEsclusione": dati["dataFineEsclusione"],
            "giorniSettimana": dati["giorniSettimana"],
            "prezzoIntero": dati["prezzoIntero"],
            "prezzoRidotto": dati["prezzoRidotto"]
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
                for var in giorno_selezionato:
                    var.set(0)

            except Exception as e:
                messagebox.showerror("Errore", f"Impossibile salvare la corsa: {e}")

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

    departure_var = tk.StringVar()
    arrival_var = tk.StringVar()

    tk.Label(root, text="Porto partenza:").grid(row=3, column=0, pady=10, padx=10, sticky="w")
    departure_combobox = ttk.Combobox(root, textvariable=departure_var, values=ports)
    departure_combobox.grid(row=3, column=1, padx=10, sticky="ew")

    tk.Label(root, text="Porto arrivo:").grid(row=4, column=0, pady=10, padx=10, sticky="w")
    arrival_combobox = ttk.Combobox(root, textvariable=arrival_var, values=ports)
    arrival_combobox.grid(row=4, column=1, padx=10, sticky="ew")

    departure_var.trace_add("write", lambda name, index, operation: update_arrival_options(departure_var, arrival_var, ports, arrival_combobox))

    ora_partenza_var = tk.StringVar()
    ora_arrivo_var = tk.StringVar()

    ora_partenza_entry = tk.Entry(root, textvariable=ora_partenza_var)
    ora_arrivo_entry = tk.Entry(root, textvariable=ora_arrivo_var)

    ora_partenza_var.trace_add(
        "write", lambda var, index, mode: format_time_entry(ora_partenza_entry, ora_partenza_var, index, mode)
    )
    ora_arrivo_var.trace_add(
        "write", lambda var, index, mode: format_time_entry(ora_arrivo_entry, ora_arrivo_var, index, mode)
    )

    # Layout
    tk.Label(root, text="Ora partenza (hh:mm):").grid(row=5, column=0, pady=10, padx=10, sticky="w")
    ora_partenza_entry.grid(row=5, column=1, padx=10, sticky="ew")

    tk.Label(root, text="Ora arrivo (hh:mm):").grid(row=6, column=0, pady=10, padx=10, sticky="w")
    ora_arrivo_entry.grid(row=6, column=1, padx=10, sticky="ew")

    inizio_esclusione_var = tk.StringVar()
    fine_esclusione_var = tk.StringVar()

    inizio_esclusione_entry = tk.Entry(root, textvariable=inizio_esclusione_var)
    fine_esclusione_entry = tk.Entry(root, textvariable=fine_esclusione_var)

    inizio_esclusione_var.trace_add(
        "write", lambda var, index, mode: format_date_entry(inizio_esclusione_entry, inizio_esclusione_var)
    )
    fine_esclusione_var.trace_add(
        "write", lambda var, index, mode: format_date_entry(fine_esclusione_entry, fine_esclusione_var)
    )

    # Layout
    tk.Label(root, text="Data inizio esclusione:").grid(row=7, column=0, pady=10, padx=10, sticky="w")
    inizio_esclusione_entry.grid(row=7, column=1, padx=10, sticky="ew")

    tk.Label(root, text="Data fine esclusione:").grid(row=8, column=0, pady=10, padx=10, sticky="w")
    fine_esclusione_entry.grid(row=8, column=1, padx=10, sticky="ew")

    prezzo_intero_var = tk.DoubleVar()
    prezzo_ridotto_var = tk.DoubleVar()

    prezzo_intero_entry = tk.Entry(root, textvariable=prezzo_intero_var)
    prezzo_ridotto_entry = tk.Entry(root, textvariable=prezzo_ridotto_var)

    tk.Label(root, text="Prezzo intero:").grid(row=9, column=0, pady=10, padx=10, sticky="w")
    prezzo_intero_entry.grid(row=9, column=1, padx=10, sticky="ew")
    
    tk.Label(root, text="Prezzo ridotto:").grid(row=10, column=0, pady=10, padx=10, sticky="w")
    prezzo_ridotto_entry.grid(row=10, column=1, padx=10, sticky="ew")

    tk.Label(root, text="Giorno della settimana:").grid(row=11, column=0, pady=10, padx=10, sticky="w")

    checkbox_frame = tk.Frame(root)
    checkbox_frame.grid(row=11, column=1, padx=10, sticky="w")

    # List of IntVar for each day of the week (7 days)
    giorno_selezionato = [tk.IntVar() for _ in range(7)]
    giorni_settimana = ["Lun", "Mar", "Mer", "Gio", "Ven", "Sab", "Dom"]

    def get_selected_days_as_string():
        selected_days = ""
        for i, var in enumerate(giorno_selezionato):
            if var.get() == 1:
                selected_days += str(i + 1)
        return selected_days

    for i, giorno in enumerate(giorni_settimana):
        cb = tk.Checkbutton(checkbox_frame, text=giorno, variable=giorno_selezionato[i])
        cb.pack(side="left", padx=5)

    def show_selected_days():
        selected_days = get_selected_days_as_string()
        print(f"Selected days: {selected_days}")

    save_button = tk.Button(root, text="Salva", command=handle_save)
    save_button.grid(row=12, column=0, columnspan=3, pady=20)

    root.mainloop()
