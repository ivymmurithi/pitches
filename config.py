import os
import secrets

class Config:
    FLASK_APP="main.py"
    SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI=os.environ["SQLALCHEMY_DATABASE_URI"]

class ProdConfig(Config):
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ["SQLALCHEMY_DATABASE_URI"]


class DevConfig(Config):
    FLASK_ENV = "development"
    SQLALCHEMY_DATABASE_URI=os.environ["SQLALCHEMY_DATABASE_URI"]


    DEBUG = True

