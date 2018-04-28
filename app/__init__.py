from flask import Flask
from flaskext.mysql import MySQL
from app.config import BaseConfig


app = Flask(__name__)
db = MySQL()
app.config.from_object(BaseConfig)
db.init_app(app)

from app import routes

