from io import BytesIO

from flask import render_template, flash, url_for, redirect

from theunderground.forms import PosterForm
from theunderground.operations import manage_delete_item
from theunderground.admin import oidc
from asset_data import PosterAsset
from models import Posters, db
from room import app, s3
from url1.event_today import event_today
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

        return redirect(url_for("list_posters"))

    return render_template("poster_add.html", form=form)


@app.route("/theunderground/posters/<poster>/remove", methods=["GET", "POST"])
@oidc.require_login
def remove_poster(poster: int):
    def drop_poster():
        db.session.delete(Posters.query.filter_by(poster_id=poster).first())
        db.session.commit()

        PosterAsset(poster, False).delete()

        return redirect(url_for("list_posters"))

    return manage_delete_item(poster, "poster", drop_poster)


@app.route("/theunderground/posters/<poster>/thumbnail.jpg")
@oidc.require_login
def get_poster(poster):
    if s3:
        return redirect(f"{config.url1_cdn_url}/wall/{poster}.img")

    return PosterAsset(poster, is_theatre=False).send_file()
