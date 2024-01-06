from flask import Flask, request, jsonify
from http import HTTPStatus
from time import time
from uuid import uuid4
app = Flask(__name__)

prodotto = [
    {
        'id': 1,
        'nome': 'prodotto1',
        'descrizione': 'descrizione prodotto1',
        'giacenza': 10,
        'codice_identificativo': str(uuid4())
    },
    {
        'id': 2,
        'nome': 'prodotto2',
        'descrizione': 'descrizione prodotto2',
        'giacenza': 20,
        'codice_identificativo': str(uuid4())
    },
    {
        'id': 3,
        'nome': 'prodotto3',
        'descrizione': 'descrizione prodotto3',
        'giacenza': 30,
        'codice_identificativo': str(uuid4())
    },
    {
        'id': 4,
        'nome': 'prodotto4',
        'descrizione': 'descrizione prodotto4',
        'giacenza': 40,
        'codice_identificativo': str(uuid4())
    },
]


@app.route('/')
def default():
    return 'Pagina prodotto'


@app.route('/prodotti', methods=['GET'])
def get_all():
    return jsonify(prodotto), HTTPStatus.OK


@app.route('/prodotti/<int:id>', methods=['GET'])
def get_by_id(id):
    product = next((product for product in prodotto if product['id'] == id), None)
    if product:
        return jsonify(product), HTTPStatus.OK
    else:
        return jsonify({
            'error': 'ID not found',
            'status': 'error'
        }), HTTPStatus.NOT_FOUND

    # variante con ciclo 'for' al posto di 'next'
    # for product in data:
    #     if product['id'] == id:
    #         return jsonify(product), HTTPStatus.OK
    # return jsonify({
    #     'error': 'ID not found',
    #     'status': 'error'
    # }), HTTPStatus.NOT_FOUND


@app.route('/prodotti', methods=['POST'])
def insert():
    product = request.json
    # genera un id univoco basandosi sul timestamp corrente e lo assegna a product['id']
    product['id'] = int(time() * (10 ** 7))
    # genera un codice univoco utilizzando il metodo uuid4 che sfrutta il timestamp corrente e il MAC address della macchina sul quale e' stato generato e lo assegna a product['codice_identificativo']
    product['codice_identificativo'] = str(uuid4())
    prodotto.append(product)
    return jsonify(product), HTTPStatus.OK


@app.route('/prodotti/<int:id>', methods=['PUT'])
def update_by_id(id):
    product = next((product for product in prodotto if product['id'] == id), None)
    if product:
        product.update(request.json)
        return jsonify(prodotto), HTTPStatus.OK
    else:
        return jsonify({
            'error': 'ID not found',
            'status': 'error'
        }), HTTPStatus.NOT_FOUND


@app.route('/prodotti/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    product = next((product for product in prodotto if product['id'] == id), None)
    if product:
        prodotto.remove(product)
        return jsonify(prodotto), HTTPStatus.OK
    else:
        return jsonify({
            'error': 'ID not found',
            'status': 'error'
        }), HTTPStatus.NOT_FOUND


# error 404 handler
@ app.errorhandler(404)
def page_not_found_handler(error):
    return jsonify({
        'error': 'Page not found :(',
        'code': error.code
    }), HTTPStatus.NOT_FOUND


if __name__ == '__main__':
    app.run(debug=True)
