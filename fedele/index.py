import numpy as np
import matplotlib.pyplot as plt

# Dati demografici reali
gruppi_etnici = ['Bianchi', 'Afroamericani', 'Ispanici', 'Asiatici','Indiano americano/nativo dell\'Alaska']
popolazione = np.array([191000000, 46000000, 65000000, 20000000,3700000])  # Popolazione per ciascun gruppo etnico (in milioni)
tasso_fertilita = np.array([1.59, 1.67, 1.89, 1.35, 1.47])  # Tasso di fertilità per ciascun gruppo etnico

# Creazione del grafico a dispersione
plt.figure(figsize=(10, 6))
plt.scatter(popolazione, tasso_fertilita, label='Tasso di Fertilità delle vari gruppi etnici 2021')

# Imposta valori specifici sull'asse x
valori_x = [50000000,100000000,150000000,200000000]
plt.xticks(valori_x, valori_x)

# Imposta valori specifici sull'asse y
valori_y = [1.20, 1.40, 1.60, 1.80, 2]
plt.yticks(valori_y, valori_y)

plt.ylabel('Tasso di Fertilità')
plt.xlabel('Popolazione')
plt.title('Dati Demografici Reali')

# Aggiungi etichette dei gruppi etnici
for i, gruppo_etnico in enumerate(gruppi_etnici):
    plt.text(popolazione[i], tasso_fertilita[i], gruppo_etnico, fontsize=9, ha='center')

plt.legend()
plt.show()




