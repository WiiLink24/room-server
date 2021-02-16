from room import app
from datetime import datetime 
from pytz import timezone
from helpers import xml_node_name, current_date_and_time
from urllib import urlopen
from config import ipinfo_token
from json import load
from flask import request
requested_data = str(request.environ.get('HTTP_X_REAL_IP', request.remote_addr))
json_data = json.load(urlopen('http://ipinfo.io/{}/json?token='.format(requested_data) + ipinfo_token))
response_data = datetime.now(pytz.timezone(str(json_data['timezone']))).strftime("%Y-%m-%dT%H:%M:%S")) 
@app.route("/url2/reginfo.cgi")
@xml_node_name("RegionInfo")
def reginfo_cgi():
    return {
        "sdt": str(response_data),
        "cdt": str(response_data),
        "limited": "0",
    }
@app.route("/url1/conf/datetime.xml")
@xml_node_name("DateTime")
def datetime_xml():
    # DateTime is roughly equivalent to RegInfo as seen in v1025.
    return {"upddt": str(response_data)}
