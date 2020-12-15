from .app import db


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




