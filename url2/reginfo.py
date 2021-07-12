import zoneinfo
from datetime import datetime

from flask import request
from helpers import xml_node_name, current_date_and_time
from room import app


def get_user_timezone(request) -> zoneinfo.ZoneInfo:
    try:
        if "X-Time-Zone" in request.headers:
            time_zone = request.headers.get("X-Time-Zone")
            return zoneinfo.ZoneInfo(time_zone)
    except KeyError or zoneinfo.ZoneInfoNotFoundError:
        pass

    # We default to UTC.
    return zoneinfo.ZoneInfo("Etc/UTC")


@app.route("/url2/reginfo.cgi")
@xml_node_name("RegionInfo")
def reginfo_cgi():
    current_user_time = datetime.now(get_user_timezone(request))

    return {
        "sdt": current_date_and_time(),
        "cdt": current_user_time.strftime("%Y-%m-%dT%H:%M:%S"),
        "limited": "0",
    }


@app.route("/url1/conf/datetime.xml")
@xml_node_name("DateTime")
def datetime_xml():
    # DateTime is roughly equivalent to RegInfo as seen in v1025.

    return {"upddt": current_date_and_time()}
