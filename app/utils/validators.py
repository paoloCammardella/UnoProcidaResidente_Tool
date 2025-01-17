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
