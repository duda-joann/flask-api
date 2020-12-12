import os
from flask import Flask
from database_creation.app import db

app = Flask(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'artists.db')))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///artists.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()


