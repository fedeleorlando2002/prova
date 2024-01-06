# Inizializzazione migration: flask db init (prima volta)
# Creazione di una nuova migration: flask db migrate (in caso di aggiunta o modifica model)
# Applicazione migration al database: flask db upgrade

from flask import Flask, request, jsonify, Blueprint
from flask_migrate import Migrate
from flask.views import MethodView
from http import HTTPStatus
from common import db
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/db_cinema?charset=utf8mb4'
db.init_app(app)
migrate = Migrate(app, db)

# Import da eliminare
from anagrafica.models import AnagraficaModel
from ordini.models import OrdersModel, RigheOrdineModel, PostazioniPrenotate
from pagamenti.models import CarteModel, PagamentiModel
from spettacoli.models import SalaModel, PostiModel, GenereModel, FilmModel, DateModel, PrezzoModel
from ticket.models import TicketModel

def filter_sqlalchemy(entity):
    entity_dict = entity.__dict__
    filtered_entity = {}
    
    for key in entity_dict:
        if key != '_sa_instance_state':
            filtered_entity[key] = entity_dict[key]

    return filtered_entity
 
 

@app.errorhandler(404)
def func_404(error):
    return jsonify({'status' : 'Elemento non trovato'})

if __name__ == '__main__':
    app.run(debug=True)
