import os
import pathlib
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask import render_template
from flask import request, jsonify
from database_creation.app import db
from database_creation.models import Artists


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.update(dict(DATABASE=os.path.join(pathlib.Path(app.root_path),
                                        'database_creation', 'artists.db')))
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

DATABASE = os.path.join(PROJECT_ROOT, 'database_creation', 'artists.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DATABASE
db.init_app(app)

@app.route('/', methods=['GET'])
def render_main():
    """render start page"""

    return render_template('main.html')


@app.route('/api/v1/all-artists', methods=['GET'])
def get_all():
    items = Artists.query.all()
    items_json = jsonify(items)
    return render_template('all.html', items=items_json)


if __name__ == '__main__':
    app.config["DEBUG"] = True
    app.run()
