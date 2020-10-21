from room import db


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


class Miis(db.Model):
    mii_id = db.Column(db.Integer, primary_key=True, unique=True)
    clothes = db.Column(db.Integer, nullable=False)
    color1 = db.Column(db.String(6), nullable=False)
    color2 = db.Column(db.String(6), nullable=False)
    action = db.Column(db.Integer, nullable=False)
    prof = db.Column(db.String(129), nullable=False)
    name = db.Column(db.String(10), nullable=False)
    movie_id = db.Column(db.Integer, nullable=False)


class MiiData(db.Model):
    mii_id = db.Column(db.Integer, db.ForeignKey("miis.mii_id"), primary_key=True)
    data = db.Column(db.LargeBinary(74), nullable=False)


class MiiMsgInfo(db.Model):
    # We make both the Mii's ID and message type unique, as to allow row
    # identification for SQLAlchemy.
    mii_id = db.Column(
        db.Integer, db.ForeignKey("miis.mii_id"), primary_key=True, nullable=False
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
    staff = db.Column(db.Boolean, nullable=False)
