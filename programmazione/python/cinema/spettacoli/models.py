import sqlalchemy as sa
from common import db

class SalaModel(db.Model):
    
    id = sa.Column(sa.Integer, primary_key=True)
    nome = sa.Column(sa.String(10), unique=True, nullable=False)
    posti_totali = sa.Column(sa.Integer, nullable=False)

class PostiModel(db.Model):

    id = sa.Column(sa.Integer, primary_key=True)
    riga = sa.Column(sa.String(2), nullable=False)
    colonna = sa.Column(sa.Integer, nullable=False)
    sala_id = sa.Column(sa.ForeignKey(SalaModel.id), nullable=False)

class GenereModel(db.Model):

    id = sa.Column(sa.Integer, primary_key=True)
    nome = sa.Column(sa.String(20), nullable=False)

class FilmModel(db.Model):

    id = sa.Column(sa.Integer, primary_key=True)
    genere_id = sa.Column(sa.ForeignKey(GenereModel.id), nullable=False)
    titolo = sa.Column(sa.String(255), nullable=False)
    anno = sa.Column(sa.Integer, nullable=False)
    regia = sa.Column(sa.String(40), nullable=False)
    attori = sa.Column(sa.String(255), nullable=False)
    durata_min = sa.Column(sa.Integer, nullable=False)
    trama = sa.Column(sa.Text)
    lingua = sa.Column(sa.String(10))
    vm = sa.Column(sa.Boolean, nullable=False, default=False)
    is_3d = sa.Column(sa.Boolean, nullable=False, default=False)

class DateModel(db.Model):

    id = sa.Column(sa.Integer, primary_key=True)
    film_datetime = sa.Column(sa.DateTime, nullable=False)
    sala_id = sa.Column(sa.ForeignKey(SalaModel.id), nullable=False)
    film_id = sa.Column(sa.ForeignKey(FilmModel.id), nullable=False)

class PrezzoModel(db.Model):

    id = sa.Column(sa.Integer, primary_key=True)
    film_id = sa.Column(sa.ForeignKey(FilmModel.id), nullable=False)
    prezzo_infra = sa.Column(sa.DECIMAL(4,2), nullable=False)
    prezzo_we = sa.Column(sa.DECIMAL(4,2), nullable=False)