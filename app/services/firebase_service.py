import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("app/config/os-android-d463a-firebase-adminsdk-ryqo8-0ac66eec8a.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://os-android-d463a-default-rtdb.europe-west1.firebasedatabase.app/'
})

try:
    print("Connessione al Realtime Database riuscita")
except Exception as e:
    print(f"Errore nella connessione al Realtime Database: {e}")


def save_trip(nomeNave, oraPartenza, minutiPartenza, oraArrivo, minutiArrivo,
              portoPartenza, portoArrivo, giorniInizioEsclusione, meseInizioEsclusione,
              annoInizioEsclusione, giorniFineEsclusione, meseFineEsclusione,
              annoFineEsclusione, giorniSettimana):
    try:
        ref = db.reference("Transports")
        trip_data = {
            "nomeNave": nomeNave,
            "oraPartenza": oraPartenza,
            "minutiPartenza": minutiPartenza,
            "oraArrivo": oraArrivo,
            "minutiArrivo": minutiArrivo,
            "portoPartenza": portoPartenza,
            "portoArrivo": portoArrivo,
            "giorniInizioEsclusione": giorniInizioEsclusione,
            "meseInizioEsclusione": meseInizioEsclusione,
            "annoInizioEsclusione": annoInizioEsclusione,
            "giorniFineEsclusione": giorniFineEsclusione,
            "meseFineEsclusione": meseFineEsclusione,
            "annoFineEsclusione": annoFineEsclusione,
            "giorniSettimana": giorniSettimana
        }

        new_trip_ref = ref.push()
        new_trip_ref.set(trip_data)
        print("Dati salvati correttamente nel Realtime Database!")
        return True
    except Exception as e:
        print(f"Errore durante il salvataggio dei dati nel Realtime Database: {e}")
        return False
