"""Remove ds_dist boolean column

Revision ID: ec29b09a3e38
Revises: 8d9d8ccd6476
Create Date: 2021-05-26 00:51:00.624446

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "ec29b09a3e38"
down_revision = "8d9d8ccd6476"
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column("movies", "ds_dist")


def downgrade():
    op.add_column(
        "movies",
        sa.Column("ds_dist", sa.BOOLEAN(), autoincrement=False, nullable=False),
    )
