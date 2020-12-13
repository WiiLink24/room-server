import os

from flask import send_from_directory

from room import app
from helpers import xml_node_name

eula_text = open("./conf/eula.txt", "r").read()


@app.route("/url1/conf/eula.xml")
@xml_node_name("LicenseAgree")
def conf_eula():
    return {"agree": eula_text}


if app.debug:

    @app.route("/url1/conf/brtest-H.mov")
    @app.route("/url1/conf/brtest-L.mov")
    def conf_sample_movie():
        return send_from_directory("assets/conf", "brtest-H.mo")
