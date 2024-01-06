from flask import Blueprint, jsonify, request
from flask.views import MethodView
from http import HTTPStatus

corsi = [{
    'id' : 1,
    'nome' : 'Principi di matematica',
    'materia' : 'matematica',
    'docente' : 'rossi'
},
{
    'id' : 2,
    'nome' : 'Principi di informatica',
    'materia' : 'informatica',
    'docente' : 'gentile'
}]

blp_corsi = Blueprint("Blueprint corsi", "blp_corsi")

class Corsi(MethodView):

    def get(self):
        return jsonify(corsi)
    
    def post(self):
        new_corso = request.json
        new_corso['id'] = len(corsi) + 1
        corsi.append(new_corso)
        return jsonify(new_corso), HTTPStatus.CREATED

view_corsi = Corsi.as_view('corsi')
blp_corsi.add_url_rule("/corsi", view_func=view_corsi)
    

class Corso(MethodView):

    def get(self, corso_id):
        for c in corsi:
            if c['id'] == corso_id:
                return jsonify(c)
            
        return jsonify({"message": "Corso non trovato"}), HTTPStatus.NOT_FOUND
    

    def put(self, corso_id):
        for c in corsi:
            if c['id'] == corso_id:
                c.update(request.json)
                return jsonify(c)
            
        return jsonify({"message": "Corso non trovato"}), HTTPStatus.NOT_FOUND

    def delete(self, corso_id):
        for c in corsi:
            if c['id'] == corso_id:
                corsi.remove(c)
                return({"message": "Eliminato"})
            
        return jsonify({"message": "Corso non trovato"}), HTTPStatus.NOT_FOUND
    
view_corso = Corso.as_view('corso')
blp_corsi.add_url_rule("/corsi/<int:corso_id>", view_func=view_corso)