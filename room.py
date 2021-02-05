from elasticsearch import Elasticsearch
from flask import Flask, session, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from werkzeug import exceptions

import config

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = config.secret_key

login = LoginManager()

es = Elasticsearch(config.elasticsearch_url)

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

    login.init_app(app)


# Required to allow version detection.
from helpers import determine_version

# Import routes here.
import first

from url1 import (
    beacon,
    category_n,
    category_search,
    eula,
    event_today,
    mii,
    movie_metadata,
    new,
    paylink,
    popular_all,
    popular_n,
    wall_metadata,
)
from url1.special import all, allbin, page

from url2 import reginfo, related, search

from url3.pay import category, category_header, event_today, wall_metadata

import theunderground
