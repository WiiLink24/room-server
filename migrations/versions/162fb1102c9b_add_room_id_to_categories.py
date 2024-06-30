"""Add room_id to Categories

Revision ID: 162fb1102c9b
Revises: 9c8a56231382
Create Date: 2024-06-30 12:02:00.363756

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "162fb1102c9b"
down_revision = "9c8a56231382"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("categories", schema=None) as batch_op:
        batch_op.add_column(sa.Column("sp_page_id", sa.Integer()))

    op.execute(
        """
     UPDATE categories
     SET sp_page_id = 1;
     """
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("categories", schema=None) as batch_op:
        batch_op.drop_column("sp_page_id")

    # ### end Alembic commands ###
