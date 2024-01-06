from flask import Flask, request, jsonify
from http import HTTPStatus
from time import time
app = Flask(__name__)

films = [
    {
        'id': 1,
        'titolo': 'film1',
        'descrizione': 'descrizione1',
        'regista': 'regista1',
        'anno_di_uscita': 2001,
        'voto_medio': 1,
        'genere': 'genere1',
        'durata_min': 111
    },
    {
        'id': 2,
        'titolo': 'film2',
        'descrizione': 'descrizione2',
        'regista': 'regista2',
        'anno_di_uscita': 2002,
        'voto_medio': 2,
        'genere': 'genere2',
        'durata_min': 112
    },
    {
        'id': 3,
        'titolo': 'film3',
        'descrizione': 'descrizione3',
        'regista': 'regista3',
        'anno_di_uscita': 2003,
        'voto_medio': 3,
        'genere': 'genere3',
        'durata_min': 113
    },
]


@app.route('/')
def default():
    return 'Pagina film'


@app.route('/film', methods=['GET'])
def get_all():
    return jsonify(films), HTTPStatus.OK


@app.route('/film/<int:id>', methods=['GET'])
def get_by_id(id):
    film = next((film for film in films if film['id'] == id), None)
    if film:
        return jsonify(film), HTTPStatus.OK
    else:
        return jsonify({
            'error': 'ID not found',
            'status': 'error'
        }), HTTPStatus.NOT_FOUND

    # variante con ciclo 'for' al posto di 'next'
    # for film in data:
    #     if film['id'] == id:
    #         return jsonify(film), HTTPStatus.OK
    # return jsonify({
    #     'error': 'ID not found',
    #     'status': 'error'
    # }), HTTPStatus.NOT_FOUND


@app.route('/film', methods=['POST'])
def insert():
    film = request.json
    # genera un id univoco basandosi sul timestamp corrente e lo assegna a film['id']
    film['id'] = int(time() * (10 ** 7))
    films.append(film)
    return jsonify(film), HTTPStatus.OK


@app.route('/film/<int:id>', methods=['PUT'])
def updat_by_id(id):
    film = next((film for film in films if film['id'] == id), None)
    if film:
        film.update(request.json)
        return jsonify(films), HTTPStatus.OK
    else:
        return jsonify({
            'error': 'ID not found',
            'status': 'error'
        }), HTTPStatus.NOT_FOUND


@app.route('/film/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    film = next((film for film in films if film['id'] == id), None)
    if film:
        films.remove(film)
        return jsonify(films), HTTPStatus.OK
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
