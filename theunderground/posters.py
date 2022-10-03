from flask import render_template, flash, url_for, redirect
from flask_login import login_required
from theunderground.forms import PosterForm
from asset_data import PosterAsset
from models import Posters, db
from room import app


@app.route("/theunderground/posters")
@login_required
def list_posters():
    # Displays a table of posters with options to add and remove them
    posters = Posters.query.paginate()
    return render_template(
        "poster_list.html",
        posters=posters,
        type_length=posters.total,
        # I mean not really, but we should never have this much ever
        type_max_count=30,
    )


@app.route("/theunderground/movies/poster", methods=["GET", "POST"])
@login_required
def add_poster():
    form = PosterForm()

    if form.validate_on_submit():
        db_poster = Posters(
            msg=form.msg.data, movie_id=form.movie_id.data, title=form.title.data
        )

        db.session.add(db_poster)
        db.session.commit()

        if form.poster:
            # Now upload poster
            PosterAsset(db_poster.poster_id, False).encode(form.poster)
        else:
            flash("Error uploading asset!")

        return redirect(url_for("list_posters"))

    return render_template("poster_add.html", form=form)


@app.route("/theunderground/posters/<poster>/thumbnail.jpg")
@login_required
def get_poster(poster):
    return PosterAsset(poster, is_theatre=False).send_file()
