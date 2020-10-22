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
migrate = Migrate(app,db)
import models

with app.test_request_context():
    db.init_app(app)
    db.create_all()

login = LoginManager(app)


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
import url1.special.all

from url2 import assets, reginfo


from url3.pay import event_today, wall_metadata
from theunderground import admin
# Do not rely on any of this in production.
# For more information, please see conf/README.md.
if app.debug:

    @app.route("/conf/first.bin")
    def conf_first_bin():
        return send_from_directory("conf", "first.bin")

    @app.route("/url1/wall/<name>.img")
    def serve_images(name):
        return send_from_directory("assets/normal", name + ".img")

    @app.route("/url3/pay/wall/<name>.img")
    def serve_pay_images(name):
        return send_from_directory("assets/pay", name + ".img")

