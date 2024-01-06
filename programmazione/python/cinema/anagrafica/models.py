import sqlalchemy as sa
from common import db

class AnagraficaModel(db.Model):

    id = sa.Column(sa.Integer, primary_key=True)
    nome = sa.Column(sa.String(20), nullable=False)
    cognome = sa.Column(sa.String(20), nullable=False)
    data_di_nascita = sa.Column(sa.Date, nullable=False)
    password = sa.Column(sa.String(255), nullable=False)
    email = sa.Column(sa.String(255), nullable=False, unique=True)
    telefono = sa.Column(sa.Integer, nullable=True)



