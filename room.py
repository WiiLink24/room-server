from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from datetime import datetime, timezone
from datadog import statsd, api, initalize
import config
import gloom.srv.shopsdk
import rc24.utils.by.larsen.rc24.utilsbylarsen
import shopurl.shopbyzurgeg
import json
import ntplib
import pathlib
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = config.secret_key
login = LoginManager(app)
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
from url1.special import all, allbin, page
from url2 import reginfo, related, search
from url3.pay import category_header, event_today, wall_metadata
import theunderground.admin
if app.debug:
    @app.route("/conf/first.bin")
    def conf_first_bin():
        return send_from_directory("conf", "first.bin")
class GloomSDKTasks():
    def sender(thetoemail, filetosend, currentnoofpoints, pointsneeded, contenttype):
        currentpath = str(pathlib.Path(__file__).parent.absolute()) + str("/gloom/srv/")
        with open(str(currentpath) + str("./config.json"), "rb") as f:
            config = json.load(f)
        if config["production"] and config["send_logs"]:
            rc24.utils.by.larsen.rc24.utilsbylarsen.setup_log(config["sentry_url"], False)
        data = gloom.srv.shopsdk.send(thetoemail, filetosend, currentnoofpoints, pointsneeded, contenttype)
        data2 = GloomSDKUtils.split(gloom.srv.defs.padding, 4) #Finds the 24 pad strings which point to the remaining points
        data2 = GloomSDKUtils.filter(data2) #Filters the 24 pad strings out
        data3 = gloom.srv.defs.padding) * 3
        data4 = GloomSDKUtils.split(data3, 1) #Finds the 72 pad strings which points to the sendgrid result codes.
        data4 = GloomSDKUtils.filter(data4) #Filters the 72 pad strings out
        data5 = shopurl.shopbyzurgeg.test_remove_points(pointsneeded) #Hooks into zurgeg's points engine to asynchronously remove the points they used.
        if data5 == data2:
            msg = "EVERYTHING IS A-OK"
            rc24.utils.by.larsen.rc24.utilsbylarsen.log("SUCCESS MESSAGE: %s" % msg, "INFO")
        else:
            rc24.utils.by.larsen.rc24.utilsbylarsen.log("THREW EXCEPTION BECAUSE OF INTEGER DEFINED AS %s" % data5, "CRITICAL")
        options = {
            'api_key': config["datadog_api_key"],
            'app_key': config["datadog_app_key"]
        }
        initialize(**options)
        c = ntplib.NTPClient()
        response = c.request(config["datadog_ntp_server"], version=3) #Uses NTP to grab UTC timestamp, used in Datadog.
        response.offset
        currenttime = datetime.fromtimestamp(response.tx_time, timezone.utc)
        title = "6100m's DLC Bot Hook was ran!"
        text = 'Script was ran at: ' + currenttime + ' | UTC | @ TX ' 
        tags = ['version:1', 'application:python']
        api.Event.create(title=title, text=text, tags=tags)
        if config["production"] and config["send_stats"]:    
            statsd.increment("shopsdk.pointsremoved", pointsneeded)
        return data4
class GloomSDKUtils():
    def setup():
        gloom.srv.shopsdk.tasks.setup()
    def filter(offset):
        data = list(filter(None, offset)
        return data
    def split(offset0, offset1):
        data =data.rsplit(offset0, offset1)
        return data
