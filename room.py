from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from sentry_sdk.integrations.flask import FlaskIntegration
from sqlalchemy_searchable import make_searchable

from models import db, login

import config
import sentry_sdk

# Initialize Sentry
if config.use_sentry:
    sentry_sdk.init(
        dsn=config.sentry_dsn,
        integrations=[FlaskIntegration()],
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,
    )

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = config.secret_key

# Ensure DB tables are created.
# Importing models must occur after the DB is instantiated.
# It must not initialize around an app so that we can create
# models automatically within a test context.
db.init_app(app)
make_searchable(db.metadata)

# Ensure the DB is able to determine migration needs.
migrate = Migrate(app, db)
login.init_app(app)


with app.app_context():
    # Ensure our database is present.
    db.create_all()


db.configure_mappers()

# Import routes here.
import first

import url1
import url2
import url3
import theunderground
