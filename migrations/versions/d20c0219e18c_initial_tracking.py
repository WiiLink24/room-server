"""Initial tracking

Revision ID: d20c0219e18c
Revises: 
Create Date: 2021-05-04 20:35:49.421200

"""
from alembic import op
import models
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d20c0219e18c"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "categories",
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("category_id"),
        sa.UniqueConstraint("category_id"),
    )
    op.create_table(
        "category_pay_movies",
        sa.Column("category_id", sa.Integer(), nullable=True),
        sa.Column("movie_id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("movie_id"),
        sa.UniqueConstraint("movie_id"),
    )
    op.create_table(
        "mii_data",
        sa.Column("mii_id", sa.Integer(), nullable=False),
        sa.Column("data", sa.LargeBinary(length=74), nullable=False),
        sa.Column("name", sa.String(length=10), nullable=False),
        sa.Column("color1", sa.String(length=6), nullable=False),
        sa.Column("color2", sa.String(length=6), nullable=False),
        sa.PrimaryKeyConstraint("mii_id"),
    )
    op.create_table(
        "movies",
        sa.Column("movie_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=48), nullable=False),
        sa.Column("length", sa.String(length=8), nullable=False),
        sa.Column("aspect", sa.Boolean(), nullable=False),
        sa.Column("genre", sa.Integer(), nullable=False),
        sa.Column("sp_page_id", sa.Integer(), nullable=False),
        sa.Column("ds_dist", sa.Boolean(), nullable=False),
        sa.Column("ds_mov_id", sa.Integer(), nullable=True),
        sa.Column("staff", sa.Boolean(), nullable=False),
        sa.Column(
            "date_added", sa.DateTime(), server_default=sa.text("now()"), nullable=False
        ),
        sa.PrimaryKeyConstraint("movie_id"),
        sa.UniqueConstraint("movie_id"),
    )
    op.create_table(
        "mii_msg",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("msg", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "pay_categories",
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("genre_id", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("category_id"),
        sa.UniqueConstraint("category_id"),
    )
    op.create_table(
        "pay_category_headers",
        sa.Column("title", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("title"),
        sa.UniqueConstraint("title"),
    )
    op.create_table(
        "pay_movies",
        sa.Column("movie_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=15), nullable=False),
        sa.Column("length", sa.String(), nullable=False),
        sa.Column("note", sa.String(length=76), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("released", sa.String(length=10), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("movie_id"),
        sa.UniqueConstraint("movie_id"),
    )
    op.create_table(
        "pay_posters",
        sa.Column("poster_id", sa.Integer(), nullable=False),
        sa.Column("msg", sa.String(length=15), nullable=False),
        sa.Column("movie_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=47), nullable=False),
        sa.Column("type", sa.Integer(), nullable=False),
        sa.Column("aspect", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("poster_id"),
        sa.UniqueConstraint("poster_id"),
    )
    op.create_table(
        "posters",
        sa.Column("poster_id", sa.Integer(), nullable=False),
        sa.Column("msg", sa.String(length=15), nullable=False),
        sa.Column("movie_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=47), nullable=False),
        sa.PrimaryKeyConstraint("poster_id"),
        sa.UniqueConstraint("poster_id"),
    )
    op.create_table(
        "room_menu",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("room_id", sa.Integer(), nullable=True),
        sa.Column("data", models.DictType(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("username", sa.String(length=100), nullable=True),
        sa.Column("password_hash", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "category_movies",
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.Column("movie_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["category_id"],
            ["categories.category_id"],
        ),
        sa.ForeignKeyConstraint(
            ["movie_id"],
            ["movies.movie_id"],
        ),
        sa.PrimaryKeyConstraint("category_id", "movie_id"),
    )
    op.create_table(
        "concierge_miis",
        sa.Column("mii_id", sa.Integer(), nullable=False),
        sa.Column("clothes", sa.Integer(), nullable=False),
        sa.Column("action", sa.Integer(), nullable=False),
        sa.Column("prof", sa.String(length=129), nullable=False),
        sa.Column("movie_id", sa.Integer(), nullable=False),
        sa.Column("voice", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["mii_id"],
            ["mii_data.mii_id"],
        ),
        sa.PrimaryKeyConstraint("mii_id"),
        sa.UniqueConstraint("mii_id"),
    )
    op.create_table(
        "mii_msg_info",
        sa.Column("mii_id", sa.Integer(), nullable=False),
        sa.Column("type", sa.Integer(), nullable=False),
        sa.Column("seq", sa.Integer(), nullable=False),
        sa.Column("msg", sa.String(), nullable=False),
        sa.Column("face", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["mii_id"],
            ["mii_data.mii_id"],
        ),
        sa.PrimaryKeyConstraint("mii_id", "type", "seq"),
    )
    op.create_table(
        "parade_miis",
        sa.Column("mii_id", sa.Integer(), nullable=False),
        sa.Column("logo_id", sa.String(length=5), nullable=False),
        sa.Column("logo_bin", sa.LargeBinary(length=8000), nullable=True),
        sa.Column("mii_msg", sa.String(), nullable=True),
        sa.Column("level", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["mii_id"],
            ["mii_data.mii_id"],
        ),
        sa.PrimaryKeyConstraint("mii_id", "logo_id"),
    )
    op.create_table(
        "rooms",
        sa.Column("room_id", sa.Integer(), nullable=False),
        sa.Column(
            "bgm",
            sa.Enum(
                "SOFT_GUITAR",
                "NORMAL",
                "FOLK",
                "JAZZY",
                "TRUMPET",
                "CHIMES",
                "WESTERN",
                "HARP",
                name="roombgmtypes",
            ),
            nullable=True,
        ),
        sa.Column("mascot", sa.Boolean(), nullable=True),
        sa.Column("contact", sa.Boolean(), nullable=True),
        sa.Column("intro_msg", sa.String(), nullable=True),
        sa.Column("mii_msg", sa.String(), nullable=True),
        sa.Column("logo2_id", sa.String(), nullable=True),
        sa.Column("contact_data", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(
            ["room_id"],
            ["mii_data.mii_id"],
        ),
        sa.PrimaryKeyConstraint("room_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("rooms")
    op.drop_table("parade_miis")
    op.drop_table("mii_msg_info")
    op.drop_table("concierge_miis")
    op.drop_table("category_movies")
    op.drop_table("user")
    op.drop_table("room_menu")
    op.drop_table("posters")
    op.drop_table("pay_posters")
    op.drop_table("pay_movies")
    op.drop_table("pay_category_headers")
    op.drop_table("pay_categories")
    op.drop_table("mii_msg")
    op.drop_table("movies")
    op.drop_table("mii_data")
    op.drop_table("category_pay_movies")
    op.drop_table("categories")
    # ### end Alembic commands ###
