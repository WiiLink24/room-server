# TODO: Have part of this as its own package with more functionality for usage elsewhere.
# Ensure flask-specific parts are not migrated as well.
import hashlib

import os
import rsa
from io import BytesIO
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

import config
from time import gmtime, strftime

from room import s3
from models import Categories, PayCategories
from theunderground.encodemii import (
    movie_thumbnail_encode,
    pay_movie_thumbnail_encode,
    pay_poster_thumbnail_encode,
)

from url1.movie_metadata import movie_metadata
from typing import Union

DS_NONCE = b"\x76\xDB\x26\xAE\x09\xBE\x10\x24"
DS_KEY = b"\x37\xF9\x60\x01\x85\xB4\xDC\xEA\x85\x03\x7B\x32\x5D\xAD\xF6\x44"


def get_movie_byte(movie_id: int) -> str:
    # We can't hash an integer.
    movie_id = f"{movie_id}"

    # Nintendo takes the MD5 of the ID and uses its first byte.
    hasher = hashlib.md5()
    hasher.update(movie_id.encode("utf-8"))
    resulting_hash = hasher.hexdigest()
    return resulting_hash[0:2]


def get_movie_path(movie_id: int) -> str:
    movie_byte = get_movie_byte(movie_id)
    if s3:
        return f"movie/{movie_byte}"
    else:
        return f"./assets/movies/{movie_byte}"


def get_ds_movie_path(movie_id: int) -> str:
    movie_byte = get_movie_byte(movie_id)
    if s3:
        return f"dsmov/{movie_byte}"
    else:
        return f"./assets/dsmov/{movie_byte}"


def get_pay_movie_dir(movie_id: int) -> str:
    movie_byte = get_movie_byte(movie_id)
    return f"./assets/pay-movie/{movie_byte}"


def validate_mobiclip(file_data: bytes) -> bool:
    # Validate file magic
    if file_data[0:4] != b"MOC5":
        return False

    # Ensure we have a valid keyframe index.
    if b"KI" not in file_data:
        return False

    return True


def validate_mobi_dsi(file_data: bytes) -> Union[bool, bytes]:
    # Validate file magic
    if file_data[0:4] == b"MODS":
        # Encrypt the data into the SSCF container
        data = b"SSCF"
        data += b"\x00" * 4
        # Movie size
        data += len(file_data).to_bytes(4, "little")
        # Movie offset
        data += (200).to_bytes(2, "little")
        # IV offset relative to end of header
        data += b"\x00\x00"
        # NINTENDO for some reason
        data += b"NINTENDO"
        # 40 null bytes
        data += b"\x00" * 40
        # RSA signature gets placed here after
        data += b"\x00" * 128
        # IV
        data += DS_NONCE

        with open(config.ds_rsa_key_path, "rb") as f:
            private_key = rsa.PrivateKey.load_pkcs1(f.read(), "PEM")
            signature = rsa.sign(data, private_key, "SHA-1")

        # Now write the signature to the container.
        data = data[:64]
        data += signature
        data += DS_NONCE

        # Next step is to encrypt the movie with AES-128-CTR.
        # Although CTR doesn't require the data to be block size, Nintendo does.
        cipher = AES.new(DS_KEY, AES.MODE_CTR, nonce=DS_NONCE)
        data += cipher.encrypt(pad(file_data, AES.block_size))
        return data
    elif file_data[0:4] == b"SSCF":
        # Check for NINTENDO header
        if file_data[17:25] != b"NINTENDO":
            return False
    else:
        return False

    return True


def get_category_list():
    db_categories = Categories.query.all()

    choice_categories = []
    for _, category in enumerate(db_categories):
        choice_categories.append([category.category_id, category.name])

    return choice_categories


def get_pay_category_list():
    db_categories = PayCategories.query.all()

    choice_categories = []
    for _, paycategory in enumerate(db_categories):
        choice_categories.append([paycategory.category_id, paycategory.name])

    return choice_categories


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


def save_movie_data(
    movie_id: int, thumbnail_data: bytes, movie_data: bytes, ds_movie_data: bytes = None
):
    movie_dir = get_movie_path(movie_id)
    ds_movie_dir = get_ds_movie_path(movie_id)
    md5_hash = get_movie_byte(movie_id)

    if s3:
        # Upload movie
        if movie_data:
            movie_path = f"{movie_dir}/{movie_id}-H.mov"
            s3.upload_fileobj(BytesIO(movie_data), config.r2_bucket_name, movie_path)

        # Metadata XML
        met_xml = movie_metadata(md5_hash, movie_id)
        met_path = f"{movie_dir}/{movie_id}.met"
        s3.upload_fileobj(BytesIO(met_xml), config.r2_bucket_name, met_path)

        # Thumbnail
        if thumbnail_data:
            thumbnail_data = movie_thumbnail_encode(thumbnail_data)
            thumbnail_path = f"{movie_dir}/{movie_id}.img"
            s3.upload_fileobj(
                BytesIO(thumbnail_data), config.r2_bucket_name, thumbnail_path
            )

        if ds_movie_data:
            # Upload DS movie
            ds_movie_path = f"{ds_movie_dir}/{movie_id}.enc"
            s3.upload_fileobj(
                BytesIO(ds_movie_data), config.r2_bucket_name, ds_movie_path
            )
    else:
        if not os.path.isdir(movie_dir):
            os.makedirs(movie_dir)

        if thumbnail_data:
            # Resize and write thumbnail
            thumbnail_data = movie_thumbnail_encode(thumbnail_data)
            thumbnail = open(f"{movie_dir}/{movie_id}.img", "wb")
            thumbnail.write(thumbnail_data)
            thumbnail.close()

        if movie_data:
            # Write movie
            movie = open(f"{movie_dir}/{movie_id}-H.mov", "wb")
            movie.write(movie_data)
            movie.close()

        if ds_movie_data:
            if not os.path.isdir(ds_movie_dir):
                os.makedirs(ds_movie_dir)

            # Write DS movie
            ds_movie = open(f"{ds_movie_dir}/{movie_id}.enc", "wb")
            ds_movie.write(ds_movie_data)
            ds_movie.close()


def save_pay_movie_data(
    movie_id: int, thumbnail_data: bytes, movie_data: bytes, poster_data: bytes
):
    movie_dir = get_pay_movie_dir(movie_id)

    # Create the holding assets folder if it does not already exist.
    if not os.path.isdir(movie_dir):
        os.makedirs(f"{movie_dir}/{movie_id}")

    # Resize and write thumbnail
    thumbnail_data = pay_movie_thumbnail_encode(thumbnail_data)
    thumbnail = open(f"{movie_dir}/{movie_id}/D_{movie_id}-1.img", "wb")
    thumbnail.write(thumbnail_data)
    thumbnail.close()

    # Resize and write poster
    poster_data = pay_poster_thumbnail_encode(poster_data)
    poster = open(f"{movie_dir}/{movie_id}/{movie_id}.img", "wb")
    poster.write(poster_data)
    poster.close()

    # Write movie
    movie = open(f"{movie_dir}/{movie_id}/S_{movie_id}-H.smo", "wb")
    movie.write(movie_data)
    movie.close()


def delete_movie_data(movie_id: int, ds_movie: bool):
    movie_dir = get_movie_path(movie_id)
    if ds_movie:
        ds_movie_dir = get_ds_movie_path(movie_id)

    if s3:
        s3.delete_object(
            Bucket=config.r2_bucket_name, Key=f"{movie_dir}/{movie_id}.img"
        )
        s3.delete_object(
            Bucket=config.r2_bucket_name, Key=f"{movie_dir}/{movie_id}-H.mov"
        )
        s3.delete_object(
            Bucket=config.r2_bucket_name, Key=f"{movie_dir}/{movie_id}.met"
        )
        if ds_movie:
            s3.delete_object(
                Bucket=config.r2_bucket_name, Key=f"{ds_movie_dir}/{movie_id}.enc"
            )
    else:
        os.remove(f"{movie_dir}/{movie_id}.img")
        os.remove(f"{movie_dir}/{movie_id}-H.mov")
        if ds_movie:
            os.remove(f"{ds_movie_dir}/{movie_id}.enc")


def delete_pay_movie_data(movie_id: int):
    movie_dir = get_pay_movie_dir(movie_id)

    os.remove(f"{movie_dir}/{movie_id}/{movie_id}.img")
    os.remove(f"{movie_dir}/{movie_id}/S_{movie_id}-H.smo")
    os.remove(f"{movie_dir}/{movie_id}/D_{movie_id}-1.img")
