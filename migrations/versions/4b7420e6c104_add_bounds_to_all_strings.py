"""Add bounds to all strings

Revision ID: 4b7420e6c104
Revises: e68ac4fc8fee
Create Date: 2024-07-03 13:09:59.316769

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4b7420e6c104"
down_revision = "e68ac4fc8fee"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("mii_msg_info", schema=None) as batch_op:
        batch_op.alter_column("seq", existing_type=sa.INTEGER(), nullable=False)

    with op.batch_alter_table("movies", schema=None) as batch_op:
        batch_op.alter_column(
            "title",
            existing_type=sa.VARCHAR(length=48),
            type_=sa.String(length=47),
            existing_nullable=False,
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("movies", schema=None) as batch_op:
        batch_op.alter_column(
            "title",
            existing_type=sa.String(length=47),
            type_=sa.VARCHAR(length=48),
            existing_nullable=False,
        )

    with op.batch_alter_table("mii_msg_info", schema=None) as batch_op:
        batch_op.alter_column("seq", existing_type=sa.INTEGER(), nullable=True)

    # ### end Alembic commands ###
