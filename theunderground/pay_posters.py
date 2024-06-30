from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from flask import render_template, flash, url_for, redirect
from werkzeug import exceptions

from theunderground.forms import PayPosterForm
from theunderground.operations import manage_delete_item
from theunderground.admin import oidc
from asset_data import PosterAsset, PayMovieAsset
from models import PayPosters, db
from room import app
from flask_wtf.file import FileRequired

import os

PAY_POSTER_KEY = b"\x5a\xb3\x62\xaa\x57\xdb\xb1\xdc\x16\x84\x9e\x3e\x2d\x1c\xf2\xff"
PAY_POSTER_IV = b"\x09\xd4\xfb\xfc\xa4\x00\xc1\x3d\xa0\x1c\xbf\x83\x5d\xa3\x24\x3a"


@app.route("/theunderground/payposters")
@oidc.require_login
def list_pay_posters():
    # Displays a table of posters with options to add and remove them
    posters = PayPosters.query.paginate()
    return render_template(
        "pay_poster_list.html",
        posters=posters,
        type_length=posters.total,
        # I mean not really, but we should never have this much ever
        type_max_count=2,
    )


@app.route("/theunderground/payposters/add", methods=["GET", "POST"])
@oidc.require_login
def add_pay_poster():
    form = PayPosterForm()

    # Add the file validators
    form.poster.validators = [FileRequired()]
    form.movie.validators = [FileRequired()]

    if form.validate_on_submit():
        db_poster = PayPosters(
            msg=form.msg.data, title=form.title.data, type=1, aspect=False
        )

        db.session.add(db_poster)
        db.session.commit()

        # Encrypt movie
        if form.movie:
            cipher = AES.new(PAY_POSTER_KEY, AES.MODE_CBC, iv=PAY_POSTER_IV)
            encrypted_movie = cipher.encrypt(
                pad(form.movie.data.read(), AES.block_size)
            )
            PayMovieAsset(db_poster.poster_id).upload_movie(encrypted_movie)
        else:
            flash("Error uploading movie!")
            return redirect(url_for("list_pay_posters"))

        if form.poster:
            # Now upload poster
            PosterAsset(db_poster.poster_id, True).encode(form.poster)
        else:
            flash("Error uploading poster!")
            return redirect(url_for("list_pay_posters"))

        return redirect(url_for("list_pay_posters"))

    return render_template("pay_poster_action.html", form=form, action="Upload")


@app.route("/theunderground/payposters/<poster_id>/edit", methods=["GET", "POST"])
@oidc.require_login
def edit_pay_poster(poster_id):
    form = PayPosterForm()

    poster = PayPosters.query.filter_by(poster_id=poster_id).first()
    if not poster:
        return exceptions.NotFound()

    if form.validate_on_submit():
        poster.msg = form.msg.data
        poster.title = form.title.data

        # Encrypt movie
        if form.movie.data:
            cipher = AES.new(PAY_POSTER_KEY, AES.MODE_CBC, iv=PAY_POSTER_IV)
            encrypted_movie = cipher.encrypt(
                pad(form.movie.data.read(), AES.block_size)
            )
            PayMovieAsset(poster.poster_id).upload_movie(encrypted_movie)

        if form.poster.data:
            # Now upload poster
            PosterAsset(poster.poster_id, True).encode(form.poster)

        db.session.commit()
        return redirect(url_for("list_pay_posters"))
    else:
        form.msg.data = poster.msg
        form.title.data = poster.title

    return render_template(
        "pay_poster_action.html", form=form, action="Edit", poster_id=poster_id
    )


@app.route("/theunderground/payposters/<poster>/remove", methods=["GET", "POST"])
@oidc.require_login
def remove_pay_poster(poster):
    def drop_pay_poster():
        os.unlink(PosterAsset(poster, is_theatre=True).asset_path())
        db.session.delete(PayPosters.query.filter_by(poster_id=poster).first())
        db.session.commit()

        return redirect(url_for("list_pay_posters"))

    return manage_delete_item(poster, "pay poster", drop_pay_poster)


@app.route("/theunderground/payposters/<poster>/thumbnail.jpg")
@oidc.require_login
def get_pay_poster(poster):
    return PosterAsset(poster, is_theatre=True).send_file()
