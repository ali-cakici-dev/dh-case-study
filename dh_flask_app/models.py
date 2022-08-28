from .extensions import db


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(80))
    shortUrl = db.Column(db.String(10), unique=True)
    counter = db.Column(db.Integer)
