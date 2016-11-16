"""Quick and dirty elasticsearch RESTful API

@author: Jordan Taylor
@github: jtaylor32
"""
import os

from flask import Flask
from flask_cors import CORS

from app.config import (
    ProductionConfig,
    DevelopmentConfig,
)
from app.extensions import (
    migrate,
)
from app.api import api_blueprint


if os.environ.get("FLASK_ENV") == 'production':
    DefaultConfig = ProductionConfig
else:
    DefaultConfig = DevelopmentConfig


# APPLICATION FACTORY =========================================================
def create_app(config_object=DefaultConfig):
    """A flask application factory

    :param config_object: The configuration object to use.
    :returns: flask.Flask object
    """
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_object)
    register_blueprints(app)
    return app


# REGISTER BLUEPRINTS =========================================================
def register_blueprints(app):
    """Register all blueprints.

    :app: flask.Flask object
    :returns: None

    """
    app.register_blueprint(api_blueprint)
