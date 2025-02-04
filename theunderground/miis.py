import crc16
from flask_wtf.file import FileRequired
from werkzeug import exceptions
from flask import render_template, redirect, flash, url_for


from models import MiiData, db
from room import app
from theunderground.forms import MiiUploadForm
from theunderground.admin import oidc
from theunderground.logging import log_action


@app.route("/theunderground/miis")
@oidc.require_login
def list_miis():
    miis = MiiData.query.order_by(MiiData.mii_id).all()

    return render_template("mii_list.html", miis=miis, type_length=len(miis))


@app.route("/theunderground/miis/<mii_id>/edit", methods=["GET", "POST"])
@oidc.require_login
def edit_mii(mii_id):
    form = MiiUploadForm()

    mii = MiiData.query.filter_by(mii_id=mii_id).first()
    if not mii:
        return exceptions.NotFound()

    if form.validate_on_submit():
        full_mii = None
        checksum = None
        real_data = None
        if form.mii.data:
            data = form.mii.data.read()
            mii_length = len(data)

            # An uploaded Mii can be with or without its checksum.
            # We'll insert one ourselves all the same.
            if mii_length == 74 or mii_length == 76:
                # If we do have a checksum, split it off.
                real_data = data[:74]
                checksum = crc16.crc16xmodem(real_data).to_bytes(
                    length=2, byteorder="big"
                )
            else:
                flash("Invalid Mii uploaded")

        if full_mii:
            full_mii = real_data + checksum
            mii.data = (full_mii,)

        mii.name = (form.name.data,)
        mii.color1 = (form.color1.data,)
        mii.color2 = (form.color2.data,)

        db.session.commit()

        log_action(f"Mii ID {mii_id} was edited")
        return redirect(url_for("list_miis"))
    else:
        form.name.data = mii.name
        form.color1.data = mii.color1
        form.color2.data = mii.color2
        form.mii.validators = [FileRequired()]

    return render_template("mii_action.html", form=form, action="Edit")


@app.route("/theunderground/miis/add", methods=["GET", "POST"])
@oidc.require_login
def add_mii():
    form = MiiUploadForm()
    if form.validate_on_submit():
        mii = form.mii.data
        if mii:
            data = mii.read()
            mii_length = len(data)

            # An uploaded Mii can be with or without its checksum.
            # We'll insert one ourselves all the same.
            if mii_length == 74 or mii_length == 76:
                # If we do have a checksum, split it off.
                real_data = data[:74]
                checksum = crc16.crc16xmodem(real_data).to_bytes(
                    length=2, byteorder="big"
                )

                # Insert this to the database.
                full_mii = real_data + checksum
                insert_row = MiiData(
                    data=full_mii,
                    name=form.name.data,
                    color1=form.color1.data,
                    color2=form.color2.data,
                )
                db.session.add(insert_row)
                db.session.commit()

                log_action(f"Mii ID {insert_row.mii_id} was added")
                return redirect(url_for("list_miis"))
            else:
                flash("Invalid Mii uploaded")
        else:
            flash("Error uploading Mii")

    return render_template("mii_action.html", form=form, action="Add")
