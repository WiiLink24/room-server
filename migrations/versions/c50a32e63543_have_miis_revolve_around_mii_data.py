"""Have Miis revolve around mii_data

Revision ID: c50a32e63543
Revises: a33eb0efb9b5
Create Date: 2020-10-24 09:14:20.822326

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c50a32e63543"
down_revision = "a33eb0efb9b5"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, "concierge_miis", "mii_data", ["mii_id"], ["mii_id"])
    op.drop_constraint("mii_data_mii_id_fkey", "mii_data", type_="foreignkey")
    op.drop_constraint("mii_msg_info_mii_id_fkey", "mii_msg_info", type_="foreignkey")
    op.create_foreign_key(None, "mii_msg_info", "mii_data", ["mii_id"], ["mii_id"])
    op.create_foreign_key(None, "parade_miis", "mii_data", ["miiid"], ["mii_id"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "parade_miis", type_="foreignkey")
    op.drop_constraint(None, "mii_msg_info", type_="foreignkey")
    op.create_foreign_key(
        "mii_msg_info_mii_id_fkey",
        "mii_msg_info",
        "concierge_miis",
        ["mii_id"],
        ["mii_id"],
    )
    op.create_foreign_key(
        "mii_data_mii_id_fkey", "mii_data", "concierge_miis", ["mii_id"], ["mii_id"]
    )
    op.drop_constraint(None, "concierge_miis", type_="foreignkey")
    # ### end Alembic commands ###
