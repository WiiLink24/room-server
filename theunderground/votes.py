import os
import config

from flask import (
    render_template,
    redirect,
    flash,
    send_from_directory,
    request,
    url_for,
)
from flask_login import login_required
from flask_wtf.file import FileRequired
from werkzeug import exceptions

from asset_data import NormalCategoryAsset
from models import Categories, Movies, db
from room import app, s3
from theunderground.forms import CategoryForm
from theunderground.operations import manage_delete_item
from theunderground.mobiclip import (
    get_category_list,
    validate_mobiclip,
    get_mobiclip_length,
    save_movie_data,
    delete_movie_data,
    get_movie_path,
)


@app.route("/theunderground/votes")
def votes_list_categories():
    page_num = request.args.get("page", default=1, type=int)

    categories = Categories.query.order_by(Categories.category_id.asc()).paginate(
        page=page_num, per_page=15, error_out=False
    )

    return render_template(
        "vote_category_list.html",
        categories=categories,
        type_length=categories.total,
        type_max_count=64,
    )

@app.route("/theunderground/votes/<category>/thumbnail.jpg")
def votes_get_category_thumbnail(category):
    if s3:
        return redirect(f"{config.url1_cdn_url}/list/category/img/{category}.img")

    return NormalCategoryAsset(category).send_file()

@app.route("/theunderground/votes/<category>")
def votes_list_movies(category):
    # Get our current page, or start from scratch.
    page_num = request.args.get("page", default=1, type=int)

    # We want at most 20 movies per page.
    movies = Movies.query.filter(Movies.category_id == category).paginate(
        page=page_num, per_page=20, error_out=False
    )

    return render_template(
        "vote_movie_list.html",
        movies=movies,
        category_id=category,
        type_length=movies.total,
        type_max_count=64,
    )

@app.route("/theunderground/movies/<movie_id>/thumbnail.jpg")
def votes_get_movie_thumbnail(movie_id):
    movie_dir = get_movie_path(movie_id)
    if s3:
        return redirect(f"{config.url1_cdn_url}/{movie_dir}/{movie_id}.img")

    return send_from_directory(movie_dir, f"{movie_id}.img")
