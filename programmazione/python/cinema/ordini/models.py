import sqlalchemy as sa
from common import db
from anagrafica.models import AnagraficaModel
from spettacoli.models import DateModel, PostiModel

class OrdersModel(db.Model):

    id = sa.Column(sa.Integer, primary_key=True)
    anagrafica_id = sa.Column(sa.ForeignKey(AnagraficaModel.id), nullable=False)
    valido = sa.Column(sa.DateTime, nullable=True)
    prezzo_totale = sa.Column(sa.DECIMAL(6,2), nullable=False)
    codice_ordine = sa.Column(sa.String(15), nullable=False)

class RigheOrdineModel(db.Model):

    id = sa.Column(sa.Integer, primary_key=True)
    order_id = sa.Column(sa.ForeignKey(OrdersModel.id), nullable=False)
    date_id = sa.Column(sa.ForeignKey(DateModel.id), nullable=False)
    quantita = sa.Column(sa.Integer, nullable=False)
    prezzo_riga = sa.Column(sa.DECIMAL(6,2), nullable=False)

class PostazioniPrenotate(db.Model):

    id = sa.Column(sa.Integer, primary_key=True)
    posto_id = sa.Column(sa.ForeignKey(PostiModel.id), nullable=False)
    data_id = sa.Column(sa.ForeignKey(DateModel.id), nullable=False)
    valido = sa.Column(sa.DateTime, nullable=True)
