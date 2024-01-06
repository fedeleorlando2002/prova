from flask import Flask, request, jsonify
from http import HTTPStatus
from time import time
app = Flask('Orlando_Fedele')

brani = [
    {
        'id': 1,
        'titolo': 'ti amo',
        'artista': 'francesca',
        'genere': 'rap',
        'durata_min': '4',
        'nr_ascolti': '300',
        'anno': '2010',
        'album': 'ti amo'
    },
    {
        'id': 2,
        'titolo': 'giovanni',
        'artista': 'giovanni',
        'genere': 'classica',
        'durata_min': '2',
        'nr_ascolti': '100',
        'anno': '2013',
        'album': 'giovanni'
    },
    {
        'id': 3,
        'titolo': 'ciao franco',
        'artista': 'rocco',
        'genere': 'rock',
        'durata_min': '5',
        'nr_ascolti': '150',
        'anno': '2022',
        'album': 'ciao franco'
    },
]

# pagina brano
@app.route('/')
def default():
    return 'Pagina brano'

# GET
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

# POST
@app.route('/brano', methods=['POST'])
def insert():
    brano = request.json
    brano['id'] = int(time() * (10 ** 7))
    brani.append(brano)
    return jsonify(brano), HTTPStatus.OK

# PUT
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

# DELETE
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



@ app.errorhandler(404)
def page_not_found_handler(error):
    return jsonify({
        'error': 'Page not found :(',
        'code': error.code
    }), HTTPStatus.NOT_FOUND


if 'Orlando_Fedele' == '__main__':
    app.run(debug=True)