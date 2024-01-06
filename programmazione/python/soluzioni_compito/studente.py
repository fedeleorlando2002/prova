from flask import Flask, request, jsonify
from http import HTTPStatus
from time import time
from datetime import date
app = Flask(__name__)

studenti = [
    {
        'id': 1,
        'nome': 'nome1',
        'cognome': 'cognome1',
        'data_di_nascita': date(2001, 1, 11),  # yyyy, mm, dd
        'luogo_di_nascita': 'luogo1',
        'sesso': 'M',
        'media_voti': 91,
        'nazionalita': 'nazionalita1',
        'corso_di_laurea': 'corso1',
        'anno_di_iscrizione': date(2011, 1, 11)  # yyyy, mm, dd
    },
    {
        'id': 2,
        'nome': 'nome2',
        'cognome': 'cognome2',
        'data_di_nascita': date(2002, 2, 12),  # yyyy, mm, dd
        'luogo_di_nascita': 'luogo2',
        'sesso': 'M',
        'media_voti': 92,
        'nazionalita': 'nazionalita2',
        'corso_di_laurea': 'corso2',
        'anno_di_iscrizione': date(2012, 2, 12)  # yyyy, mm, dd
    },
    {
        'id': 3,
        'nome': 'nome3',
        'cognome': 'cognome3',
        'data_di_nascita': date(2003, 3, 13),  # yyyy, mm, dd
        'luogo_di_nascita': 'luogo3',
        'sesso': 'M',
        'media_voti': 93,
        'nazionalita': 'nazionalita3',
        'corso_di_laurea': 'corso3',
        'anno_di_iscrizione': date(2013, 3, 13)  # yyyy, mm, dd
    },
]


@app.route('/')
def default():
    return 'Pagina studente'


@app.route('/studente', methods=['GET'])
def get_all():
    return jsonify(studenti), HTTPStatus.OK


@app.route('/studente/<int:id>', methods=['GET'])
def get_by_id(id):
    studente = next(
        (studente for studente in studenti if studente['id'] == id), None)
    if studente:
        return jsonify(studente), HTTPStatus.OK
    else:
        return jsonify({
            'error': 'ID not found',
            'status': 'error'
        }), HTTPStatus.NOT_FOUND

    # variante con ciclo 'for' al posto di 'next'
    # for studente in data:
    #     if studente['id'] == id:
    #         return jsonify(studente), HTTPStatus.OK
    # return jsonify({
    #     'error': 'ID not found',
    #     'status': 'error'
    # }), HTTPStatus.NOT_FOUND


@app.route('/studente', methods=['POST'])
def insert():
    studente = request.json
    # genera un id univoco basandosi sul timestamp corrente e lo assegna a studente['id']
    studente['id'] = int(time() * (10 ** 7))
    studenti.append(studente)
    return jsonify(studente), HTTPStatus.OK


@app.route('/studente/<int:id>', methods=['PUT'])
def updat_by_id(id):
    studente = next(
        (studente for studente in studenti if studente['id'] == id), None)
    if studente:
        studente.update(request.json)
        return jsonify(studenti), HTTPStatus.OK
    else:
        return jsonify({
            'error': 'ID not found',
            'status': 'error'
        }), HTTPStatus.NOT_FOUND


@app.route('/studente/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    studente = next(
        (studente for studente in studenti if studente['id'] == id), None)
    if studente:
        studenti.remove(studente)
        return jsonify(studenti), HTTPStatus.OK
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
