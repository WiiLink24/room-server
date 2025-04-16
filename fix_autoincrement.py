"""
Not a migration however deals with the database.
For certain parts, Wii Room requires ID's to be a specific length.
This script does that.
"""

from sqlalchemy import create_engine, text
import config


def fix_autoincrement():
    engine = create_engine(config.db_url)
    with engine.connect() as conn:
        result = conn.execute(
            text("ALTER SEQUENCE categories_category_id_seq RESTART WITH 10000")
        )
        result.close()

        result = conn.execute(
            text("ALTER SEQUENCE pay_categories_category_id_seq RESTART WITH 20000")
        )
        result.close()

        result = conn.execute(
            text("ALTER SEQUENCE pay_posters_poster_id_seq RESTART WITH 100")
        )
        result.close()


if __name__ == "__main__":
    fix_autoincrement()
