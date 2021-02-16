from flask.request import args
from room import app
from urllib import urlopen
def gettime(ip):
  return str(urllib.urlopen('http://api.hostip.info/get_html.php?ip=<ip>').read())
@app.route("/api/obtaintime", methods=["GET"])
 gettime(request.args["ipaddr"])
