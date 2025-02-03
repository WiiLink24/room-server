from io import BytesIO

from flask import render_template, flash, url_for, redirect
from werkzeug import exceptions

from theunderground.forms import PosterForm
from theunderground.operations import manage_delete_item
from theunderground.admin import oidc
from asset_data import PosterAsset
from models import Posters, db
from room import app, s3
from url1.event_today import event_today
from flask_wtf.file import FileRequired
from theunderground.logging import log_action
import config


@app.route("/theunderground/posters")
@oidc.require_login
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
@oidc.require_login
def add_poster():
    form = PosterForm()
    form.poster.validators = [FileRequired()]

    if form.validate_on_submit():
        db_poster = Posters(
            msg=form.msg.data, movie_id=form.movie_id.data, title=form.title.data
        )

        db.session.add(db_poster)
        db.session.commit()
        if s3:
            event_xml = event_today()
            s3.upload_fileobj(
                BytesIO(event_xml), config.r2_bucket_name, "event/today.xml"
            )

        if form.poster:
            # Now upload poster
            PosterAsset(db_poster.poster_id, False).encode(form.poster)
        else:
            flash("Error uploading asset!")

        log_action(f"Poster {db_poster.poster_id} was added")
        return redirect(url_for("list_posters"))

    return render_template("poster_action.html", form=form, action="Upload")


@app.route("/theunderground/movies/poster/<poster_id>/edit", methods=["GET", "POST"])
@oidc.require_login
def edit_poster(poster_id):
    form = PosterForm()

    poster = Posters.query.filter_by(poster_id=poster_id).first()
    if not poster:
        return exceptions.NotFound()

    if form.validate_on_submit():
        poster.title = form.title.data
        poster.msg = form.msg.data
        poster.movie_id = form.movie_id.data

        if form.poster.data:
            # Now upload poster
            PosterAsset(poster_id, False).encode(form.poster)

        # Commit before uploading to s3
        db.session.commit()
        if s3:
            event_xml = event_today()
            s3.upload_fileobj(
                BytesIO(event_xml), config.r2_bucket_name, "event/today.xml"
            )

        log_action(f"Poster {poster_id} was edited")
        return redirect(url_for("list_posters"))
    else:
        form.title.data = poster.title
        form.msg.data = poster.msg
        form.movie_id.data = poster.movie_id

    return render_template(
        "poster_action.html", form=form, poster_id=poster_id, action="Edit"
    )


@app.route("/theunderground/posters/<poster>/remove", methods=["GET", "POST"])
@oidc.require_login
def remove_poster(poster: int):
    def drop_poster():
        db.session.delete(Posters.query.filter_by(poster_id=poster).first())
        db.session.commit()

        PosterAsset(poster, False).delete()

        log_action(f"Poster {poster} was removed")
        return redirect(url_for("list_posters"))

    return manage_delete_item(poster, "poster", drop_poster)


@app.route("/theunderground/posters/<poster>/thumbnail.jpg")
@oidc.require_login
def get_poster(poster):
    if s3:
        return redirect(f"{config.url1_cdn_url}/wall/{poster}.img")

    return PosterAsset(poster, is_theatre=False).send_file()
