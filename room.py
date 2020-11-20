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
import roomutils
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
        #Find the 24 pad strings which point to the remaining points
        data2 = roomutils.GloomSDKUtils.split(gloom.srv.defs.padding, 4) 
        #Filter the 24 pad strings out
        data2 = roomutils.GloomSDKUtils.filter(data2) 
        #Triple padding for sendgrid result code detection
        data3 = roomutils.GloomSDKUtils.triple(gloom.srv.defs.padding)
        #Find the 72 pad strings which points to the sendgrid result codes.
        data4 = roomutils.GloomSDKUtils.split(data3, 1) 
        #Filter the 72 pad strings out
        data4 = roomutils.GloomSDKUtils.filter(data4)
        #Hook into zurgeg's points engine to asynchronously remove the points they used.
        data5 = roomutils.GloomSDKUtils.pointremover(pointsneeded)
        if data5 == data2:
            roomutils.GloomSDKUtils.loggertool("SUCCESS MESSAGE: ", GloomSDKUtils.msgtool(), "INFO")
        else:
            roomutils.GloomSDKUtils.loggertool("THREW EXCEPTION BECAUSE OF INTEGER DEFINED AS: ", data5, "CRITICAL")
        options = {
            'api_key': config["datadog_api_key"],
            'app_key': config["datadog_app_key"]
        }
        initialize(**options)
        c = ntplib.NTPClient()
        #Uses NTP to grab UTC timestamp, used in Datadog.
        response = c.request(config["datadog_ntp_server"], version=3) 
        response.offset
        currenttime = datetime.fromtimestamp(response.tx_time, timezone.utc)
        title = "6100m's DLC Bot Hook was ran!"
        text = 'Script was ran at: ' + currenttime + ' | UTC | @ TX ' 
        tags = ['version:1', 'application:python']
        api.Event.create(title=title, text=text, tags=tags)
        if config["production"] and config["send_stats"]:    
            statsd.increment("shopsdk.pointsremoved", pointsneeded)
        return data4
