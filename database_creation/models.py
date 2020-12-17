from .app import db
import datetime
from flask_marshmallow import Schema, fields


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
            db.Datetime,
            default = datetime.datetime.now)

    def __repr__(self):
        return f'{self.id}, {self.username}', {self.email}, {self.password}, {self.creation}


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
    creation = fields.Datetime('%y %m %d', required = True, dump_only=True)


user_schema = UserSchema()

