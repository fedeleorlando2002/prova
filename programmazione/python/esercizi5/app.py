from flask import Flask, request, jsonify
from http import HTTPStatus

app = Flask("anagrafics")
person = [
    {
        "id" : 1,
        "age" : 22,
        "name" : "fedele",
        "surname" : "orlando",
        "idcode" : "d",
        "city" : "francavilla",
    },
    {
        "id" : 2,
        "age" : 22,
        "name" : "giovanni",
        "surname" : "argentina",
        "idcode" : "c" ,
        "city" : "castellaneta",
    },
    {
        "id" : 3,
        "age" : 22,
        "name" : "franco",
        "surname" : "ciccio",
        "idcode" : "r",
        "city" : "laterza",
    },
    {
        "id" : 4,
        "age" : 22,
        "name" : "giulia",
        "surname" : "anna",
        "idcode" : "t",
        "city" : "laterza",
    },
]    

@app.route("/")
def getlist():
    return jsonify(person)

@app.route("/city/<string:city>", methods=['GET'])
def getfromlistcity(city):
    listacitta=[]
    for citta in person:
        if citta["city"] == city:
            listacitta.append(citta)
    return jsonify(listacitta)

