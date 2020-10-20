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
import url2.reginfo
import url1.beacon.any
import url1.conf.eula
import url1.conf2.paylink
import url1.event.today


# Do not rely on this in production.
# For more information, please see conf/README.md.
if app.debug:

    @app.route("/conf/first.bin")
    def conf_first_bin():
        return send_from_directory("conf", "first.bin")
