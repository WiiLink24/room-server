import base64
import io

from PIL import Image


def room_logo(infile: bytes) -> bytes:
    return generic_encode(infile, 320, 180)


def parade_encode(infile: bytes) -> bytes:
    return generic_encode(infile, 184, 80)


def movie_thumbnail_encode(infile: bytes) -> bytes:
    return generic_encode(infile, 160, 120)


def pay_movie_thumbnail_encode(infile: bytes) -> bytes:
    return generic_encode(infile, 832, 456)


def pay_poster_thumbnail_encode(infile: bytes) -> bytes:
    return generic_encode(infile, 320, 456)


def category_encode(infile: bytes) -> bytes:
    return generic_encode(infile, 160, 120)


def room_tv_encode(infile: bytes) -> bytes:
    return generic_encode(infile, 160, 120)


def room_big_img_encode(infile: bytes) -> bytes:
    return generic_encode(infile, 832, 456)


def vote_picture_encode(infile: bytes) -> bytes:
    return generic_encode(infile, 168, 128)


def generic_encode(in_bytes: bytes, w: int, h: int) -> bytes:
    """Encodes an image to a format suitable for the Wii."""
    im = Image.open(io.BytesIO(in_bytes))

    # If we have an alpha channel, it must be removed.
    if im.mode in ("RGBA", "P"):
        im = im.convert("RGB")

    im = im.resize((w, h))

    result = io.BytesIO()
    # These defaults are required for the Wii to read an JPEG.
    im.save(result, "jpeg", subsampling="4:2:0", progressive=False)

    return result.getvalue()
