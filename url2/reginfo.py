import zoneinfo
from datetime import datetime

from flask import request
from geoip2 import database
from geoip2.errors import AddressNotFoundError

import config
from helpers import xml_node_name, current_date_and_time
from room import app


if config.use_localized_time:
    maxmind_client = database.Reader(config.maxmind_db_location)


def get_user_timezone(request) -> zoneinfo.ZoneInfo:
    # We default to UTC.
    time_zone = "Etc/UTC"

    if config.use_localized_time:
        try:
            # Attempt to query the DB.
            possible_time = maxmind_client.city(
                ip_address=request.remote_addr
            ).location.time_zone

            # The location may not have a timezone.
            if possible_time:
                time_zone = possible_time
        except AddressNotFoundError:
            # We'll stay to UTC.
            pass

    return zoneinfo.ZoneInfo(time_zone)


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
