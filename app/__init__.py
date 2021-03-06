# Standard library imports
import os

# Related third party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

# Local app specific imports
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_POOL_SIZE'] = 20
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 50
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
SCHEMA_NAME = os.getenv("SCHEMA_NAME")

from app.home.routes import home_api
from app.responsibilties.routes import responsibilties_api
from app.noticeboard.routes import noticeboard_api

app.register_blueprint(home_api)
app.register_blueprint(noticeboard_api)
app.register_blueprint(responsibilties_api)

from app.utils.app_functions import (
    before_request,
    after_request,
)
