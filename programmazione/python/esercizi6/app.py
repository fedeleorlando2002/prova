from flask import Flask, request, render_template, jsonify
from http import HTTPStatus
 
app = Flask(__name__)
 
# Lista vuota di prodotti
products = []
 
# Endpoint per ottenere la lista dei prodotti
 
 
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)
 
# Endpoint per aggiungere un nuovo prodotto
@app.route('/products', methods=['POST'])
def add_product():
    # Recupera i dati del prodotto dal form della richiesta
    product = {
        'id': request.form['id'],
        'name': request.form['name'],
        'description': request.form['description'],
        'price': request.form['price']
    }
    # Aggiunge il nuovo prodotto alla lista dei prodotti
    products.append(product)
    return render_template('index.html', products=products)
 
# Endpoint per aggiornare un prodotto esistente
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    # Recupera i dati del prodotto aggiornato dal form della richiesta
    updated_product = {
        'id': request.form['id'],
        'name': request.form['name'],
        'description': request.form['description'],
        'price': request.form['price']
    }
    # Cerca il prodotto da aggiornare nella lista dei prodotti
    for product in products:
        if product['id'] == product_id:
            # Aggiorna i dati del prodotto
            product.update(updated_product)
            return render_template('index.html', products=products)
    # Se il prodotto non viene trovato, restituisce un messaggio di errore
    return 'Prodotto non trovato', HTTPStatus.NOT_FOUND
 
# Endpoint per visualizzare la pagina di inserimento di un nuovo prodotto
@app.route('/add_product', methods=['GET'])
def add_product_page():
    return render_template('add_product.html')
 
# Endpoint per visualizzare la pagina di modifica di un prodotto esistente
 
 
@app.route('/update_product/<int:product_id>', methods=['GET'])
def update_product_page(product_id):
    # Cerca il prodotto da aggiornare nella lista dei prodotti
    for product in products:
        if product['id'] == product_id:
            # Restituisce la pagina di modifica del prodotto
            return render_template('update_product.html', product=product)
    # Se il prodotto non viene trovato, restituisce un messaggio di errore
    return 'Prodotto non trovato', HTTPStatus.NOT_FOUND
 
 
if name == 'main':
    app.run()