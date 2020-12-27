from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask import render_template
from database_creation.models import Artists
from database_creation.create_app import create_app, db
from .helpers import token_required

app = create_app()
api = Api(app)

artists_put_args = reqparse.RequestParser()
artists_put_args.add_argument("id", type=int, help="Artist ID", required=True)
artists_put_args.add_argument("name", type=str, help="Name of the artist", required=True)
artists_put_args.add_argument("playcount", type=str, help="Amount of listenings", required=True)
artists_put_args.add_argument("listeners", type=int, help="Amount of the listeners", required=True)
artists_put_args.add_argument("mbid", type=str, help="MBID number", required=True)

artists_update_args = reqparse.RequestParser()
artists_update_args.add_argument("id", type=int, help="Artist ID", required=True)
artists_update_args.add_argument("name", type=str, help="Name of the artist is required", required=True)
artists_update_args.add_argument("playcount", type=str, help="Amount of the listenings")
artists_update_args.add_argument("likes", type=int, help="Likes on the video")
artists_update_args.add_argument("mbid", type=str, help="MBID number")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'playcount': fields.Integer,
    'listeners': fields.Integer,
    'mbid': fields.String,
}

@app.route('/', methods=['GET'])
def render_main():
    """render start page"""

    return render_template('main.html')


class ArtistAllResult(Resource):
    @marshal_with(resource_fields)
    @token_required
    def get(self):
        result = Artists.query.all()
        if not result:
            abort(404, message="Could not find any data")

        return result

class ArtistIDApi(Resource):
    @marshal_with(resource_fields)
    @token_required
    def get(self, id):
        result = Artists.query.filter_by(id=id).first()
        if not result:
            abort(404, message="Could not find artist with that id")
        return result

    @marshal_with(resource_fields)
    @token_required
    def put(self, id):
        args = artists_put_args.parse_args()
        result = Artists.query.filter_by(id=id).first()
        if result:
            abort(409, message="Artist id taken...")

        artist = Artists(
            id=id,
            name=args['name'],
            playcount=args['playcount'],
            listeners=args['listeners'],
            mbid=args['mbid'])

        db.session.add(artist)
        db.session.commit()
        return artist, 201

    @marshal_with(resource_fields)
    @token_required
    def delete(self, id):
        query = Artists.delete(id=id)
        if query:
            query.execute()
        else:
            return f'Record does not exist', 405

        db.session.commit()
        return f'', 204

    @marshal_with(resource_fields)
    @token_required
    def patch(self, id):
        args = artists_update_args.parse_args()
        result = Artists.query.filter_by(id=id).first()
        if not result:
            abort(404, message="Artist doesn't exist, cannot update")

        if args['name']:
            result.name = args['name']
        if args['playcount']:
            result.playcount = args['playcount']
        if args['listeners']:
            result.likes = args['listeners']
        if args['mbid']:
            result.likes = args['mbid']

        db.session.commit()

        return result


api.add_resource(ArtistIDApi, "/api/v1/artist/<int:id>")
api.add_resource(ArtistAllResult, "/api/v1/artists")


if __name__ == '__main__':
    app.config["DEBUG"] = True
    app.run()
