"""Pay date added

Revision ID: 97296e3225e2
Revises: d20c0219e18c
Create Date: 2021-05-04 20:48:28.950492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "97296e3225e2"
down_revision = "d20c0219e18c"
branch_labels = None
depends_on = None


def upgrade():
    op.create_unique_constraint(None, "categories", ["category_id"])
    op.create_unique_constraint(None, "category_pay_movies", ["movie_id"])
    op.create_unique_constraint(None, "concierge_miis", ["mii_id"])
    op.create_unique_constraint(None, "movies", ["movie_id"])
    op.create_unique_constraint(None, "mii_msg", ["id"])
    op.create_unique_constraint(None, "pay_categories", ["category_id"])
    op.create_unique_constraint(None, "pay_category_headers", ["title"])
    op.add_column(
        "pay_movies",
        sa.Column(
            "date_added", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
    )
    op.create_unique_constraint(None, "pay_movies", ["movie_id"])
    op.create_unique_constraint(None, "pay_posters", ["poster_id"])
    op.create_unique_constraint(None, "posters", ["poster_id"])
    op.create_unique_constraint(None, "room_menu", ["id"])


def downgrade():
    op.drop_constraint(None, "room_menu", type_="unique")
    op.drop_constraint(None, "posters", type_="unique")
    op.drop_constraint(None, "pay_posters", type_="unique")
    op.drop_constraint(None, "pay_movies", type_="unique")
    op.drop_column("pay_movies", "date_added")
    op.drop_constraint(None, "pay_category_headers", type_="unique")
    op.drop_constraint(None, "pay_categories", type_="unique")
    op.drop_constraint(None, "mii_msg", type_="unique")
    op.drop_constraint(None, "movies", type_="unique")
    op.drop_constraint(None, "concierge_miis", type_="unique")
    op.drop_constraint(None, "category_pay_movies", type_="unique")
    op.drop_constraint(None, "categories", type_="unique")
