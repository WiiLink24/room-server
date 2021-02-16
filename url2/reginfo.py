from room import app
from helpers import xml_node_name, current_date_and_time
from ... import timezone_module
response_data = timezone_module.gettime(request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
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
