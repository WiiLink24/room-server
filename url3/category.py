from asset_data import PayCategoryAsset
from room import app
from helpers import xml_node_name, RepeatedElement
from models import PayCategories, db

from werkzeug import exceptions
from flask import send_from_directory


@app.route("/url3/pay/list/category/<int:list_id>.xml")
@xml_node_name("PayCategoryList")
def pay_list_category(list_id: int):
    queried_categories = PayCategories.query.order_by(PayCategories.name.asc()).all()

    retrieved_data = (
        db.session.query(PayCategories)
        .filter(PayCategories.genre_id == list_id)
        .order_by(PayCategories.category_id)
        .all()
    )
    filler = []

    if list_id <= 9:
        filler.extend(
            RepeatedElement(
                {
                    "place": i + 1,
                    "categid": pay_categories.category_id,
                    "name": pay_categories.name,
                    "sppageid": 0,
                    "splinktext": "Link Text",
                }
            )
            for i, pay_categories in enumerate(queried_categories)
        )
    elif retrieved_data:
        filler.extend(
            RepeatedElement(
                {
                    "place": i + 1,
                    "categid": pay_categories.category_id,
                    "name": pay_categories.name,
                    "sppageid": 0,
                    "splinktext": "Link Text",
                }
            )
            for i, pay_categories in enumerate(retrieved_data)
        )
    else:
        # Looks like this category does not exist, or contains no movies.
        return exceptions.NotFound()

    return {
        "type": 3,
        "img": 1,
        "categinfo": filler,
    }


if app.debug:

    @app.route("/url3/pay/list/category/img/<category_id>.img")
    # Grabs the thumbnail for the categories
    def serve_pay_category_thumbnail(category_id):
        return PayCategoryAsset(category_id).send_file()
