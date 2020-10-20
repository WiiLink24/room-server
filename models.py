from room import db


class Posters(db.Model):
    poster_id = db.Column(db.String(5), primary_key=True, unique=True)
    msg = db.Column(db.String(), nullable=False)
    movie_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(), nullable=False)
