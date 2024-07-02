"""Readd sequence to MiiMsgInfo

Revision ID: e68ac4fc8fee
Revises: 42bc7a8c4eb9
Create Date: 2024-07-02 17:17:27.054317

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "e68ac4fc8fee"
down_revision = "42bc7a8c4eb9"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("mii_msg_info", schema=None) as batch_op:
        batch_op.add_column(sa.Column("seq", sa.Integer()))
    # ### end Alembic commands ###

    op.execute(
        """
     UPDATE mii_msg_info
     SET seq = 1;
     """
    )

    # Finally re-add the constraint.
    op.alter_column(
        "mii_msg_info",
        "seq",
        existing_type=sa.Integer(),
        nullable=True,
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("mii_msg_info", schema=None) as batch_op:
        batch_op.drop_column("seq")

    # ### end Alembic commands ###
