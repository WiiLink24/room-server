from room import app


@app.route("/url2/smp.cgi", methods=["POST"])
def handle_delivery():
    """This is 100% not apart of url2 however I don't know where else to put this"""
    return "OK"
