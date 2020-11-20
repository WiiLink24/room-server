from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import datetime
import datadog
import config as roomconf
import gloom.srv.shopsdk
import json
import ntplib
import pathlib
import roomutils
app = Flask(__name__)
g = gloom.srv.shopsdk
f = roomutils.GloomSDKUtils.filter
l = roomutils.GloomSDKUtils.loggertool
s = roomutils.GloomSDKUtils.split
app.config["SQLALCHEMY_DATABASE_URI"] = roomconf.db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = roomconf.secret_key
login = LoginManager(app)
# Ensure DB tables are created
# Importing models must occur after the DB is instantiated
# It must not initialize around an app so that we can create models automatically within a test context
db = SQLAlchemy()
padding=gloom.srv.defs.padding
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
    def sender(toemail, file, currentpoints, pointsneeded, int(num), mime):
        path=str(pathlib.Path(__file__).parent.absolute()) + "/gloom/srv/"
        with open(path + "./config.json", "rb") as f:
            conf=json.load(f)
        if conf["production"] and conf["send_logs"]:
           roomutils.GloomSDKUtils.setuptool(conf["sentry_url"])
        data = g.send(toemail, file, currentpoints, pointsneeded, int(num), mime)
        #Find 24 pad strings that point to spent points.
        data2 = s(padding, 4) 
        #Filter out 24 pad strings.
        data2 = f(data2) 
        #Triple the padding for locating sendgrid response codes.
        data3 = r.GloomSDKUtils.triple(padding)
        #Find 72 pad strings which point to sendgrid response codes.
        data4 = s(data3, 1)
        #Filter out 72 pad strings.
        data4 = f(data4)
        #Hooks into zurgeg's points engine to remove spent points.
        data5 = roomutils.GloomSDKUtils.pointremover(pointsneeded)
        if data5 == data2:
            l("SUCCESS MESSAGE: ", GloomSDKUtils.msgtool(), "INFO")
        else:
            l("THREW EXCEPTION BECAUSE OF INTEGER DEFINED AS: ", data5, "CRITICAL")
            raise ExceptionError
        options = {
            'api_key': conf["datadog_api_key"],
            'app_key': conf["datadog_app_key"]
        }
        datadog.initialize(**options)
        c = ntplib.NTPClient()
        #Use NTP to get UTC time for Datadog.
        response = c.request(conf["datadog_ntp_server"], version=3) 
        response.offset
        currenttime = datetime.fromtimestamp(response.tx_time, timezone.utc)
        title = "6100m's DLC Bot Hook was ran!"
        text = 'Script was ran at: ' + currenttime + ' | UTC | @ TX ' 
        tags = ['version:1', 'application:python']
        datadog.api.Event.create(title=title, text=text, tags=tags)
        if conf["production] and conf["send_stats"]:    
            datadog.statsd.increment("shopsdk.pointsremoved", pointsneeded)
        return data4
