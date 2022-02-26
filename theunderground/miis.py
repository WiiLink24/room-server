import crc16
from flask import render_template, redirect, flash, url_for
from flask_login import login_required

from models import MiiData, db
from room import app
from theunderground.forms import MiiUploadForm


@app.route("/theunderground/miis")
@login_required
def list_miis():
    miis = MiiData.query.order_by(MiiData.mii_id).all()

    return render_template("mii_list.html", miis=miis, type_length=len(miis))


@app.route("/theunderground/miis/add", methods=["GET", "POST"])
@login_required
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
                return redirect(url_for("list_miis"))
            else:
                flash("Invalid Mii uploaded")
        else:
            flash("Error uploading Mii")

    return render_template("mii_add.html", form=form)
