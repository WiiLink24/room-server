"""Separate Mii IDs from room IDs

Revision ID: 413307c4c044
Revises: d47aeb04a99c
Create Date: 2021-09-28 15:44:20.490928

"""
import os

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "413307c4c044"
down_revision = "d47aeb04a99c"
branch_labels = None
depends_on = None


def get_tables() -> (sa.table, sa.table):
    rooms = sa.table(
        "rooms",
        sa.Column("room_id", sa.Integer),
        sa.Column("mii_id", sa.Integer),
    )
    room_menu = sa.table(
        "room_menu",
        sa.Column("room_id", sa.Integer, primary_key=True),
    )

    return rooms, room_menu


def upgrade():
    # Rename room_id to room_id
    op.drop_constraint("rooms_room_id_fkey", "rooms", type_="foreignkey")
    op.execute("ALTER TABLE rooms RENAME room_id TO mii_id")
    op.create_foreign_key(None, "rooms", "mii_data", ["mii_id"], ["mii_id"])

    # Add room_id
    op.add_column(
        "rooms",
        sa.Column(
            "room_id",
            sa.Integer(),
            primary_key=True,
            autoincrement=True,
            nullable=False,
            server_default="1",
        ),
    )
    op.create_unique_constraint(None, "rooms", ["room_id"])

    rooms, room_menu = get_tables()

    # Migrate disk assets
    room_values = op.get_bind().execute("SELECT room_id, mii_id FROM rooms").fetchall()
    for room_id, mii_id in room_values:
        old_path = f"./assets/special-{mii_id}"
        new_path = f"./assets/special/{room_id}"
        os.renames(old_path, new_path)

    # Update room_menu to use room ID over mii ID
    op.execute(
        room_menu.update()
        .where(room_menu.c.room_id == rooms.c.mii_id)
        .values(
            {
                room_menu.c.room_id: rooms.c.room_id,
            }
        )
    )


def downgrade():
    # Revert disk asset movement
    room_values = op.get_bind().execute("SELECT room_id, mii_id FROM rooms").fetchall()
    for room_id, mii_id in room_values:
        old_path = f"./assets/special/{room_id}"
        new_path = f"./assets/special-{mii_id}"
        os.renames(old_path, new_path)

    # Revert room_menu
    rooms, room_menu = get_tables()
    op.execute(
        room_menu.update()
        .where(room_menu.c.room_id == rooms.c.room_id)
        .values(
            {
                room_menu.c.room_id: rooms.c.mii_id,
            }
        )
    )

    # Drop the new room_id
    op.drop_column("rooms", "room_id")

    # Rename mii_id to room_id
    op.drop_constraint("rooms_mii_id_fkey", "rooms", type_="foreignkey")
    op.execute("ALTER TABLE rooms RENAME mii_id TO room_id")
    op.create_foreign_key(None, "rooms", "mii_data", ["room_id"], ["mii_id"])
