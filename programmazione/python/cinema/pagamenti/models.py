import sqlalchemy as sa
from common import db
from ordini.models import OrdersModel

VIRTUALE = 1
CONTANTI = 2

ACCETTATO = 1
RESPINTO = 2

class CarteModel(db.Model):

    id = sa.Column(sa.Integer, primary_key=True)
    intestatario = sa.Column(sa.String(255), nullable=False)
    n_carta = sa.Column(sa.String(20), nullable=False)
    scadenza = sa.Column(sa.Date, nullable=False)
    cvc = sa.Column(sa.Integer, nullable=False)

class PagamentiModel(db.Model):

    id = sa.Column(sa.Integer, primary_key=True)
    payment_id = sa.Column(sa.String(10), unique=False)
    orders_id = sa.Column(sa.ForeignKey(OrdersModel.id), nullable=False)
    dataora = sa.Column(sa.DateTime, nullable=False)
    metodo = sa.Column(sa.Integer, nullable=False)
    stato = sa.Column(sa.Integer, nullable=False)
    card_id = sa.Column(sa.ForeignKey(CarteModel.id), nullable=True)

