from datetime import datetime

from room import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from room import login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class ParadeMiis(db.Model):
    # We need to be able to select by both the Mii's ID and the logo.
    mii_id = db.Column(db.Integer, db.ForeignKey("mii_data.mii_id"), primary_key=True)
    logo_id = db.Column(db.String(5), primary_key=True)
    logo_bin = db.Column(db.Binary(8000))
    news = db.Column(db.String)
    level = db.Column(db.Integer, default=1)


class User(db.Model, UserMixin):
    # Used to login to the Admin Panel
    id = db.Column(db.Integer, primary_key=True, default=1)
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Posters(db.Model):
    poster_id = db.Column(db.Integer, primary_key=True, unique=True)
    msg = db.Column(db.String(15), nullable=False)
    movie_id = db.Column(db.Integer, nullable=False)
    # While a maximum of 47 characters seems arbitrary, it is what it is.
    # It appears they mandate the last byte in their char array is null (and sprintf),
    # so perhaps the internal type is char[48]?
    title = db.Column(db.String(47), nullable=False)


class PayPosters(db.Model):
    poster_id = db.Column(db.Integer, primary_key=True, unique=True)
    msg = db.Column(db.String(15), nullable=False)
    movie_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(47), nullable=False)
    type = db.Column(db.Integer, nullable=False)
    aspect = db.Column(db.Boolean, nullable=False)


class ConciergeMiis(db.Model):
    mii_id = db.Column(
        db.Integer, db.ForeignKey("mii_data.mii_id"), primary_key=True, unique=True
    )
    clothes = db.Column(db.Integer, nullable=False)
    action = db.Column(db.Integer, nullable=False)
    prof = db.Column(db.String(129), nullable=False)
    movie_id = db.Column(db.Integer, nullable=False)
    voice = db.Column(db.Boolean, nullable=False)
    update_date = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


# MiiData provides the genuine Mii alongside other common information.
class MiiData(db.Model):
    mii_id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.LargeBinary(74), nullable=False)
    name = db.Column(db.String(10), nullable=False)
    color1 = db.Column(db.String(6), nullable=False)
    color2 = db.Column(db.String(6), nullable=False)


class MiiMsgInfo(db.Model):
    # We make both the Mii's ID and message type unique, as to allow row
    # identification for SQLAlchemy.
    mii_id = db.Column(
        db.Integer, db.ForeignKey("mii_data.mii_id"), primary_key=True, nullable=False
    )
    type = db.Column(db.Integer, primary_key=True, nullable=False)
    seq = db.Column(db.Integer, primary_key=True, nullable=False)
    msg = db.Column(db.String, nullable=False)
    face = db.Column(db.Integer, nullable=False)


class Movies(db.Model):
    movie_id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String, nullable=False)
    length = db.Column(db.String(8), nullable=False)
    aspect = db.Column(db.Boolean, nullable=False)
    genre = db.Column(db.Integer, nullable=False)
    sp_page_id = db.Column(db.Integer, nullable=False)
    ds_dist = db.Column(db.Boolean, nullable=False)
    ds_mov_id = db.Column(db.Integer)
    staff = db.Column(db.Boolean, nullable=False)


class Categories(db.Model):
    category_id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String)


class CategoryMovies(db.Model):
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.category_id"),
        primary_key=True,
        nullable=False,
    )
    movie_id = db.Column(
        db.Integer,
        db.ForeignKey("movies.movie_id"),
        primary_key=True,
        nullable=False,
    )
