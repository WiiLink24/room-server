from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import config

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = config.secret_key
# Ensure DB tables are created.

db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)
login = LoginManager(app)
import models

db = SQLAlchemy()

with app.test_request_context():
    db.init_app(app)
    db.create_all()


# Import routes here.
from url1 import (
    allbin,
    beacon,
    category_n,
    eula,
    event_today,
    mii,
    movie_metadata,
    paylink,
    wall_metadata,
)
import url1.special.all, url1.special.page

from url2 import reginfo, related

from url3.pay import category_header, event_today, wall_metadata
from theunderground import admin

if app.debug:

    @app.route("/conf/first.bin")
    def conf_first_bin():
        return send_from_directory("conf", "first.bin")
