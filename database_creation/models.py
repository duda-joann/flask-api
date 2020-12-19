from .app import db
import datetime
from flask_marshmallow import Schema, fields
from marshmallow.validate import Length
from werkzeug.security import generate_password_hash


class Artists(db.Model):
    """Data model for artists data"""
    __tablename__= 'Artists'
    id = db.Column(
            db.Integer,
            primary_key=True,
            autoincrement=True
    )
    name = db.Column(
        db.String,
        nullable=False
    )
    playcount = db.Column(
            db.Integer,
            nullable=False
    )
    listeners = db.Column(
            db.Integer,
            nullable=False
    )
    mbid = db.Column(
            db.String,
            nullable=False
    )

    def __repr__(self):
        return f'{self.id}, {self.playcount}, {self.name}, {self.listeners}, {self.mbid}'


class Users(db.Model):
    " Model for user's data"
    id = db.Column(
        db.Integer,
        primary_key = True
    )
    username = db.Column(
            db.String(255),
            nullable=False,
            unique = True
    )
    email = db.Column(
            db.String(255),
            nullable=False,
            unique=True
    )
    password = db.Column(
            db.String(255),
            nullable=False,
            unique=True)
    creation = db.Column(
            db.DateTime,
            default = datetime.datetime.now)

    def __repr__(self):
        return f'{self.id}, {self.username}', {self.email}, {self.password}, {self.creation}

    @staticmethod
    def generate_hashed_password(password):
        return generate_password_hash(password)


    def generate_jwt(self):
        payload = {
            'user_id': self.id,
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=30)
        }
        return payload.encode()

class UserSchema(Schema):
    id = fields.Integer(
            dump_only=True,
    )
    username = fields.String(
            required=True,
            validate=Length(min=5, max=255)
    )
    password = fields.String(
            required=True,
            validate=Length(min=8, max=255)
    )
    creation = fields.DateTime(
            '%y %m %d',
            required = True,
            dump_only=True
    )


user_schema = UserSchema()


