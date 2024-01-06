from flask import Flask, request, jsonify
from http import HTTPStatus

app = Flask("shop")

storage = [
    {
        "id" : 1,
        "type" : "T-shirt",
        "size" : {
            "s": 3, 
            "m": 5,
            "l": 2 
            },
        "color" : {
            "red" : 7,
            "blue" : 5,
            "black" : 2
            }
    },
    {
        "id" : 2,
        "type" : "Jumper",
        "size" : {
            "s": 3, 
            "m": 0,
            "l": 2 
            },
        "color" : {
            "red" : 7,
            "blue" : 5,
            "black" : 2
            }
    },
    {
        "id" : 3,
        "type" : "Jacket",
        "size" : {
            "s": 3, 
            "m": 0,
            "l": 2 
            },
        "color" : {
            "red" : 7,
            "blue" : 5,
            "black" : 2
            }
    },
    {
        "id" : 4,
        "type" : "Cargo",
        "size" : {
            "s": 3, 
            "m": 0,
            "l": 2 
            },
        "color" : {
            "red" : 7,
            "blue" : 5,
            "black" : 2
            }
},
]


@app.route("/storage/size/<string:size>")
def get_storage_by_size(size):
    size_filtered = []
    for clothes in storage:
        if clothes["size"][size] > 0:
            size_filtered.append({clothes["type"] : clothes["size"][size]})
            # size_filtered.append(clothes)
    return jsonify(size_filtered)


@app.route("/storage/color/<string:color>")
def get_storage_by_color(color):
    color_filtered = []
    for clothes in storage:
        if clothes["color"][color] > 0:
            color_filtered.append(clothes)
    return jsonify(color_filtered)


dizionario = {
    "chiave_dizionario_1" : {"chiave_dizionario_2" : "valore"}
}

dizionario["chiave_dizionario_1"]["chiave_dizionario_2"]















