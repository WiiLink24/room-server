import os
import config

from flask import redirect, render_template, request, url_for
from flask_login import login_required
from flask_wtf.file import FileRequired
from werkzeug import exceptions

from asset_data import NormalCategoryAsset
from models import Categories, db
from room import app, s3
from theunderground.forms import CategoryForm
from theunderground.operations import manage_delete_item


@app.route("/theunderground/categories")
@login_required
def list_categories():
    page_num = request.args.get("page", default=1, type=int)

    categories = Categories.query.order_by(Categories.category_id.asc()).paginate(
        page=page_num, per_page=15, error_out=False
    )

    return render_template(
        "category_list.html",
        categories=categories,
        type_length=categories.total,
        type_max_count=64,
    )


@app.route("/theunderground/categories/add", methods=["GET", "POST"])
@login_required
def add_category():
    form = CategoryForm()
    # As we're adding, ensure a file is required.
    form.thumbnail.validators = [FileRequired()]

    if form.validate_on_submit():
        new_category = Categories(name=form.category_name.data)

        # Add to retrieve the category ID.
        db.session.add(new_category)
        db.session.commit()

        # With this ID, write the thumbnail.
        NormalCategoryAsset(new_category.category_id).encode(form.thumbnail)
        return redirect(url_for("list_categories"))

    return render_template("category_action.html", form=form, action="Add")


@app.route("/theunderground/categories/<category>/edit", methods=["GET", "POST"])
@login_required
def edit_category(category):
    form = CategoryForm()
    form.submit.label.text = "Edit"

    # Populate data
    current_category = Categories.query.filter(
        Categories.category_id == category
    ).first()
    if not current_category:
        return exceptions.NotFound()

    if form.validate_on_submit():
        current_category.name = form.category_name.data
        db.session.commit()

        # Check if we have a new thumbnail.
        if form.thumbnail.data:
            NormalCategoryAsset(current_category.category_id).encode(form.thumbnail)

        return redirect(url_for("list_categories"))
    else:
        # Populate the current name.
        # category_action.html below will populate the current thumbnail.
        form.category_name.data = current_category.name

    return render_template(
        "category_action.html", category=current_category, form=form, action="Edit"
    )


@app.route("/theunderground/categories/<category>/remove", methods=["GET", "POST"])
@login_required
def remove_category(category):
    def drop_category():
        db.session.delete(current_category)
        db.session.commit()
        os.unlink(NormalCategoryAsset(category).asset_path())

        return redirect(url_for("list_categories"))

    current_category = Categories.query.filter(
        Categories.category_id == category
    ).first()

    if not current_category:
        return exceptions.NotFound()

    return manage_delete_item(category, "category", drop_category)


@app.route("/theunderground/categories/<category>/thumbnail.jpg")
@login_required
def get_category_thumbnail(category):
    if s3:
        return redirect(f"{config.url1_cdn_url}/list/category/img/{category}.img")

    return NormalCategoryAsset(category).send_file()
