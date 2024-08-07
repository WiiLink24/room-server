"""Add MovieGenres enum

Revision ID: 9c8a56231382
Revises: 9ee9728a92da
Create Date: 2024-06-30 10:31:41.658347

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "9c8a56231382"
down_revision = "9ee9728a92da"
branch_labels = None
depends_on = None


def upgrade():
    # We need some workarounds to cast the integer value to the enum.
    # First drop the null constraint.
    op.alter_column("movies", "genre", existing_type=sa.INTEGER(), nullable=True)

    # Set everything to null
    op.execute(
        """
     UPDATE movies
     SET genre = NULL;
     """
    )

    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("movies", schema=None) as batch_op:
        batch_op.alter_column(
            "genre",
            existing_type=sa.INTEGER(),
            type_=sa.Enum(
                "White", "Gray", "Green", "Orange", "Pink", "Blue", name="moviegenres"
            ),
            existing_nullable=False,
            postgresql_using="genre::text::moviegenres",
        )

    # ### end Alembic commands ###

    op.execute(
        """
     UPDATE movies
     SET genre = 'White';
    """
    )

    # Finally re-add the constraint.
    op.alter_column(
        "movies",
        "genre",
        existing_type=sa.Enum(name="moviegenres"),
        nullable=False,
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("movies", schema=None) as batch_op:
        batch_op.alter_column(
            "genre",
            existing_type=sa.Enum(
                "White", "Gray", "Green", "Orange", "Pink", "Blue", name="moviegenres"
            ),
            type_=sa.INTEGER(),
            existing_nullable=False,
        )

    # ### end Alembic commands ###
