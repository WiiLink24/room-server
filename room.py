from elasticsearch import Elasticsearch
from flask import Flask, session, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from werkzeug.middleware.proxy_fix import ProxyFix

import config

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=2)
app.config["SQLALCHEMY_DATABASE_URI"] = config.db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = config.secret_key

login = LoginManager()

es = Elasticsearch(
    config.elasticsearch_url,
    http_auth=(config.elasticsearch_user, config.elasticsearch_pass),
)

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

# Import routes here.

import first

import url1
import url2
import url3
import theunderground
