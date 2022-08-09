"""Remove contact boolean field

Revision ID: 01a299e3292d
Revises: e6c5c826b357
Create Date: 2022-08-09 04:34:57.915400

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "01a299e3292d"
down_revision = "e6c5c826b357"
branch_labels = None
depends_on = None


def upgrade():
    op.drop_column("rooms", "contact")


def downgrade():
    op.add_column(
        "rooms", sa.Column("contact", sa.BOOLEAN(), autoincrement=False, nullable=True)
    )
