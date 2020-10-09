from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://database.db'
db.init_app(app)