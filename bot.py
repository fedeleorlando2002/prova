import time 
import pywhatkit as kit 
# Specifica il numero di telefono (con il prefisso internazionale) e il messaggio
phone_number = "+393501525391"
message = "Vuoi prenotare la visita" 
# Invia il messaggio immediatamente
kit.sendwhatmsg_instantly(phone_number, message)
time.sleep(6) 

def leggi_risposta():
    # Leggi la risposta dell'utente
    risposta = input("Inserisci la tua risposta (si, va bene / un'altra volta): ")
    return risposta.lower()

def main():
    
    # Aspetta la risposta dell'utente
    risposta_utente = leggi_risposta()

    # Analizza la risposta dell'utente
    if "si" in risposta_utente:
        print("Prenotazione confermata!")
        # Aggiungi qui il codice per la gestione della prenotazione confermata
    elif "altra volta" in risposta_utente or "un'altra volta" in risposta_utente:
        print("Ok, un'altra volta.")
        # Aggiungi qui il codice per gestire la risposta "un'altra volta"
        risposta = input("quando: ")
        input("Inserisci la tua risposta (ok, ottimo / no, non va bene): ")
    else:
        print("Risposta non valida.")

if __name__ == "__main__":
    main()
















#import random
#import pyautogui as pg
#import time
# 3922559982
#animal=('monkey','donkey','dog')

#time.sleep(6)

#for i in range(50):
    #a=random.choice(animal)
    #pg.write("you are a "+a)
    #pg.press('enter')you are a donkey

    