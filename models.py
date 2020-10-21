from room import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from room import login
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class ConciergeMii(db.Model):
     mii_id = db.Column(db.Integer, primary_key=True, unique=True)
     title = db.Column(db.String(6))
     color1 = db.Column(db.String(6))
     color2 = db.Column(db.String(6))
     message1 = db.Column(db.String(100))
     message2 = db.Column(db.String(100))
     message3 = db.Column(db.String(100))
     message4 = db.Column(db.String(100))
     message5 = db.Column(db.String(100))
     message6 = db.Column(db.String(100))
     message7 = db.Column(db.String(100))
     updated = db.Column(db.String(17))
     movieid = db.Column(db.String(1))
class User(db.Model, UserMixin):
    # Used to login to the Admin Panel
    username = db.Column(db.String(100),primary_key=True)
    password_hash = db.Column(db.String(9999999))
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
    type = db.Column(db.Integer)
    aspect = db.Column(db.Boolean)
