import os
from flask import Flask
from database_creation.app import db
from config import config


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config.update(DATABASE=os.path.join(app.root_path, 'artists.db'))
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///artists.db"
    db.init_app(app)

    with app.app_context():
        db.create_all()
    return app


def create_database():
    app = create_app()
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    create_app()
    create_database()
