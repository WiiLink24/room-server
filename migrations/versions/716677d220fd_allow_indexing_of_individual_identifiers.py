"""Allow indexing of individual identifiers

Revision ID: 716677d220fd
Revises: 30bb30ec6914
Create Date: 2021-08-03 00:15:26.434399

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "716677d220fd"
down_revision = "30bb30ec6914"
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column("concierge_miis", "update_date")
    op.create_index(
        op.f("ix_evaluate_data_movie_id"), "evaluate_data", ["movie_id"], unique=False
    )
    op.create_unique_constraint(None, "evaluate_data", ["id"])
    op.create_index(
        op.f("ix_poll_data_poll_id"), "poll_data", ["poll_id"], unique=False
    )
    op.create_unique_constraint(None, "poll_data", ["id"])


def downgrade():
    op.drop_constraint(None, "poll_data", type_="unique")
    op.drop_index(op.f("ix_poll_data_poll_id"), table_name="poll_data")
    op.drop_constraint(None, "evaluate_data", type_="unique")
    op.drop_index(op.f("ix_evaluate_data_movie_id"), table_name="evaluate_data")
