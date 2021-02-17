from pytz import timezone
from helpers import xml_node_name
from urllib3 import urlopen
from json import load
from config.reginfo_data import ipinfo_token
from room.app import route
from datetime.datetime import now
from flask.request.environ import get
from flask.request import remote_addr


def getzone():
    return str(
        now(
            timezone(
                json_data=load(
                    urlopen(
                        str("http://ipinfo.io/%s/json?token=%s")
                        % get("HTTP_X_REAL_IP", remote_addr),
                        ipinfo_token,
                    )
                )["timezone"]
            )
        ).strftime("%Y-%m-%dT%H:%M:%S")
    )


@route("/url2/reginfo.cgi")
@xml_node_name("RegionInfo")
def reginfo_cgi():
    return {
        "sdt": getzone(),
        "cdt": getzone(),
        "limited": "0",
    }


@route("/url1/conf/datetime.xml")
@xml_node_name("DateTime")
def datetime_xml():
    # DateTime is roughly equivalent to RegInfo as seen in v1025.
    return {"upddt": getzone()}
