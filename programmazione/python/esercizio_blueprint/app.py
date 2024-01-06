from flask import Flask
from corsi.module import blp_corsi

app = Flask("Test blueprint")

app.register_blueprint(blp_corsi )
