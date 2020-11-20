#Modified version to serve as a submodule so that way a circular dependency error doesn't happen.
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import config
import gloom.srv.shopsdk
import rc24.utils.by.larsen.rc24.utilsbylarsen
import shopurl.shopbyzurgeg
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = config.secret_key
login = LoginManager(app)
# Ensure DB tables are created.
# Importing models must occur after the DB is instantiated.
# It must not initialize around an app so that we can create
# models automatically within a test context.
db = SQLAlchemy()
import models
# Ensure the DB is able to determine migration needs.
migrate = Migrate(app, db, compare_type=True)
with app.test_request_context():
    db.init_app(app)
    db.create_all()
# Import routes here.
from url1 import (
    beacon,
    category_n,
    eula,
    event_today,
    mii,
    movie_metadata,
    paylink,
    wall_metadata,
)
from url1.special import all, allbin, page
from url2 import reginfo, related, search
from url3.pay import category_header, event_today, wall_metadata
import theunderground.admin
class GloomSDKUtils():
    def setup():
        data = gloom.srv.shopsdk.tasks.setup()
        return data
    def filter(offset):
        data = list(filter(None, offset)
        return data
    def split(offset0, offset1):
        data = data.rsplit(offset0, offset1)
        return data
    def triple(string):
        data = string * 3
        return data
    def loggertool(offset0, offset1, offset2):
        rc24.utils.by.larsen.rc24.utilsbylarsen.log(offset0 % offset1, offset2)
        data = msgtool()
        return data
    def msgtool():
        data = "EVERYTHING A-OK"
        return data
    def pointremover(pointsneeded):
        shopurl.shopbyzurgeg.test_remove_points(pointsneeded)
        return pointsneeded
