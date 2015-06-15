from flask import Flask
from chronos.config import config

app = Flask(__name__)

app.debug = config.flask.get('debug')
app.secret_key = config.flask.get('secret_key')

from .urls import *
