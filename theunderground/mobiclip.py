# TODO: Have part of this as its own package with more functionality for usage elsewhere.
# Ensure flask-specific parts are not migrated as well.
import hashlib

import os
from time import gmtime, strftime

from models import Categories, PayCategories
from theunderground.encodemii import (
    movie_thumbnail_encode,
    pay_movie_thumbnail_encode,
    pay_poster_thumbnail_encode,
)


def get_movie_byte(movie_id: int) -> str:
    # We can't hash an integer.
    movie_id = f"{movie_id}"

    # Nintendo takes the MD5 of the ID and uses its first byte.
    hasher = hashlib.md5()
    hasher.update(movie_id.encode("utf-8"))
    resulting_hash = hasher.hexdigest()
    return resulting_hash[:2]


def get_movie_dir(movie_id: int) -> str:
    movie_byte = get_movie_byte(movie_id)
    return f"./assets/movies/{movie_byte}"


def get_pay_movie_dir(movie_id: int) -> str:
    movie_byte = get_movie_byte(movie_id)
    return f"./assets/pay-movie/{movie_byte}"


def validate_mobiclip(file_data: bytes) -> bool:
    # Validate file magic
    return False if file_data[:4] != b"MOC5" else b"KI" in file_data


def get_category_list():
    db_categories = Categories.query.all()

    return [[category.category_id, category.name] for category in db_categories]


def get_pay_category_list():
    db_categories = PayCategories.query.all()

    return [
        [paycategory.category_id, paycategory.name]
        for paycategory in db_categories
    ]


def get_mobiclip_length(file_data: bytes) -> str:
    # We find the FPS at 0xc - 0xf.
    raw_fps = int.from_bytes(file_data[0xC:0xF], byteorder="little")
    # Next, the chunk count is present from 0x10 - 0x13.
    chunk_count = int.from_bytes(file_data[0x10:0x13], byteorder="little")

    # Divide the FPS by 256 to obtain a usable FPS.
    fps = raw_fps / 256

    # As each "chunk" is a frame, we can divide their count by frames,
    # leaving us with length in seconds.
    length = chunk_count / fps

    # Finally, we hope no video over a day long is uploaded.
    return strftime("%H:%M:%S", gmtime(length))


def save_movie_data(movie_id: int, thumbnail_data: bytes, movie_data: bytes):
    movie_dir = get_movie_dir(movie_id)

    # Create the holding assets folder if it does not already exist.
    if not os.path.isdir(movie_dir):
        os.makedirs(movie_dir)

    # Resize and write thumbnail
    thumbnail_data = movie_thumbnail_encode(thumbnail_data)
    with open(f"{movie_dir}/{movie_id}.img", "wb") as thumbnail:
        thumbnail.write(thumbnail_data)
    with open(f"{movie_dir}/{movie_id}-H.mov", "wb") as movie:
        movie.write(movie_data)


def save_pay_movie_data(
    movie_id: int, thumbnail_data: bytes, movie_data: bytes, poster_data: bytes
):
    movie_dir = get_pay_movie_dir(movie_id)

    # Create the holding assets folder if it does not already exist.
    if not os.path.isdir(movie_dir):
        os.makedirs(f"{movie_dir}/{movie_id}")

    # Resize and write thumbnail
    thumbnail_data = pay_movie_thumbnail_encode(thumbnail_data)
    with open(f"{movie_dir}/{movie_id}/D_{movie_id}-1.img", "wb") as thumbnail:
        thumbnail.write(thumbnail_data)
    # Resize and write poster
    poster_data = pay_poster_thumbnail_encode(poster_data)
    with open(f"{movie_dir}/{movie_id}/{movie_id}.img", "wb") as poster:
        poster.write(poster_data)
    with open(f"{movie_dir}/{movie_id}/S_{movie_id}-H.smo", "wb") as movie:
        movie.write(movie_data)


def delete_movie_data(movie_id: int):
    movie_dir = get_movie_dir(movie_id)

    os.remove(f"{movie_dir}/{movie_id}.img")
    os.remove(f"{movie_dir}/{movie_id}-H.mov")


def delete_pay_movie_data(movie_id: int):
    movie_dir = get_pay_movie_dir(movie_id)

    os.remove(f"{movie_dir}/{movie_id}/{movie_id}.img")
    os.remove(f"{movie_dir}/{movie_id}/S_{movie_id}-H.smo")
    os.remove(f"{movie_dir}/{movie_id}/D_{movie_id}-1.img")
