"""Convert room_data to jsonb

Revision ID: 70ae2a4487d5
Revises: 9a3ca245cede
Create Date: 2026-06-27 15:59:14.509899

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "70ae2a4487d5"
down_revision = "9a3ca245cede"
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """ALTER TABLE room_menu ALTER COLUMN data TYPE jsonb using data::jsonb"""
    )
    # ### end Alembic commands ###


def downgrade():

    op.execute("""ALTER TABLE room_menu ALTER COLUMN data TYPE text using data::text""")
    # ### end Alembic commands ###
