# # Importa i moduli necessari da Flask, pandas e matplotlib
# from flask import Flask, redirect, render_template, request
# import pandas as pd
# import matplotlib.pyplot as plt
# import os  # Aggiunto per gestire la cancellazione dei grafici

# # Inizializza l'app Flask
# app = Flask(__name__)

# # Pagina iniziale
# @app.route('/')
# def index():
#     # Restituisce il modello HTML 'index.html' quando si accede alla radice del sito
#     return render_template('index.html')

# # Gestisce il calcolo delle percentuali e la creazione dei grafici
# @app.route('/calcola_percentuale', methods=['POST'])
# def calcola_percentuale():
#     # Ottieni i dati dal modulo web tramite una richiesta POST
#     numero_under14 = int(request.form['numero_under14'])
#     numero_1564 = int(request.form['numero_1564'])
#     numero_over65 = int(request.form['numero_over65'])
    
#     # Calcola il totale della popolazione
#     totale_popolazione = numero_under14 + numero_1564 + numero_over65
    
#     # Calcola le percentuali per ciascuna fascia d'età
#     percentuale_under14 = (numero_under14 / totale_popolazione) * 100
#     percentuale_1564 = (numero_1564 / totale_popolazione) * 100
#     percentuale_over65 = (numero_over65 / totale_popolazione) * 100

#     # Creazione del grafico a cerchio (torta)
#     plt.figure(1)  # Specifica la figura 1
#     data = {
#         'Fasce d\'età': ['Under 14', '15-64', 'Over 65'],
#         'Valore': [numero_under14, numero_1564, numero_over65]
#     }
#     df_bar = pd.DataFrame(data)
#     labels = ['Under 14', '15-64', 'Over 65']
#     sizes = [percentuale_under14, percentuale_1564, percentuale_over65]
#     colors = ['red', 'blue', 'orange']
#     explode = (0.1, 0, 0)  # Per evidenziare una fetta (opzionale)
    
#     # Crea il grafico a torta
#     plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=180)
#     plt.axis('equal')  # Imposta l'aspetto del grafico a cerchio

#     # Salva il grafico a barre in un file immagine (opzionale)
#     plt.savefig('static/fedele.png')

#     # Creazione del grafico a barre
#     plt.figure(2)  # Specifica la figura 2
#     data_bar = {
#         'Fasce d\'età': ['Under 14', '15-64', 'Over 65'],
#         'Valore': [numero_under14, numero_1564, numero_over65]
#     }
#     df_bar = pd.DataFrame(data_bar)

#     # Crea il grafico a barre
#     plt.bar(df_bar['Fasce d\'età'], df_bar['Valore'], color = ['yellow', 'purple', 'brown'])
#     plt.xlabel('Fasce d\'età')
#     plt.ylabel('Valore')

#     # Salva il grafico a barre in un file immagine (opzionale)
#     plt.savefig('static/fedele2.png')
#     plt.switch_backend('agg')

#     # Restituisce i dati per la visualizzazione nella pagina risultati
#     return render_template('risultati.html', 
#                            numero_under14=numero_under14, 
#                            numero_1564=numero_1564, 
#                            numero_over65=numero_over65,
#                            percentuale_under14=percentuale_under14,
#                            percentuale_1564=percentuale_1564,
#                            percentuale_over65=percentuale_over65)


# # Nuovo endpoint per cancellare i grafici e inserire nuovi dati
# @app.route('/cancella_e_inserisci', methods=['POST'])
# def cancella_e_inserisci():
#     # Cancella i file dei grafici esistenti
#     try:
#         os.remove('static/fedele.png')
#         os.remove('static/fedele2.png')
#     except OSError:
#         pass

#     # Inserisci nuovi dati (puoi utilizzare lo stesso codice per calcolare percentuali e creare nuovi grafici)

#     # Redirect alla pagina iniziale dopo aver cancellato i grafici
#     return redirect('/')

# # Avvia l'app Flask in modalità debug
# if __name__ == '__main__':
#     app.run(debug=True)