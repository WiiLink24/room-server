from flask import Flask, send_from_directory

app = Flask(__name__)

# Import routes here.
import url2.reginfo
import url1.beacon.any
import url1.conf.eula
import url1.conf2.paylink
import url1.event.today


# Do not rely on this in production.
# For more information, please see conf/README.md.
if app.debug:

    @app.route("/conf/first.bin")
    def conf_first_bin():
        return send_from_directory("conf", "first.bin")
