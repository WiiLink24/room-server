from room import app
from flask import jsonify, request
from helpers import xml_node_name, current_date_and_time
import config
from geoip2.webservice import Client
from pytz import timezone
from datetime import datetime


class DummyMMResponse:
    def __init__(self, **kwargs):
        self.time_zone = "Etc/UTC"


class DummyMMClient:
    def __init__(*args, **kwargs):
        # Fake Maxmind client to always return UTC time
        pass

    def insights(*args, **kwargs):
        return DummyMMResponse()


if config.use_localized_time:
    client = Client(config.maxmind_account_id, config.maxmind_license_id)
else:
    client = DummyMMClient()


@app.route("/url2/reginfo.cgi")
@xml_node_name("RegionInfo")
def reginfo_cgi():
    timezone_data = client.insights(request.remote_addr).time_zone
    return {
        "sdt": current_date_and_time(),
        "cdt": datetime.now(timezone(timezone_data)),
        "limited": "0",
    }


@app.route("/url1/conf/datetime.xml")
@xml_node_name("DateTime")
def datetime_xml():
    # DateTime is roughly equivalent to RegInfo as seen in v1025.

    return {"upddt": current_date_and_time()}
