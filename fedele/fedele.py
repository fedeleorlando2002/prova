# Importa i moduli necessari da Flask, pandas e matplotlib
from flask import Flask, redirect, render_template, request
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Aggiungi questa linea
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from pymongo import MongoClient

# Connessione a MongoDB
client = MongoClient('mongodb://localhost:27017/')  # Assicurati di sostituire con la tua URL di connessione
# Seleziona il database
db = client.demografia  # Sostituisci con il nome del tuo database
# Seleziona la collezione
collezione = db.calcolo_dati  # Sostituisci con il nome della tua collezione

# Inizializza l'app Flask
app = Flask(__name__)

# Pagina iniziale
@app.route('/')
def index():
    # Restituisce il modello HTML 'index.html' quando si accede alla radice del sito
    return render_template('index.html')

# Gestisce il calcolo delle percentuali e la creazione dei grafici
@app.route('/calcola_percentuale', methods=['POST'])
def calcola_percentuale():
    try:
        # Ottieni i dati dal modulo web tramite una richiesta POST
        numero_under14 = int(request.form['numero_under14'])
        numero_1564 = int(request.form['numero_1564'])
        numero_over65 = int(request.form['numero_over65'])

        # Calcola il totale della popolazione
        totale_popolazione = numero_under14 + numero_1564 + numero_over65

        # Calcola le percentuali per ciascuna fascia d'età
        percentuale_under14 = (numero_under14 / totale_popolazione) * 100
        percentuale_1564 = (numero_1564 / totale_popolazione) * 100
        percentuale_over65 = (numero_over65 / totale_popolazione) * 100

        # Creazione del grafico a cerchio (torta)
        plt.figure()  # Crea una nuova figura
        data = {
            'Fasce d\'età': ['Under 14', '15-64', 'Over 65'],
            'Valore': [numero_under14, numero_1564, numero_over65]
        }
        df_pie = pd.DataFrame(data)
        labels = ['Under 14', '15-64', 'Over 65']
        sizes = [percentuale_under14, percentuale_1564, percentuale_over65]
        colors = ['red', 'blue', 'orange']
        explode = (0.1, 0, 0)  # Per evidenziare una fetta (opzionale)

        # Crea il grafico a torta
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=180)
        plt.axis('equal')  # Imposta l'aspetto del grafico a cerchio

        # Converti il grafico a torta in un formato base64
        pie_chart_buffer = BytesIO()
        plt.savefig(pie_chart_buffer, format='png')
        pie_chart_base64 = base64.b64encode(pie_chart_buffer.getvalue()).decode('utf-8')

        # Salva i dati nel database MongoDB
        dati = {
            'numero_under14': numero_under14,
            'numero_1564': numero_1564,
            'numero_over65': numero_over65,
            'percentuale_under14': percentuale_under14,
            'percentuale_1564': percentuale_1564,
            'percentuale_over65': percentuale_over65,
        }

        print("Dati da inserire nel database:", dati)
        collezione.insert_one(dati)
        print("Dati inseriti con successo nel database.")

        # Creazione del grafico a barre
        plt.figure()  # Crea una nuova figura
        data_bar = {
            'Fasce d\'età': ['Under 14', '15-64', 'Over 65'],
            'Valore': [numero_under14, numero_1564, numero_over65]
        }
        df_bar = pd.DataFrame(data_bar)

        # Crea il grafico a barre
        plt.bar(df_bar['Fasce d\'età'], df_bar['Valore'], color=['yellow', 'purple', 'brown'])
        plt.xlabel('Fasce d\'età')
        plt.ylabel('Valore')

        # Converti il grafico a barre in un formato base64
        bar_chart_buffer = BytesIO()
        plt.savefig(bar_chart_buffer, format='png')
        bar_chart_base64 = base64.b64encode(bar_chart_buffer.getvalue()).decode('utf-8')

        # Passa i dati dei grafici alla pagina dei risultati
        return render_template('risultati.html',
                               numero_under14=numero_under14,
                               numero_1564=numero_1564,
                               numero_over65=numero_over65,
                               percentuale_under14=percentuale_under14,
                               percentuale_1564=percentuale_1564,
                               percentuale_over65=percentuale_over65,
                               pie_chart_base64=pie_chart_base64,
                               bar_chart_base64=bar_chart_base64)

    except Exception as e:
        # Gestisce le eccezioni e restituisce un messaggio di errore
        print(f"Errore durante il calcolo delle percentuali o la creazione dei grafici: {e}")
        return render_template('errore.html', errore=str(e))
    
# Nuova route per cancellare i grafici e inserire nuovi dati

@app.route('/cancella_e_inserisci', methods=['POST'])
def cancella_e_inserisci():
    try:
        # Ottieni i nuovi dati dalla richiesta POST
        nuovi_dati = request.form.getlist('nuovi_dati')

        # Inserisci i nuovi dati nella collezione senza cancellare i dati esistenti
        if nuovi_dati:
            nuovi_documenti = [{'campo': dato} for dato in nuovi_dati]
            collezione.insert_many(nuovi_documenti)

        # Redirect alla pagina iniziale dopo aver cancellato i grafici e inserito nuovi dati
        return redirect('/')

    except Exception as e:
        # Gestisce le eccezioni e restituisce un messaggio di errore
        print(f"Errore durante la cancellazione e l'inserimento di nuovi dati: {e}")
        return render_template('errore.html', errore=str(e))

if __name__ == '__main__':
    app.run(debug=True)