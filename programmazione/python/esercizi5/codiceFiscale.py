from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)



anagrafica = [
    {
        "id" : 1,
        "nome" : "Mario",
        "cognome" : "Rossi",
        "eta" : "24",
        "data" : "1/1/1999",
        "comune" : "Massafra",
        "provincia" : "Taranto"
    },
    {
        "id" : 2,
        "nome" : "Giuseppe",
        "cognome" : "Bianchi",
        "eta" : "22",
        "data" : "13/12/2000",
        "comune" : "Massa Carrara",
        "provincia" : "Taranto"
    },
    {
        "id" : 3,
        "nome" : "Antonio",
        "cognome" : "Verdi",
        "eta" : "11",
        "data" : "11/11/2011",
        "comune" : "Taranto",
        "provincia" : "Taranto"
    },
    {
        "id" : 4,
        "nome" : "Pasquale",
        "cognome" : "Carrera",
        "eta" : "27",
        "data" : "5/5/1995",
        "comune" : "Lecce",
        "provincia" : "Lecce"
    }
]

@app.route("/", methods=["GET"])
def get_all():
    return jsonify(anagrafica)

@app.route("/comune/<string:comune>", methods=["GET"])
def get_comune(comune):
    comune_filtered = []
    for paese in anagrafica:
        if (paese["comune"].lower()).startswith(comune):
            comune_filtered.append({"nome": paese["nome"], "cognome": paese["cognome"], "comune" : paese["comune"]})
    return jsonify(comune_filtered)
    
@app.route("/provincia/<string:provincia>", methods=["GET"])
def get_provincia(provincia):
    provincia_filtered = []
    for paese in anagrafica:
        if (paese["provincia"].lower()).startswith(provincia):
            provincia_filtered.append({"nome": paese["nome"], "cognome": paese["cognome"], "provincia" : paese["provincia"]})
    return jsonify(provincia_filtered)

@app.route("/anagrafica/add", methods=["POST"])
def add_persona():
    new_persona = request.json
    new_persona["id"] = len(anagrafica) + 1
    anagrafica.append(new_persona)
    return jsonify(new_persona)

@app.route("/anagrafiche/<int:anagrafica_id>", methods=["PUT"])
def update_persona(id_lista_anagrafica):
    for id in anagrafica:
        if id["id"] == id_lista_anagrafica:
            anagrafica_found = id
            anagrafica.update(request.json)
            return jsonify(anagrafica_found)

@app.route("/anagrafiche/<int:anagrafica_id>", methods=["DELETE"])
def delete_persona(id_lista_anagrafica):
    for id in anagrafica:
        if id["id"] == id_lista_anagrafica:
            anagrafica_found = id
            anagrafica.delete(anagrafica_found)
            return "contatto eliminato"#None, HTTPStatus.NO_CONTENT
  