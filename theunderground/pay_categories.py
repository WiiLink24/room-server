import os

from flask import redirect, render_template, send_from_directory, request, url_for
from flask_login import login_required
from flask_wtf.file import FileRequired
from werkzeug import exceptions

from models import PayCategories, db
from room import app
from theunderground.encodemii import category_encode
from theunderground.forms import CategoryForm
from theunderground.operations import manage_delete_item


@app.route("/theunderground/paycategories")
@login_required
def list_pay_categories():
    page_num = request.args.get("page", default=1, type=int)

    categories = PayCategories.query.order_by(PayCategories.category_id.asc()).paginate(
        page_num, 15, error_out=False
    )

    return render_template(
        "pay_category_list.html",
        categories=categories,
        type_length=categories.total,
        type_max_count=64,
    )


@app.route("/theunderground/paycategories/add", methods=["GET", "POST"])
@login_required
def add_pay_category():
    form = CategoryForm()
    # As we're adding, ensure a file is required.
    form.thumbnail.flags.required = True

    if form.validate_on_submit():
        new_category = PayCategories(name=form.category_name.data)

        # Add to retrieve the category ID.
        db.session.add(new_category)
        db.session.commit()

        # With this ID, write the thumbnail.
        write_pay_category_thumbnail(
            new_category.category_id, form.thumbnail.data.read()
        )
        return redirect(url_for("list_pay_categories"))

    return render_template("pay_category_action.html", form=form, action="Add")


@app.route("/theunderground/paycategories/<category>/edit", methods=["GET", "POST"])
@login_required
def edit_pay_category(category):
    form = CategoryForm()
    form.submit.label.text = "Edit"

    # Populate data
    current_category = PayCategories.query.filter(
        PayCategories.category_id == category
    ).first()
    if not current_category:
        return exceptions.NotFound()

    if form.validate_on_submit():
        current_category.name = form.category_name.data
        db.session.commit()

        # Check if we have a new thumbnail.
        if form.thumbnail.data:
            write_pay_category_thumbnail(
                current_category.category_id, form.thumbnail.data.read()
            )

        return redirect(url_for("list_pay_categories"))
    else:
        # Populate the current name.
        # category_add.html below will populate the current thumbnail.
        form.category_name.data = current_category.name

    return render_template(
        "pay_category_action.html", category=current_category, form=form, action="Edit"
    )


@app.route("/theunderground/paycategories/<category>/remove", methods=["GET", "POST"])
@login_required
def remove_pay_category(category):
    def drop_pay_category():
        os.unlink(get_pay_category_location(category))

        db.session.delete(current_category)
        db.session.commit()

        return redirect(url_for("list_pay_categories"))

    current_category = PayCategories.query.filter(
        PayCategories.category_id == category
    ).first()
    if not current_category:
        return exceptions.NotFound()

    return manage_delete_item(category, "pay category", drop_pay_category)


def get_pay_category_location(category_id: int):
    return f"./assets/pay-category/{category_id}.img"


def write_pay_category_thumbnail(category_id: int, given_file: bytes):
    encoded_image = category_encode(given_file)
    with open(get_pay_category_location(category_id), "wb") as thumbnail_file:
        thumbnail_file.write(encoded_image)


@app.route("/theunderground/paycategories/<category>/thumbnail.jpg")
@login_required
def get_pay_category_thumbnail(category):
    return send_from_directory("./assets/pay-category", f"{category}.img")
