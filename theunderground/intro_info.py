from io import BytesIO


from flask import (
    render_template,
    request,
    flash,
    redirect,
    url_for,
    send_from_directory,
)
from asset_data import TVScreenAsset
from room import app, s3
from models import IntroInfo, db, ContentTypes
from theunderground.forms import IntroInfoForm
from theunderground.mobiclip import validate_mobiclip
from theunderground.operations import manage_delete_item
from theunderground.admin import oidc
from werkzeug import exceptions
from url1.event_today import event_today
from theunderground.logging import log_action

import config


@app.route("/theunderground/intro_info")
@oidc.require_login
def list_intro_info():
    page_num = request.args.get("page", default=1, type=int)

    infos = IntroInfo.query.order_by(IntroInfo.cnt_id.asc()).paginate(
        page=page_num, per_page=15, error_out=False
    )

    return render_template(
        "intro_info_list.html", infos=infos, type_length=infos.total, type_max_count=30
    )


@app.route("/theunderground/intro_info/add", methods=["GET", "POST"])
@oidc.require_login
def add_intro_info():
    form = IntroInfoForm()

    if form.is_submitted():
        intro_db = IntroInfo(cnt_type=form.cnt_type.data, link_type=form.link_type.data)

        if form.cat_name:
            intro_db.cat_name = form.cat_name.data

        if form.link_id:
            intro_db.link_id = form.link_id.data

        # Now push to database.
        db.session.add(intro_db)
        db.session.commit()

        # Wii Room requires video content id's to be 16 characters long.
        if intro_db.cnt_type == ContentTypes.Video:
            intro_db.cnt_id = int(str(intro_db.cnt_id).ljust(16, "0"))
            db.session.add(intro_db)
            db.session.commit()

        update_intro_info_on_s3()

        # Now encode image/video.
        if form.asset:
            if intro_db.cnt_type == ContentTypes.Image:
                TVScreenAsset(intro_db.cnt_id, is_theatre=False, is_movie=False).encode(
                    form.asset
                )
            else:
                video = form.asset.data.read()
                if validate_mobiclip(video):
                    TVScreenAsset(
                        intro_db.cnt_id, is_theatre=False, is_movie=True
                    ).upload_movie(video)
                else:
                    flash("Invalid movie!")
        else:
            flash("Error uploading asset!")

        log_action(f"Intro Info {intro_db.cnt_id} was added")
        return redirect(url_for("list_intro_info"))

    return render_template("intro_info_add.html", form=form)


@app.route("/theunderground/intro_info/<id>/remove", methods=["GET", "POST"])
@oidc.require_login
def remove_intro_info(id):
    def drop_intro_info():
        db.session.delete(current_info)
        db.session.commit()

        log_action(f"Intro Info {id} was removed")
        return redirect(url_for("list_intro_info"))

    current_info = IntroInfo.query.filter(IntroInfo.cnt_id == id).first()
    if not current_info:
        return exceptions.NotFound()

    return manage_delete_item(id, "info intro", drop_intro_info)


def update_intro_info_on_s3():
    # Regenerate event/today.xml on s3 if needed
    if s3:
        event_xml = event_today()
        s3.upload_fileobj(BytesIO(event_xml), config.r2_bucket_name, "event/today.xml")


@app.route("/theunderground/intro_info/<cnt_id>/thumbnail.jpg")
@oidc.require_login
def get_info_image(cnt_id):
    if s3:
        return redirect(f"{config.url1_cdn_url}/normal-intro/{cnt_id}-1.img")

    return send_from_directory("assets/normal-intro/", f"{cnt_id}-1.img")
