from room import app
from helpers import xml_node_name


@app.route("/url1/conf/eula.xml")
@xml_node_name("LicenseAgree")
def conf_eula():
    return {
        "agree": "The WiiLink24 team is not responsible for bricked devices, dead SD cards, or thermonuclear war."
    }
