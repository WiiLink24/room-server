"""Add second primary_key to RoomMiis

Revision ID: 6ebdcbc733bf
Revises: 4b7420e6c104
Create Date: 2024-07-04 22:31:59.115483

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6ebdcbc733bf"
down_revision = "4b7420e6c104"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("room_miis", schema=None) as batch_op:
        batch_op.alter_column("room_id", existing_type=sa.INTEGER(), nullable=False)
        batch_op.drop_constraint("room_miis_room_id_key", type_="unique")
        batch_op.create_unique_constraint(None, ["mii_id"])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("room_miis", schema=None) as batch_op:
        batch_op.drop_constraint(None, type_="unique")
        batch_op.create_unique_constraint("room_miis_room_id_key", ["room_id"])
        batch_op.alter_column("room_id", existing_type=sa.INTEGER(), nullable=False)

    # ### end Alembic commands ###