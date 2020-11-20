from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
import datetime as t
import datadog as d
import config as roomconf
import gloom.srv.shopsdk
import json as j
import ntplib as n
import pathlib as p
import roomutils as r
app = Flask(__name__)
g = gloom.srv.shopsdk
f = r.GloomSDKUtils.filter
l = r.GloomSDKUtils.loggertool
s = r.GloomSDKUtils.split
app.config["SQLALCHEMY_DATABASE_URI"] = roomconf.db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = roomconf.secret_key
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
        path = str(p.Path(__file__).parent.absolute()) + str("/gloom/srv/")
        with open(str(path) + str("./config.json"), "rb") as f:
            config = j.load(f)
        if config["production"] and config["send_logs"]:
           r.GloomSDKUtils.setuptool(config["sentry_url"])
        data = g.send(thetoemail, filetosend, currentnoofpoints, pointsneeded, contenttype)
        #Find the 24 pad strings which point to used points
        data2 = s(gloom.srv.defs.padding, 4) 
        #Filter the 24 pad strings out
        data2 = f(data2) 
        #3x padding for sendgrid result code locating
        data3 = r.GloomSDKUtils.triple(gloom.srv.defs.padding)
        #Find the 72 pad strings which point to sendgrid result codes.
        data4 = s(data3, 1) 
        #Filter the 72 pad strings out
        data4 = f(data4)
        #Hook into zurgeg's points engine to remove the used points.
        data5 = r.GloomSDKUtils.pointremover(pointsneeded)
        if data5 == data2:
            l("SUCCESS MESSAGE: ", GloomSDKUtils.msgtool(), "INFO")
        else:
            l("THREW EXCEPTION BECAUSE OF INTEGER DEFINED AS: ", data5, "CRITICAL")
        options = {
            'api_key': config["datadog_api_key"],
            'app_key': config["datadog_app_key"]
        }
        d.initialize(**options)
        c = n.NTPClient()
        #Uses NTP to grab UTC time for Datadog.
        response = c.request(config["datadog_ntp_server"], version=3) 
        response.offset
        currenttime = t.fromtimestamp(response.tx_time, timezone.utc)
        title = "6100m's DLC Bot Hook was ran!"
        txt = 'Script was ran at: ' + currenttime + ' | UTC | @ TX' 
        tag = ['version:1', 'application:python']
        d.api.Event.create(title=title, text=txt, tags=tag)
        if config["production"] and config["send_stats"]:    
            d.statsd.increment("shopsdk.pointsremoved", pointsneeded)
        return data4
