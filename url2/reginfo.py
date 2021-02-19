from room import app
from flask import jsonify
from helpers import xml_node_name, current_date_and_time
import config
from pytz import timezone
from datetime import datetime

geolocate = pygeoip.GeoIP(config.geoip_database)


@app.route("/url2/reginfo.cgi")
@xml_node_name("RegionInfo")
def reginfo_cgi():
    geo_data = jsonify(geolocate.record_by_addr(ip_address))
    return {
        "sdt": current_date_and_time(),
        "cdt": datetime.now(geo_data["timezone"]),
        "limited": "0",
    }


@app.route("/url1/conf/datetime.xml")
@xml_node_name("DateTime")
def datetime_xml():
    # DateTime is roughly equivalent to RegInfo as seen in v1025.

    return {"upddt": current_date_and_time()}
