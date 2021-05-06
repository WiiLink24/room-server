from ssl import create_default_context

from elasticsearch import Elasticsearch
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_bootstrap import Bootstrap
import config

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=2)
app.config["SQLALCHEMY_DATABASE_URI"] = config.db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = config.secret_key

# Elastic may need a custom root CA for communication.
es_context = create_default_context()
if config.elasticsearch_ca_path:
    es_context.load_verify_locations(cafile=config.elasticsearch_ca_path)

es = Elasticsearch(
    config.elasticsearch_url,
    http_auth=(config.elasticsearch_user, config.elasticsearch_pass),
    ssl_context=es_context,
)

# Ensure DB tables are created.
# Importing models must occur after the DB is instantiated.
# It must not initialize around an app so that we can create
# models automatically within a test context.
db = SQLAlchemy(app)

# Ensure the DB is able to determine migration needs.
migrate = Migrate(app, db)

# Allow authentication.
login = LoginManager(app)

# Various Bootstrap Things
bootstrap = Bootstrap(app)

# Ensure schema is available.
import models

# Import routes here.
import first

import url1
import url2
import url3
import theunderground
