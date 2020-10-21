from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Ensure DB tables are created.
db = SQLAlchemy()
import models

with app.test_request_context():
    db.init_app(app)
    db.create_all()

# Import routes here.
from url1 import beacon, category_n, eula, event_today, mii, movie_metadata, paylink, wall_metadata
import url1.special.all

import url2.reginfo

from url3.pay import category_header, event_today, wall_metadata

# Do not rely on any of this in production.
# For more information, please see conf/README.md.
if app.debug:

    @app.route("/conf/first.bin")
    def conf_first_bin():
        return send_from_directory("conf", "first.bin")

    @app.route("/url1/wall/<name>.img")
    def serve_images(name):
        return send_from_directory("assets/normal-wall", name + ".img")

    @app.route("/url3/pay/wall/<name>.img")
    def serve_pay_images(name):
        return send_from_directory("assets/pay-wall", name + ".img")

    @app.route("/url1/intro/<name>.img")
    def serve_intro(name):
        return send_from_directory("assets/normal-intro", name + ".img")

    @app.route("/url3/pay/intro/<name>.img")
    def serve_pay_intro(name):
        return send_from_directory("assets/pay-intro", name + ".img")

    @app.route("/url1/list/category/img/<name>.img")
    def serve_category_images(name):
        return send_from_directory("assets/normal-category", name + ".img")

    @app.route("/url3/pay/list/category/img/<name>.img")
    def serve_pay_category_images(name):
        return send_from_directory("assets/pay-category", name + ".img")

    @app.route("/url1/movie/<unk>/<name>")
    def serve_movie_data(unk, name):
        return send_from_directory("assets/movies", name)


