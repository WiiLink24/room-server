import boto3
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from botocore.client import Config
from flask_migrate import Migrate
from sentry_sdk.integrations.flask import FlaskIntegration
from sqlalchemy_searchable import make_searchable

from models import db
from pytz import utc


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
app.config["OIDC_CLIENT_SECRETS"] = config.oidc_client_secrets_json
app.config["OIDC_SCOPES"] = "openid profile"

# Ensure DB tables are created.
# Importing models must occur after the DB is instantiated.
# It must not initialize around an app so that we can create
# models automatically within a test context.
db.init_app(app)
make_searchable(db.metadata)

# Ensure the DB is able to determine migration needs.
migrate = Migrate(app, db)

with app.app_context():
    # Ensure our database is present.
    db.create_all()


db.configure_mappers()

s3 = None
if config.use_s3:
    # Start the S3 client
    s3 = boto3.client(
        "s3",
        endpoint_url=config.s3_connection_url,
        aws_access_key_id=config.s3_access_key_id,
        aws_secret_access_key=config.s3_secret_access_key,
        config=Config(signature_version="s3v4"),
        region_name="us-east-1",
    )

    # Finally, start the popular list scheduler.
    from url1.popular_all import generate_all_popular

    scheduler = BackgroundScheduler()
    scheduler.add_job(generate_all_popular, "cron", hour=0, minute=0, timezone=utc)
    scheduler.start()

# Import routes here.
import first

import url1
import url2
import url3
import theunderground
