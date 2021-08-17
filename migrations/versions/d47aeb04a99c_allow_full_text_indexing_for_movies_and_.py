"""Allow full text indexing for movies and pay movies

Revision ID: d47aeb04a99c
Revises: 716677d220fd
Create Date: 2021-08-16 22:48:49.324882

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d47aeb04a99c"
down_revision = "716677d220fd"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "movies",
        sa.Column(
            "search_vector",
            sqlalchemy_utils.types.ts_vector.TSVectorType(),
            nullable=True,
        ),
    )
    op.create_index(
        "ix_movies_search_vector",
        "movies",
        ["search_vector"],
        unique=False,
        postgresql_using="gin",
    )
    op.add_column(
        "pay_movies",
        sa.Column(
            "search_vector",
            sqlalchemy_utils.types.ts_vector.TSVectorType(),
            nullable=True,
        ),
    )
    op.create_index(
        "ix_pay_movies_search_vector",
        "pay_movies",
        ["search_vector"],
        unique=False,
        postgresql_using="gin",
    )

    # Create initial index
    op.execute("UPDATE movies SET search_vector = to_tsvector(title)")
    op.execute(
        "UPDATE pay_movies SET search_vector = to_tsvector(title) || to_tsvector(note)"
    )


def downgrade():
    op.drop_index(
        "ix_pay_movies_search_vector", table_name="pay_movies", postgresql_using="gin"
    )
    op.drop_column("pay_movies", "search_vector")
    op.drop_index(
        "ix_movies_search_vector", table_name="movies", postgresql_using="gin"
    )
    op.drop_column("movies", "search_vector")
