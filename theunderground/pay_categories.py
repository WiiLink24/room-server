import os

from flask import redirect, render_template, request, url_for
from flask_login import login_required
from werkzeug import exceptions

from asset_data import PayCategoryAsset
from models import PayCategories, db, PayCategoryHeaders
from room import app
from theunderground.forms import CategoryForm, PayCategoryHeaderForm
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
        PayCategoryAsset(new_category.category_id).encode(form.thumbnail)
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
            PayCategoryAsset(current_category.category_id).encode(form.thumbnail)

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
        os.unlink(PayCategoryAsset(category).asset_path())
        db.session.delete(current_category)
        db.session.commit()

        return redirect(url_for("list_pay_categories"))

    current_category = PayCategories.query.filter(
        PayCategories.category_id == category
    ).first()
    if not current_category:
        return exceptions.NotFound()

    return manage_delete_item(category, "pay category", drop_pay_category)


@app.route("/theunderground/paycategories/headers")
@login_required
def list_pay_category_headers():
    """Internally named headers, basically genres."""
    genres = PayCategoryHeaders.query.paginate(1, 15, error_out=False)

    return render_template(
        "pay_category_header_list.html",
        genres=genres,
        type_length=genres.total,
        type_max_count=64,
    )


@app.route("/theunderground/paycategories/headers/add", methods=["GET", "POST"])
@login_required
def add_pay_category_header():
    form = PayCategoryHeaderForm()

    if form.validate_on_submit():
        new_header = PayCategoryHeaders(title=form.title.data)

        # Add to retrieve the category ID.
        db.session.add(new_header)
        db.session.commit()

        return redirect(url_for("list_pay_category_headers"))

    return render_template("pay_category_header_action.html", form=form, action="Add")


@app.route(
    "/theunderground/paycategories/headers/<title>/edit", methods=["GET", "POST"]
)
@login_required
def edit_pay_category_header(title):
    form = PayCategoryHeaderForm()
    form.submit.label.text = "Edit"

    # Populate data
    current_category = PayCategoryHeaders.query.filter(
        PayCategoryHeaders.title == title
    ).first()
    if not current_category:
        return exceptions.NotFound()

    if form.validate_on_submit():
        current_category.title = form.title.data
        db.session.commit()

        return redirect(url_for("list_pay_category_headers"))
    else:
        # Populate the current name.
        # category_add.html below will populate the current thumbnail.
        form.title.data = current_category.title

    return render_template("pay_category_header_action.html", form=form, action="Edit")


@app.route(
    "/theunderground/paycategories/headers/<title>/remove", methods=["GET", "POST"]
)
@login_required
def remove_pay_category_header(title):
    def drop_pay_category_header():
        db.session.delete(current_category)
        db.session.commit()

        return redirect(url_for("list_pay_category_headers"))

    current_category = PayCategoryHeaders.query.filter(
        PayCategoryHeaders.title == title
    ).first()
    if not current_category:
        return exceptions.NotFound()

    return manage_delete_item(title, "pay genre", drop_pay_category_header)


@app.route("/theunderground/paycategories/<category>/thumbnail.jpg")
@login_required
def get_pay_category_thumbnail(category):
    return PayCategoryAsset(category).send_file()
