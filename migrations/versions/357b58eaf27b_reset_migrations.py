"""Reset Migrations

Revision ID: 357b58eaf27b
Revises: 
Create Date: 2024-06-29 17:02:21.005371

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "357b58eaf27b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("user")
    with op.batch_alter_table("giveaways", schema=None) as batch_op:
        batch_op.alter_column("email", existing_type=sa.VARCHAR(), nullable=False)
        batch_op.create_unique_constraint(None, ["id"])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("giveaways", schema=None) as batch_op:
        batch_op.drop_constraint(None, type_="unique")
        batch_op.alter_column("email", existing_type=sa.VARCHAR(), nullable=True)

    op.create_table(
        "user",
        sa.Column(
            "username", sa.VARCHAR(length=100), autoincrement=False, nullable=True
        ),
        sa.Column("password_hash", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.PrimaryKeyConstraint("id", name="user_pkey"),
        sa.UniqueConstraint("id", name="user_user_id_key"),
    )
    # ### end Alembic commands ###
