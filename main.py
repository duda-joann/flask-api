from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://database.db'
db = SQLAlchemy(app)


url = "http://makeup-api.herokuapp.com/api/v1/products.json"