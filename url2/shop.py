# This file isn't a part of url2, but there's not much of
# a better place to put serving a swf.
from flask import send_from_directory

from room import app

if app.debug:

    @app.route("/shop/<file>")
    def serve_shop(file):
        return send_from_directory("./assets/shop", file)
