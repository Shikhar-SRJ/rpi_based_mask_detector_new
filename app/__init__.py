from flask import Flask
from flask_basicauth import BasicAuth
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
auth = BasicAuth(app)

from app import utils, routes

