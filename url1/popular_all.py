import config

from sqlalchemy import func
from io import BytesIO

from models import EvaluateData, Movies, db
from room import app, s3
from helpers import xml_node_name, RepeatedElement, current_date_and_time


def query_popular(*criteria):
    query = (
        db.session.query(EvaluateData, Movies)
        # Select movie_id and title...
        .with_entities(EvaluateData.movie_id, Movies.title)
        # ...by grouping together all duplicate movie votes to their title...
        .group_by(EvaluateData.movie_id, Movies.title)
        # ...then join together the movie_id of EvaluateData to that of Movies for title...
        .filter(EvaluateData.movie_id == Movies.movie_id)
        # ...and then sort by highest voted movies...
        .order_by(func.sum(EvaluateData.vote).desc())
    )

    # Finally, apply all needed criteria!
    for expression in criteria:
        query = query.filter(expression)

    # Limit to 64, and go wild!
    popular_movies = query.limit(64).all()

    movieinfo = []
    for i, movie in enumerate(popular_movies):
        # Items must be indexed by 1.
        movieinfo.append(
            RepeatedElement(
                {
                    "rank": i + 1,
                    "movieid": movie.movie_id,
                    "title": movie.title,
                    "genre": 1,
                    "strdt": current_date_and_time(),
                    "pop": 0,
                }
            )
        )

    return movieinfo


@app.route("/url1/list/popular/all.xml")
@xml_node_name("Popular")
def popular_all():
    return {
        "movieinfo": query_popular(),
    }


from url1.popular_age import *
from url1.popular_blood import *


def generate_all_popular():
    with app.app_context():
        # This is specifically for S3/R2 reasons. A scheduler is set that at the dawn of a new day (UTC), it will
        # generate and upload all the XMLs that are related to voting.
        payload = popular_all()
        s3.upload_fileobj(
            BytesIO(payload), config.r2_bucket_name, "list/popular/all.xml"
        )

        # Blood
        payload = popular_blood_a()
        s3.upload_fileobj(
            BytesIO(payload), config.r2_bucket_name, "list/popular/11.xml"
        )

        payload = popular_blood_b()
        s3.upload_fileobj(
            BytesIO(payload), config.r2_bucket_name, "list/popular/12.xml"
        )

        payload = popular_blood_ab()
        s3.upload_fileobj(
            BytesIO(payload), config.r2_bucket_name, "list/popular/14.xml"
        )

        payload = popular_blood_o()
        s3.upload_fileobj(
            BytesIO(payload), config.r2_bucket_name, "list/popular/13.xml"
        )

        # Gender
        payload = popular_male()
        s3.upload_fileobj(
            BytesIO(payload), config.r2_bucket_name, "list/popular/01.xml"
        )

        payload = popular_female()
        s3.upload_fileobj(
            BytesIO(payload), config.r2_bucket_name, "list/popular/02.xml"
        )

        # Age
        payload = popular_under_age_9()
        s3.upload_fileobj(
            BytesIO(payload), config.r2_bucket_name, "list/popular/03.xml"
        )

        payload = popular_age_10()
        s3.upload_fileobj(
            BytesIO(payload), config.r2_bucket_name, "list/popular/04.xml"
        )

        payload = popular_age_20()
        s3.upload_fileobj(
            BytesIO(payload), config.r2_bucket_name, "list/popular/05.xml"
        )

        payload = popular_age_30()
        s3.upload_fileobj(
            BytesIO(payload), config.r2_bucket_name, "list/popular/06.xml"
        )

        payload = popular_age_40()
        s3.upload_fileobj(
            BytesIO(payload), config.r2_bucket_name, "list/popular/07.xml"
        )

        payload = popular_age_50()
        s3.upload_fileobj(
            BytesIO(payload), config.r2_bucket_name, "list/popular/08.xml"
        )

        payload = popular_age_60()
        s3.upload_fileobj(
            BytesIO(payload), config.r2_bucket_name, "list/popular/09.xml"
        )

        payload = popular_age_over_70()
        s3.upload_fileobj(
            BytesIO(payload), config.r2_bucket_name, "list/popular/10.xml"
        )
