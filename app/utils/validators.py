import tkinter as tk

def validate_time_format(time_str):
    try:
        hours, minutes = map(int, time_str.split(":"))
        return 0 <= hours < 24 and 0 <= minutes < 60
    except ValueError:
        return False

def validate_ports(port_departure, port_arrival):
    return port_departure != port_arrival

def validate_date_format(date_str):
    try:
        day, month, year = map(int, date_str.split("/"))
        return 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2100
    except ValueError:
        return False


# update_options.py
def update_arrival_options(departure_var, arrival_var, ports, arrival_combobox):
    """Update the options in the arrival combobox based on departure selection."""
    selected_departure = departure_var.get()

    if selected_departure == "Procida":
        # If departure is Procida, arrival combobox options exclude "Procida"
        arrival_combobox['values'] = [port for port in ports if port != "Procida"]
        arrival_var.set("")  # Clear current selection
    else:
        # If departure is not Procida, arrival is fixed to "Procida"
        arrival_combobox['values'] = ["Procida"]
        arrival_var.set("Procida")  # Automatically set to Procida


def format_date_entry(entry, string_var):
    value = string_var.get()
    new_value = ""

    digits = ''.join(filter(str.isdigit, value))

    # Format as dd/mm/yyyy
    if len(digits) >= 1:
        new_value += digits[:2]
    if len(digits) >= 3:
        new_value += "/" + digits[2:4]
    if len(digits) >= 5:
        new_value += "/" + digits[4:8]
    if len(digits) > 8:
        new_value = new_value[:10]
        
    string_var.set(new_value)

    entry.after(1, lambda: entry.icursor(tk.END))

def format_time_entry(entry, var, index, mode):
    value = var.get()
    
    cleaned_value = "".join(char for char in value if char.isdigit() or char == ":")
    
    if len(cleaned_value) > 2 and ":" not in cleaned_value:
        cleaned_value = f"{cleaned_value[:2]}:{cleaned_value[2:]}"
    elif len(cleaned_value) > 5:
        cleaned_value = cleaned_value[:5]
        
    var.set(cleaned_value)   
    entry.after(1, lambda: entry.icursor(tk.END))
