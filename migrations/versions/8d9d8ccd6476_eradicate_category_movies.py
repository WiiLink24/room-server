"""Eradicate category_movies

Revision ID: 8d9d8ccd6476
Revises: 97296e3225e2
Create Date: 2021-05-17 23:58:54.685789

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import table, Integer, Column

revision = "8d9d8ccd6476"
down_revision = "97296e3225e2"
branch_labels = None
depends_on = None


def upgrade():
    # Migrate normal movies
    op.add_column(
        "movies",
        sa.Column("category_id", sa.Integer(), nullable=False, server_default="10000"),
    )
    op.create_foreign_key(
        None, "movies", "categories", ["category_id"], ["category_id"]
    )

    movies = table(
        "movies",
        Column("movie_id", Integer, primary_key=True, unique=True),
        Column("category_id", Integer),
    )
    category_movies = table(
        "category_movies",
        Column("category_id", Integer, primary_key=True),
        Column("movie_id", Integer, primary_key=True, unique=True),
    )
    op.execute(
        movies.update()
        .where(movies.c.movie_id == category_movies.c.movie_id)
        .values(
            {
                movies.c.category_id: category_movies.c.category_id,
            }
        )
    )

    # Migrate pay movies
    pay_movies = table(
        "pay_movies",
        Column("movie_id", Integer, primary_key=True, unique=True),
        Column("category_id", Integer),
    )
    category_pay_movies = table(
        "category_pay_movies",
        Column("category_id", Integer, primary_key=True),
        Column("movie_id", Integer, primary_key=True, unique=True),
    )

    op.alter_column(
        "pay_movies",
        "category_id",
        existing_type=sa.INTEGER(),
        nullable=False,
        server_default="20001",
    )
    op.create_foreign_key(
        None, "pay_movies", "pay_categories", ["category_id"], ["category_id"]
    )

    op.execute(
        pay_movies.update()
        .where(pay_movies.c.movie_id == category_pay_movies.c.movie_id)
        .values(
            {
                pay_movies.c.category_id: category_pay_movies.c.category_id,
            }
        )
    )

    op.drop_table("category_movies")
    op.drop_table("category_pay_movies")


def downgrade():
    op.create_table(
        "category_pay_movies",
        sa.Column("category_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("movie_id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.PrimaryKeyConstraint("movie_id", name="category_pay_movies_pkey"),
        sa.UniqueConstraint("movie_id", name="category_pay_movies_movie_id_key"),
    )
    op.create_table(
        "category_movies",
        sa.Column("category_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("movie_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(
            ["category_id"],
            ["categories.category_id"],
            name="category_movies_category_id_fkey",
        ),
        sa.ForeignKeyConstraint(
            ["movie_id"], ["movies.movie_id"], name="category_movies_movie_id_fkey"
        ),
        sa.PrimaryKeyConstraint("category_id", "movie_id", name="category_movies_pkey"),
    )

    op.drop_constraint(None, "pay_movies", type_="foreignkey")
    op.alter_column(
        "pay_movies", "category_id", existing_type=sa.INTEGER(), nullable=True
    )
    op.drop_constraint(None, "movies", type_="foreignkey")
    op.drop_column("movies", "category_id")
