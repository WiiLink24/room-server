import os
import config
import io
import csv

from flask import (
    render_template,
    redirect,
    send_from_directory,
    request,
    make_response,
)

from asset_data import NormalCategoryAsset
from models import Categories, Movies, EvaluateData
from room import app, s3
from theunderground.admin import oidc
from theunderground.mobiclip import get_movie_path


@app.route("/theunderground/votes")
def votes_list_categories():
    page_num = request.args.get("page", default=1, type=int)

    categories = Categories.query.order_by(Categories.category_id.asc()).paginate(
        page=page_num, per_page=15, error_out=False
    )

    votes = {}
    evaluatedata = EvaluateData.query

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
        "age.avg": 0,
    }

    return render_template(
        "vote_category_list.html",
        categories=categories,
        votes=votes,
        type_length=categories.total,
        type_max_count=64,
    )


@app.route("/theunderground/votes/c<category>/thumbnail.jpg")
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

        votes[movie.movie_id] = {
            "count": movie_vote.count(),
            "vote.1": movie_vote.filter_by(vote=1).count(),
            "vote.2": movie_vote.filter_by(vote=2).count(),
            "vote.3": movie_vote.filter_by(vote=3).count(),
            "vote.4": movie_vote.filter_by(vote=4).count(),
            "gender.1": movie_vote.filter_by(gender=1).count(),
            "gender.2": movie_vote.filter_by(gender=2).count(),
            "blood.0": movie_vote.filter_by(blood=0).count(),
            "blood.1": movie_vote.filter_by(blood=1).count(),
            "blood.2": movie_vote.filter_by(blood=2).count(),
            "blood.3": movie_vote.filter_by(blood=3).count(),
            "blood.4": movie_vote.filter_by(blood=4).count(),
            "blood.avg": 0,
            "age.avg": 0,
        }

    return render_template(
        "vote_movie_list.html",
        movies=movies,
        votes=votes,
        category_id=category,
        type_length=movies.total,
        type_max_count=64,
    )


@app.route("/theunderground/votes/m<movie_id>/thumbnail.jpg")
def votes_get_movie_thumbnail(movie_id):
    movie_dir = get_movie_path(movie_id)
    if s3:
        return redirect(f"{config.url1_cdn_url}/{movie_dir}/{movie_id}.img")

    return send_from_directory(movie_dir, f"{movie_id}.img")


@app.route("/theunderground/votes/data.csv")
@oidc.require_login
def votes_download():

    evaluatedata = EvaluateData.query.all()

    si = io.StringIO()
    cw = csv.writer(si)

    cw.writerow(
        [
            "id",
            "movie_id",
            "gender",
            "blood",
            "age",
            "vote"
        ]
    )

    for data in evaluatedata:
        cw.writerow(
            [
                data.id,
                data.movie_id,
                data.gender,
                data.blood,
                data.age,
                data.vote
            ]
        )

    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=votes.csv"
    output.headers["Content-Type"] = "text/csv"

    return output
