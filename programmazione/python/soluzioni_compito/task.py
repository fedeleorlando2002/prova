from flask import Flask, request, jsonify
from http import HTTPStatus
from time import time
from datetime import date
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'titolo': 'task1',
        'descrizione': 'descrizione1',
        'nome_progetto': 'progetto1',
        'data_inizio': date(2001, 1, 11),  # yyyy, mm, dd
        'data_fine': date(2011, 1, 11),  # yyyy, mm, dd,
        'ore_stimate': 1001,
        'piorita': 'priorita1'
    },
    {
        'id': 2,
        'titolo': 'task2',
        'descrizione': 'descrizione2',
        'nome_progetto': 'progetto2',
        'data_inizio': date(2002, 2, 12),  # yyyy, mm, dd
        'data_fine': date(2012, 2, 12),  # yyyy, mm, dd,
        'ore_stimate': 1002,
        'piorita': 'priorita2'
    },
    {
        'id': 3,
        'titolo': 'task3',
        'descrizione': 'descrizione3',
        'nome_progetto': 'progetto3',
        'data_inizio': date(2003, 3, 13),  # yyyy, mm, dd
        'data_fine': date(2013, 3, 13),  # yyyy, mm, dd,
        'ore_stimate': 1003,
        'piorita': 'priorita3'
    },
]


@app.route('/')
def default():
    return 'Pagina task'


@app.route('/task', methods=['GET'])
def get_all():
    return jsonify(tasks), HTTPStatus.OK


@app.route('/task/<int:id>', methods=['GET'])
def get_by_id(id):
    task = next((task for task in tasks if task['id'] == id), None)
    if task:
        return jsonify(task), HTTPStatus.OK
    else:
        return jsonify({
            'error': 'ID not found',
            'status': 'error'
        }), HTTPStatus.NOT_FOUND

    # variante con ciclo 'for' al posto di 'next'
    # for task in data:
    #     if task['id'] == id:
    #         return jsonify(task), HTTPStatus.OK
    # return jsonify({
    #     'error': 'ID not found',
    #     'status': 'error'
    # }), HTTPStatus.NOT_FOUND


@app.route('/task', methods=['POST'])
def insert():
    task = request.json
    # genera un id univoco basandosi sul timestamp corrente e lo assegna a task['id']
    task['id'] = int(time() * (10 ** 7))
    tasks.append(task)
    return jsonify(task), HTTPStatus.OK


@app.route('/task/<int:id>', methods=['PUT'])
def updat_by_id(id):
    task = next((task for task in tasks if task['id'] == id), None)
    if task:
        task.update(request.json)
        return jsonify(tasks), HTTPStatus.OK
    else:
        return jsonify({
            'error': 'ID not found',
            'status': 'error'
        }), HTTPStatus.NOT_FOUND


@app.route('/task/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    task = next((task for task in tasks if task['id'] == id), None)
    if task:
        tasks.remove(task)
        return jsonify(tasks), HTTPStatus.OK
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
