from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Ensure DB tables are created.
db = SQLAlchemy()

# Please keep this import here so that initialization can create new tables.
import models

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
import url1.special.all, url1.special.page, url1.movie.movieimages, url1.special.allbin

from url2 import assets, reginfo, related

from url3.pay import category_header, event_today, wall_metadata
