from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import config
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Ensure DB tables are created.
db = SQLAlchemy()

with app.test_request_context():
    db.init_app(app)
    db.create_all()
login = LoginManager(app)
# Import routes here.
import theunderground.admin
from url1 import beacon, eula, event_today, paylink, wall_metadata
import url1.special.all

import url2.reginfo

from url3.pay import event_today, wall_metadata

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
