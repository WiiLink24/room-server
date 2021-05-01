from flask import render_template, url_for, redirect, flash
from flask_login import login_required

from models import ConciergeMiis, MiiMsgInfo, MiiData
from room import db, app
from theunderground.forms import ConciergeForm, KillMii


@app.route("/theunderground/concierge")
@login_required
def list_concierge():
    concierge_miis = (
        db.session.query(ConciergeMiis, MiiData)
        .filter(ConciergeMiis.mii_id == MiiData.mii_id)
        .all()
    )

    print(concierge_miis)

    return render_template(
        "concierge_list.html",
        miis=concierge_miis,
        type_length=len(concierge_miis),
        type_max_count=20,
    )


@app.route("/theunderground/concierge/<mii_id>", methods=["GET", "POST"])
@login_required
def edit_concierge(mii_id):
    form = ConciergeForm()
    if form.validate_on_submit():
        concierge_data = ConciergeMiis(
            mii_id=mii_id,
            clothes=1,  # TODO: Allow disabling of custom clothes
            action=1,  # TODO: Allow changing of whatever the heck "action" is
            prof=form.prof.data,  # TODO: Add this.
            movie_id=form.movieid.data,
            voice=False,  # The web console does not currently support this
        )
        # I would **assume** that Mii data is already in the console.
        # Which saves us space in the UI
        # The below will be very messy, enjoy!
        msg1 = MiiMsgInfo(mii_id=mii_id, type=1, seq=1, msg=form.message1.data, face=1)
        msg2 = MiiMsgInfo(mii_id=mii_id, type=2, seq=1, msg=form.message2.data, face=1)
        msg3 = MiiMsgInfo(mii_id=mii_id, type=3, seq=1, msg=form.message3.data, face=1)
        msg4 = MiiMsgInfo(mii_id=mii_id, type=4, seq=1, msg=form.message4.data, face=1)
        msg5 = MiiMsgInfo(mii_id=mii_id, type=5, seq=1, msg=form.message5.data, face=1)
        msg6 = MiiMsgInfo(mii_id=mii_id, type=6, seq=1, msg=form.message6.data, face=1)
        msg7 = MiiMsgInfo(mii_id=mii_id, type=7, seq=1, msg=form.message7.data, face=1)
        # Now to add all of them
        db.session.add(msg1)
        db.session.add(msg2)
        db.session.add(msg3)
        db.session.add(msg4)
        db.session.add(msg5)
        db.session.add(msg6)
        db.session.add(msg7)
        db.session.add(concierge_data)
        db.session.commit()
        return redirect(url_for("list_concierge"))

    return render_template("concierge_edit.html", form=form)


@app.route("/theunderground/concierge/<mii_id>/remove", methods=["GET", "POST"])
@login_required
def remove_concierge(mii_id):
    form = KillMii()
    if form.validate_on_submit():
        # While this is easily circumvented, we need the user to pay attention.
        if form.given_id.data == mii_id:
            db.session.delete(ConciergeMiis.query.filter_by(mii_id=mii_id).first())
            db.session.delete(MiiMsgInfo.query.filter_by(mii_id=mii_id).first())
            db.session.commit()
            return redirect(url_for("list_concierge"))
        else:
            flash("Incorrect Mii ID!")
    return render_template("concierge_delete.html", form=form, item_id=mii_id)
