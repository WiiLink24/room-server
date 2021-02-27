from room import app
from helpers import xml_node_name, current_date_and_time


@app.route("/url2/reginfo.cgi")
@xml_node_name("RegionInfo")
def reginfo_cgi():
    return {
        "sdt": current_date_and_time(),
        "cdt": current_date_and_time(),
        "limited": "0",
    }


@app.route("/url1/conf/datetime.xml")
@xml_node_name("DateTime")
def datetime_xml():
    # DateTime is roughly equivalent to RegInfo as seen in v1025.

    return {"upddt": current_date_and_time()}
