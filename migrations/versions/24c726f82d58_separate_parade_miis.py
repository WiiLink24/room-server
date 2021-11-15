"""Separate parade_miis

Revision ID: 24c726f82d58
Revises: 413307c4c044
Create Date: 2021-09-29 02:09:38.416634

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "24c726f82d58"
down_revision = "413307c4c044"
branch_labels = None
depends_on = None


def upgrade():
    # Create our room_miis table.
    op.create_table(
        "room_miis",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("room_id", sa.Integer(), nullable=False),
        sa.Column("mii_id", sa.Integer(), nullable=False),
        sa.Column("mii_msg", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["mii_id"],
            ["mii_data.mii_id"],
        ),
        sa.ForeignKeyConstraint(
            ["room_id"],
            ["rooms.room_id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # Add mii_msg and level columns.
    op.add_column("rooms", sa.Column("mii_msg", sa.String(), nullable=True))
    op.add_column("rooms", sa.Column("level", sa.Integer(), nullable=True))

    # Before we drop parade_miis and similar, we need to salvage
    # data from it. First, we salvage logo_bin (the parade banner)
    # and write it to disk for that room ID.
    logos = (
        op.get_bind()
        .execute(
            "SELECT rooms.room_id, parade_miis.logo_bin FROM rooms, parade_miis WHERE rooms.mii_id = parade_miis.mii_id"
        )
        .fetchall()
    )
    for room_id, logo_bin in logos:
        open(f"./assets/special/{room_id}/parade_banner.jpg", "wb").write(logo_bin)

    # Finally, migrate data otherwise.
    # We will not use SQLAlchemy for this.
    op.get_bind().execute(
        "INSERT INTO room_miis (room_id, mii_id, mii_msg)"
        " SELECT rooms.room_id, parade_miis.mii_id, rooms.mii_msg FROM rooms, parade_miis"
        " WHERE rooms.mii_id = parade_miis.mii_id"
    )
    op.get_bind().execute(
        "UPDATE rooms "
        "SET level = parade_miis.level, mii_msg = parade_miis.mii_msg "
        "FROM parade_miis "
        "WHERE rooms.mii_id = parade_miis.mii_id"
    )

    op.drop_table("parade_miis")
    op.drop_column("rooms", "mii_msg")
    op.drop_column("rooms", "logo2_id")


def downgrade():
    raise ValueError(
        "Downgrading from this revision is not supported. Please manually restore images."
    )
