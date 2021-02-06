from flask import render_template, redirect, url_for, flash
from flask_login import login_required

from models import ParadeMiis
from room import app, db
from theunderground.encodemii import parade_encode
from theunderground.forms import ParadeForm, KillMii


@app.route("/theunderground/parade")
@login_required
def list_parade():
    parade_miis = ParadeMiis.query.order_by(ParadeMiis.mii_id.asc()).all()
    return render_template("parade_list.html", miis=parade_miis)


@app.route("/theunderground/parade/<mii_id>", methods=["GET", "POST"])
@login_required
def edit_parade(mii_id):
    form = ParadeForm()
    if form.validate_on_submit():
        # Encode an image to the appropriate size.
        inserted_image = parade_encode(form.image.data.read())

        q = ParadeMiis.query.filter_by(mii_id=mii_id)
        if list(q):
            mii = q.first()
            mii.logo_bin = inserted_image
            mii.news = form.news.data
        else:
            mii = ParadeMiis(
                mii_id=mii_id,
                logo_id="g1234",
                logo_bin=inserted_image,
                news=form.news.data,
                level=1,
            )

        db.session.add(mii)
        db.session.commit()
        return redirect(url_for("list_parade"))

    return render_template("parade_edit.html", form=form)


@app.route("/theunderground/parade/<mii_id>/remove", methods=["GET", "POST"])
@login_required
def remove_parade(mii_id):
    form = KillMii()
    if form.validate_on_submit():
        # While this is easily circumvented, we need the user to pay attention.
        if form.given_mii_id.data == mii_id:
            db.session.delete(ParadeMiis.query.filter_by(mii_id=mii_id).first())
            db.session.commit()
            return redirect(url_for("list_parade"))
        else:
            flash("Incorrect Mii ID!")
    return render_template("parade_delete.html", form=form, mii_id=mii_id)


@app.route("/theunderground/parade/<mii_id>/banner.jpg")
@login_required
def get_parade_banner(mii_id):
    parade_mii = ParadeMiis.query.filter_by(mii_id=mii_id).first()
    return parade_mii.logo_bin
