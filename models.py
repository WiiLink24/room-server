import enum

from sqlalchemy import func

from room import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from room import login
import sqlalchemy


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


from sqlalchemy.types import TypeDecorator
import json


class DictType(TypeDecorator):

    impl = sqlalchemy.Text()

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)

        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value


class RoomMenu(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    room_id = db.Column(db.Integer)
    data = db.Column(DictType)  # This is a dict with keys in it for that type.
    # TODO: Figure out a suitable UI, maybe even using Javascript?


class ParadeMiis(db.Model):
    # We need to be able to select by both the Mii's ID and the logo.
    mii_id = db.Column(db.Integer, db.ForeignKey("mii_data.mii_id"), primary_key=True)
    logo_id = db.Column(db.String(5), primary_key=True)
    logo_bin = db.Column(db.LargeBinary(8000))
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


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    msg = db.Column(db.String, nullable=False)


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
    voice = db.Column(db.Boolean, default=False, nullable=False)


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
    movie_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.category_id"),
        primary_key=True,
        nullable=False,
    )
    title = db.Column(db.String(48), nullable=False)
    length = db.Column(db.String(8), nullable=False)
    aspect = db.Column(db.Boolean, nullable=False)
    genre = db.Column(db.Integer, nullable=False)
    sp_page_id = db.Column(db.Integer, nullable=False)
    ds_mov_id = db.Column(db.Integer, nullable=True)
    staff = db.Column(db.Boolean, nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, server_default=func.now())


class PayMovies(db.Model):
    movie_id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    title = db.Column(db.String, nullable=False)
    length = db.Column(db.String(), nullable=False)
    note = db.Column(db.String(76), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    released = db.Column(db.String(10), nullable=False)
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("pay_categories.category_id"),
        primary_key=True,
        nullable=False,
    )
    date_added = db.Column(db.DateTime, nullable=False, server_default=func.now())


class PayCategories(db.Model):
    category_id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String)
    # Starts at 10, goes up by 1 each time
    genre_id = db.Column(db.Integer)


class PayCategoryHeaders(db.Model):
    title = db.Column(db.String, primary_key=True, unique=True)


class Categories(db.Model):
    category_id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String)


class RoomBGMTypes(enum.Enum):
    SOFT_GUITAR = 1
    NORMAL = 2
    FOLK = 3
    JAZZY = 4
    TRUMPET = 5
    CHIMES = 6
    WESTERN = 7
    HARP = 8

    @classmethod
    def choices(cls):
        return [(choice, choice.name) for choice in cls]

    @classmethod
    def coerce(cls, item):
        return cls(int(item)) if not isinstance(item, cls) else item

    def __str__(self):
        return str(self.value)


class RoomContentBGMTypes(enum.Enum):
    Sadness = 1
    Upbeat = 2
    Relaxing = 3
    Classical = 4
    Playful = 5
    Chill = 6
    Adventurous = 7
    Jolly = 8
    Happiness = 9
    Casino = 10
    Parade = 11
    Excitement = 12
    idk = 13

    @classmethod
    def choices(cls):
        return [(choice, choice.name) for choice in cls]

    @classmethod
    def coerce(cls, item):
        return cls(int(item)) if not isinstance(item, cls) else item

    def __str__(self):
        return str(self.value)


class Rooms(db.Model):
    room_id = db.Column(
        db.Integer, db.ForeignKey("mii_data.mii_id"), primary_key=True, nullable=False
    )
    bgm = db.Column(db.Enum(RoomBGMTypes))
    mascot = db.Column(db.Boolean)
    contact = db.Column(db.Boolean)
    intro_msg = db.Column(db.String)
    mii_msg = db.Column(db.String)
    # TODO: implement room type specific logic
    logo2_id = db.Column(db.String)
    contact_data = db.Column(db.String)


class EvaluateData(db.Model):
    # ID only exists so postgres doesn't get pissed that there isn't a private key
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    movie_id = db.Column(db.Integer)
    gender = db.Column(db.Integer)
    blood = db.Column(db.Integer)
    age = db.Column(db.Integer)
    vote = db.Column(db.Integer)


class PollData(db.Model):
    # ID only exists so postgres doesn't get pissed that there isn't a private key
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    poll_id = db.Column(db.Integer)
    wii_num = db.Column(db.BigInteger)
    choice = db.Column(db.Integer)
    age = db.Column(db.Integer)
    gender = db.Column(db.Integer)

