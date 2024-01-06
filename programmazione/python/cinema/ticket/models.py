import sqlalchemy as sa
from common import db
from spettacoli.models import DateModel



class TicketModel(db.Model):

    id = sa.Column(sa.Integer, primary_key=True)
    ticket_id = sa.Column(sa.String(15), unique=True)
    date_id = sa.Column(sa.ForeignKey(DateModel.id))
    utilizzato_il = sa.Column(sa.DateTime, nullable=True)