from flask import Flask
from chronos.config import config

app = Flask(__name__)
from .urls import *
