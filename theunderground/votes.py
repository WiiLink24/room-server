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
from flask_wtf.file import FileRequired
from werkzeug import exceptions

from asset_data import NormalCategoryAsset
from models import Categories, Movies, EvaluateData
from room import app, s3
from theunderground.forms import CategoryForm
from theunderground.operations import manage_delete_item
from theunderground.mobiclip import (
    get_movie_path,
)


@app.route("/theunderground/votes")
def votes_list_categories():
    page_num = request.args.get("page", default=1, type=int)

    categories = Categories.query.order_by(Categories.category_id.asc()).paginate(
        page=page_num, per_page=15, error_out=False
    )

    votes = {}
    evaluatedata = movie_vote = EvaluateData.query

    movie_vote_count = evaluatedata.count()

    movie_vote_t1 = evaluatedata.filter_by(vote=1).count()
    movie_vote_t2 = evaluatedata.filter_by(vote=2).count()
    movie_vote_t3 = evaluatedata.filter_by(vote=3).count()
    movie_vote_t4 = evaluatedata.filter_by(vote=4).count()

    movie_gender_t1 = evaluatedata.filter_by(gender=1).count()
    movie_gender_t2 = evaluatedata.filter_by(gender=2).count()

    movie_blood_t0 = evaluatedata.filter_by(blood=0).count()
    movie_blood_t1 = evaluatedata.filter_by(blood=1).count()
    movie_blood_t2 = evaluatedata.filter_by(blood=2).count()
    movie_blood_t3 = evaluatedata.filter_by(blood=3).count()
    movie_blood_t4 = evaluatedata.filter_by(blood=4).count()

    votes = {
        "count": movie_vote_count,
        "vote.1": movie_vote_t1,
        "vote.2": movie_vote_t2,
        "vote.3": movie_vote_t3,
        "vote.4": movie_vote_t4,
        "gender.1": movie_gender_t1,
        "gender.2": movie_gender_t2,
        "blood.0": movie_blood_t0,
        "blood.1": movie_blood_t1,
        "blood.2": movie_blood_t2,
        "blood.3": movie_blood_t3,
        "blood.4": movie_blood_t4,
        "blood.avg": 0,
        "age.avg": 0
    }

    return render_template(
        "vote_category_list.html",
        categories=categories,
        votes=votes,
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

    votes = {}
    evaluatedata = movie_vote = EvaluateData.query

    for movie in movies.items:
        movie_vote = evaluatedata.filter_by(movie_id=movie.movie_id)

        movie_vote_count = movie_vote.count()

        movie_vote_t1 = movie_vote.filter_by(vote=1).count()
        movie_vote_t2 = movie_vote.filter_by(vote=2).count()
        movie_vote_t3 = movie_vote.filter_by(vote=3).count()
        movie_vote_t4 = movie_vote.filter_by(vote=4).count()

        movie_gender_t1 = movie_vote.filter_by(gender=1).count()
        movie_gender_t2 = movie_vote.filter_by(gender=2).count()

        votes[movie.movie_id] = {
            "count": movie_vote_count,
            "vote.1": movie_vote_t1,
            "vote.2": movie_vote_t2,
            "vote.3": movie_vote_t3,
            "vote.4": movie_vote_t4,
            "gender.1": movie_gender_t1,
            "gender.2": movie_gender_t2,
            "blood.0": 0,
            "blood.1": 0,
            "blood.2": 0,
            "blood.3": 0,
            "blood.4": 0,
            "blood.avg": 0,
            "age.avg": 0
        }

    print(votes)

    return render_template(
        "vote_movie_list.html",
        movies=movies,
        votes=votes,
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
