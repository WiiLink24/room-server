from flask import render_template
from flask_login import login_required

from models import Posters
from room import app


@app.route("/theunderground/posters")
@login_required
def list_posters():
    # Displays a table of posters with options to add and remove them
    posters = Posters.query.all()
    return render_template("poster_list.html", posters=posters)
