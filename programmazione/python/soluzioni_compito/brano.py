from flask import Flask, request, jsonify
from http import HTTPStatus
from time import time
app = Flask(__name__)

brani = [
    {
        'id': 1,
        'titolo': 'brano1',
        'artista': 'artista1',
        'genere': 'genere1',
        'durata_min': 1,
        'nr_ascolti': 1001,
        'anno': 2001,
        'album': 'album1'
    },
    {
        'id': 2,
        'titolo': 'brano2',
        'artista': 'artista2',
        'genere': 'genere2',
        'durata_min': 2,
        'nr_ascolti': 1002,
        'anno': 2002,
        'album': 'album2'
    },
    {
        'id': 3,
        'titolo': 'brano3',
        'artista': 'artista3',
        'genere': 'genere3',
        'durata_min': 3,
        'nr_ascolti': 1003,
        'anno': 2003,
        'album': 'album3'
    },
]


@app.route('/')
def default():
    return 'Pagina brano'


@app.route('/brano', methods=['GET'])
def get_all():
    return jsonify(brani), HTTPStatus.OK


@app.route('/brano/<int:id>', methods=['GET'])
def get_by_id(id):
    brano = next((brano for brano in brani if brano['id'] == id), None)
    if brano:
        return jsonify(brano), HTTPStatus.OK
    else:
        return jsonify({
            'error': 'ID not found',
            'status': 'error'
        }), HTTPStatus.NOT_FOUND

    # variante con ciclo 'for' al posto di 'next'
    # for brano in data:
    #     if brano['id'] == id:
    #         return jsonify(brano), HTTPStatus.OK
    # return jsonify({
    #     'error': 'ID not found',
    #     'status': 'error'
    # }), HTTPStatus.NOT_FOUND


@app.route('/brano', methods=['POST'])
def insert():
    brano = request.json
    # genera un id univoco basandosi sul timestamp corrente e lo assegna a brano['id']
    brano['id'] = int(time() * (10 ** 7))
    brani.append(brano)
    return jsonify(brano), HTTPStatus.OK


@app.route('/brano/<int:id>', methods=['PUT'])
def update_by_id(id):
    brano = next((brano for brano in brani if brano['id'] == id), None)
    if brano:
        brano.update(request.json)
        return jsonify(brani), HTTPStatus.OK
    else:
        return jsonify({
            'error': 'ID not found',
            'status': 'error'
        }), HTTPStatus.NOT_FOUND


@app.route('/brano/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    brano = next((brano for brano in brani if brano['id'] == id), None)
    if brano:
        brani.remove(brano)
        return jsonify(brani), HTTPStatus.OK
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
