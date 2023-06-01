from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from flask import render_template, flash, url_for, redirect
from flask_login import login_required
from theunderground.forms import PayPosterForm
from theunderground.operations import manage_delete_item
from asset_data import PosterAsset, PayMovieAsset
from models import PayPosters, db
from room import app

import os

PAY_POSTER_KEY = b"\x5a\xb3\x62\xaa\x57\xdb\xb1\xdc\x16\x84\x9e\x3e\x2d\x1c\xf2\xff"
PAY_POSTER_IV = b"\x09\xd4\xfb\xfc\xa4\x00\xc1\x3d\xa0\x1c\xbf\x83\x5d\xa3\x24\x3a"


@app.route("/theunderground/payposters")
@login_required
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
@login_required
def add_pay_poster():
    form = PayPosterForm()

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

    return render_template("pay_poster_add.html", form=form)


@app.route("/theunderground/payposters/<poster>/remove", methods=["GET", "POST"])
@login_required
def remove_pay_poster(poster):
    def drop_pay_poster():
        os.unlink(PosterAsset(poster, is_theatre=True).asset_path())
        db.session.delete(PayPosters.query.filter_by(poster_id=poster).first())
        db.session.commit()

        return redirect(url_for("list_pay_posters"))

    return manage_delete_item(poster, "pay poster", drop_pay_poster)


@app.route("/theunderground/payposters/<poster>/thumbnail.jpg")
@login_required
def get_pay_poster(poster):
    return PosterAsset(poster, is_theatre=True).send_file()
