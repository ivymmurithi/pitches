from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig, Config

app = Flask(__name__)
app.config.from_object(DevConfig)
app.config['SECRET_KEY']=Config.SECRET_KEY
db = SQLAlchemy(app)
