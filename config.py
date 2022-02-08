import os

class Config:
    FLASK_APP="main.py"
    SQLALCHEMY_TRACK_MODIFICATION = False
    SECRET_KEY=os.environ["SECRET_KEY"]

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ["DATABASE_URL"]

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ["SQLALCHEMY_DATABASE_URI"]


class DevConfig(Config):
    FLASK_ENV = "development"
    SECRET_KEY=os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI=os.environ["SQLALCHEMY_DATABASE_URI"]


    DEBUG = True

