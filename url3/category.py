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
        for i, pay_categories in enumerate(queried_categories):
            # Items must be indexed by 1.
            filler.append(
                RepeatedElement(
                    {
                        "place": i + 1,
                        "categid": pay_categories.category_id,
                        "name": pay_categories.name,
                        "sppageid": 0,
                        "splinktext": "Link Text",
                    }
                )
            )
    else:
        if not retrieved_data:
            # Looks like this category does not exist, or contains no movies.
            return exceptions.NotFound()

        for i, pay_categories in enumerate(retrieved_data):
            # This section allows us to sort the categories into genres
            # Instead of them showing up in all of the genres
            filler.append(
                RepeatedElement(
                    {
                        "place": i + 1,
                        "categid": pay_categories.category_id,
                        "name": pay_categories.name,
                        "sppageid": 0,
                        "splinktext": "Link Text",
                    }
                )
            )

    return {
        "type": 3,
        "img": 1,
        "categinfo": filler,
    }


if app.debug:

    @app.route("/url3/pay/list/category/img/<name>.img")
    # Grabs the thumbnail for the categories
    def serve_pay_category_thumbnail(name):
        return send_from_directory("assets/pay-category", name + ".img")
