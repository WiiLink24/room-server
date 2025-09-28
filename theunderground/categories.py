import os
import config

from flask import redirect, render_template, request, url_for

from flask_wtf.file import FileRequired
from werkzeug import exceptions
from asset_data import NormalCategoryAsset
from models import Categories, db
from room import app, s3
from theunderground.forms import CategoryForm
from theunderground.operations import manage_delete_item
from theunderground.admin import oidc
from theunderground.mobiclip import get_room_list
from theunderground.logging import log_action


@app.route("/theunderground/categories")
@oidc.require_login
def list_categories():
    page_num = request.args.get("page", default=1, type=int)

    categories = Categories.query.order_by(Categories.category_id.asc()).paginate(
        page=page_num, per_page=15, error_out=False
    )

    unlisted_categories = Categories.query.filter(Categories.unlisted == True).all()

    return render_template(
        "category_list.html",
        categories=categories,
        type_length=categories.total - len(unlisted_categories),
        type_max_count=64,
    )


@app.route("/theunderground/movies/<category>/listed")
@oidc.require_login
def toggle_category_listed(category):
    category = Categories.query.filter_by(category_id=category).first()
    category.unlisted = not category.unlisted
    db.session.commit()
    return redirect(url_for("list_categories"))


@app.route("/theunderground/categories/add", methods=["GET", "POST"])
@oidc.require_login
def add_category():
    form = CategoryForm()
    form.room.choices = get_room_list()
    # As we're adding, ensure a file is required.
    form.thumbnail.validators = [FileRequired()]

    if form.validate_on_submit():
        new_category = Categories(
            name=form.category_name.data, sp_page_id=form.room.data
        )

        # Add to retrieve the category ID.
        db.session.add(new_category)
        db.session.commit()

        # With this ID, write the thumbnail.
        NormalCategoryAsset(new_category.category_id).encode(form.thumbnail)

        log_action(f"Category {new_category.category_id} added")
        return redirect(url_for("list_categories"))

    return render_template("category_action.html", form=form, action="Add")


@app.route("/theunderground/categories/<category>/edit", methods=["GET", "POST"])
@oidc.require_login
def edit_category(category):
    form = CategoryForm()
    form.submit.label.text = "Edit"
    form.room.choices = get_room_list()

    # Populate data
    current_category = Categories.query.filter(
        Categories.category_id == category
    ).first()
    if not current_category:
        return exceptions.NotFound()

    if form.validate_on_submit():
        current_category.name = form.category_name.data
        current_category.sp_page_id = form.room.data
        db.session.commit()

        # Check if we have a new thumbnail.
        if form.thumbnail.data:
            NormalCategoryAsset(current_category.category_id).encode(form.thumbnail)

        log_action(f"Category {current_category.category_id} edited")
        return redirect(url_for("list_categories"))
    else:
        # Populate the current name.
        # category_action.html below will populate the current thumbnail.
        form.category_name.data = current_category.name

    return render_template(
        "category_action.html", category=current_category, form=form, action="Edit"
    )


@app.route("/theunderground/categories/<category>/remove", methods=["GET", "POST"])
@oidc.require_login
def remove_category(category):
    def drop_category():
        db.session.delete(current_category)
        db.session.commit()
        NormalCategoryAsset(category).delete()

        log_action(f"Category {category} removed")
        return redirect(url_for("list_categories"))

    current_category = Categories.query.filter(
        Categories.category_id == category
    ).first()

    if not current_category:
        return exceptions.NotFound()

    return manage_delete_item(category, "category", drop_category)


@app.route("/theunderground/categories/<category>/thumbnail.jpg")
@oidc.require_login
def get_category_thumbnail(category):
    if s3:
        return redirect(f"{config.url1_cdn_url}/list/category/img/{category}.img")

    return NormalCategoryAsset(category).send_file()
