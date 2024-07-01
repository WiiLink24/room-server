import io

from PIL import Image, ImageFile


def movie_thumbnail_encode(infile: bytes) -> bytes:
    return generic_encode(infile, 160, 120)


def pay_movie_thumbnail_encode(infile: bytes) -> bytes:
    return generic_encode(infile, 832, 456)


def pay_poster_thumbnail_encode(infile: bytes) -> bytes:
    return generic_encode(infile, 320, 456)


def room_tv_encode(infile: bytes) -> bytes:
    return generic_encode(infile, 160, 120)


def room_big_img_encode(infile: bytes) -> bytes:
    return generic_encode(infile, 832, 456)


def vote_picture_encode(infile: bytes) -> bytes:
    return generic_encode(infile, 168, 128)


def generic_encode(in_bytes: bytes, w: int, h: int) -> bytes:
    """Encodes an image to a format suitable for the Wii."""
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    im = Image.open(io.BytesIO(in_bytes))

    # If we have an alpha channel, it must be removed.
    if im.mode in ("RGBA", "P"):
        im = im.convert("RGB")

    im = im.resize((w, h))

    result = io.BytesIO()
    # These defaults are required for the Wii to read an JPEG.
    im.save(result, "jpeg", subsampling="4:2:0", progressive=False)

    return result.getvalue()


def encode_mii_category(mii: bytes) -> bytes:
    dim = (160, 120)
    rgb = (253, 246, 178)
    base = Image.new("RGB", dim, rgb)

    mii_img = Image.open(io.BytesIO(mii))
    mii_img = mii_img.resize((140, 140))

    # Calculate the position to paste the PNG in the center
    base_width, base_height = base.size
    mii_width, mii_height = mii_img.size

    x = (base_width - mii_width) // 2
    y = (base_height - mii_height) // 2

    # Paste the PNG onto the base image
    base.paste(mii_img, (x, y), mii_img)

    result = io.BytesIO()
    base.save(result, "jpeg", subsampling="4:2:0", progressive=False)

    return result.getvalue()
