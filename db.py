from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig, Config, ProdConfig

app = Flask(__name__)
app.config.from_object(ProdConfig)
app.config['SECRET_KEY']=Config.SECRET_KEY
db = SQLAlchemy(app)
