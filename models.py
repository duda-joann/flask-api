from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Products(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    imaqe_link: db.Column(db.String, nullable=True)
    product_link = db.Column(db.String, nullable=True)
    currency = db.Column(db.String)
    description = db.Column(db.Text)
    category = db.Column(db.String)
    product_type = db.Column(db.Sring)


class Cosmetic(db.Model):
    __tablename__ = "Cosmetic"
    brand = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    color_hex_value = db.Column(db.String, nullable=False)
    color_name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=True)
