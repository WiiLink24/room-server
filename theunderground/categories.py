import os

from flask import redirect, render_template, send_from_directory, request, url_for
from flask_login import login_required
from werkzeug import exceptions

from models import Categories, db
from room import app
from theunderground.encodemii import category_encode
from theunderground.forms import CategoryEditForm, CategoryAddForm
from theunderground.operations import manage_delete_item


@app.route("/theunderground/categories")
@login_required
def list_categories():
    page_num = request.args.get("page", default=1, type=int)

    categories = Categories.query.order_by(Categories.category_id.asc()).paginate(
        page_num, 15, error_out=False
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
    form = CategoryAddForm()

    if form.validate_on_submit():
        new_category = Categories(name=form.category_name.data)

        # Add to retrieve the category ID.
        db.session.add(new_category)
        db.session.commit()

        # With this ID, write the thumbnail.
        write_category_thumbnail(new_category.category_id, form.thumbnail.data.read())
        return redirect(url_for("list_categories"))

    return render_template("category_add.html", form=form)


@app.route("/theunderground/categories/<category>/edit", methods=["GET", "POST"])
@login_required
def edit_category(category):
    form = CategoryEditForm()

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
            write_category_thumbnail(
                current_category.category_id, form.thumbnail.data.read()
            )

        return redirect(url_for("list_categories"))
    else:
        # Populate the current name.
        # category_add.html below will populate the current thumbnail.
        form.category_name.data = current_category.name

    return render_template("category_edit.html", category=current_category, form=form)


@app.route("/theunderground/categories/<category>/remove", methods=["GET", "POST"])
@login_required
def remove_category(category):
    def drop_category():
        db.session.delete(current_category)
        db.session.commit()

        os.unlink(get_category_location(category))

        return redirect(url_for("list_categories"))

    current_category = Categories.query.filter(
        Categories.category_id == category
    ).first()

    if not current_category:
        return exceptions.NotFound()

    return manage_delete_item(category, "category", drop_category)


def get_category_location(category_id: int):
    return f"./assets/normal-category/{category_id}.img"


def write_category_thumbnail(category_id: int, given_file: bytes):
    encoded_image = category_encode(given_file)
    with open(get_category_location(category_id), "wb") as thumbnail_file:
        thumbnail_file.write(encoded_image)


@app.route("/theunderground/categories/<category>/thumbnail.jpg")
@login_required
def get_category_thumbnail(category):
    return send_from_directory("./assets/normal-category", f"{category}.img")
