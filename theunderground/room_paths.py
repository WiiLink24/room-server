from theunderground.encodemii import (
    room_tv_encode,
    room_big_img_encode,
    vote_picture_encode,
)

from room import s3
from io import BytesIO

import config


def write_to_path(filename: str, data: bytes):
    with open(filename, "wb") as file:
        file.write(data)


def save_delivery_data(
    movie_id: int,
    movie_data: bytes,
    image_data: bytes,
    tv_data: bytes,
    pic_num: int,
    room_id: int,
):
    image_data = room_big_img_encode(image_data)
    tv_data = room_tv_encode(tv_data)

    if s3:
        s3.upload_fileobj(
            BytesIO(movie_data), config.r2_bucket_name, f"delivery/{movie_id}-H.mov"
        )

        s3.upload_fileobj(
            BytesIO(image_data),
            config.r2_bucket_name,
            f"delivery/{movie_id}.img",
            ExtraArgs={"ContentType": "image/jpeg"},
        )

        s3.upload_fileobj(
            BytesIO(tv_data),
            config.r2_bucket_name,
            f"special/{room_id}/img/a{pic_num}.img",
            ExtraArgs={"ContentType": "image/jpeg"},
        )
    else:
        movie_dir = "assets/delivery"

        # Write movie
        write_to_path(f"{movie_dir}/{movie_id}-H.mov", movie_data)

        # Resize and write thumbnail
        write_to_path(f"{movie_dir}/{movie_id}.img", image_data)

        # Resize and write poster
        write_to_path(f"assets/special/{room_id}/a{pic_num}.img", tv_data)


def save_vote_data(
    image_data: bytes,
    image2_data: bytes,
    image3_data: bytes,
    tv_data: bytes,
    pic_num: int,
    room_id: int,
):
    tv_data = room_tv_encode(tv_data)
    image_data = vote_picture_encode(image_data)
    image2_data = vote_picture_encode(image2_data)
    image3_data = vote_picture_encode(image3_data)

    if s3:
        s3.upload_fileobj(
            BytesIO(tv_data),
            config.r2_bucket_name,
            f"special/{room_id}/img/b{pic_num}.img",
            ExtraArgs={"ContentType": "image/jpeg"},
        )

        s3.upload_fileobj(
            BytesIO(image_data),
            config.r2_bucket_name,
            f"special/{room_id}/img/e{pic_num}-1.img",
            ExtraArgs={"ContentType": "image/jpeg"},
        )

        s3.upload_fileobj(
            BytesIO(image2_data),
            config.r2_bucket_name,
            f"special/{room_id}/img/e{pic_num}-2.img",
            ExtraArgs={"ContentType": "image/jpeg"},
        )

        s3.upload_fileobj(
            BytesIO(image3_data),
            config.r2_bucket_name,
            f"special/{room_id}/img/e{pic_num}-3.img",
            ExtraArgs={"ContentType": "image/jpeg"},
        )
    else:
        # Resize and write poster
        write_to_path(f"assets/special/{room_id}/b{pic_num}.img", tv_data)

        # Resize and write poster
        write_to_path(f"assets/special/{room_id}/e{pic_num}-1.img", image_data)

        # Resize and write poster
        write_to_path(f"assets/special/{room_id}/e{pic_num}-2.img", image2_data)

        # Resize and write poster
        write_to_path(f"assets/special/{room_id}/e{pic_num}-3.img", image3_data)


def save_mov_data(pic_num: int, tv_data: bytes, room_id: int):
    tv_data = room_tv_encode(tv_data)

    if s3:
        s3.upload_fileobj(
            BytesIO(tv_data),
            config.r2_bucket_name,
            f"special/{room_id}/img/c{pic_num}.img",
            ExtraArgs={"ContentType": "image/jpeg"},
        )
    else:
        write_to_path(f"assets/special/{room_id}/c{pic_num}.img", tv_data)


def save_link_data(
    movie_id: int,
    movie_data: bytes,
    image1_data: bytes,
    image2_data: bytes,
    tv_data: bytes,
    pic_num: int,
    room_id: int,
):
    image1_data = room_big_img_encode(image1_data)
    image2_data = room_big_img_encode(image2_data)
    tv_data = room_tv_encode(tv_data)
    if s3:
        s3.upload_fileobj(
            BytesIO(movie_data), config.r2_bucket_name, f"urllink/{movie_id}-H.mov"
        )

        s3.upload_fileobj(
            BytesIO(image1_data),
            config.r2_bucket_name,
            f"urllink/{movie_id}-1.img",
            ExtraArgs={"ContentType": "image/jpeg"},
        )

        s3.upload_fileobj(
            BytesIO(image2_data),
            config.r2_bucket_name,
            f"urllink/{movie_id}.img",
            ExtraArgs={"ContentType": "image/jpeg"},
        )

        s3.upload_fileobj(
            BytesIO(tv_data),
            config.r2_bucket_name,
            f"special/{room_id}/img/h{pic_num}.img",
            ExtraArgs={"ContentType": "image/jpeg"},
        )
    else:
        movie_dir = "assets/urllink"

        # Write movie
        write_to_path(f"{movie_dir}/{movie_id}-H.mov", movie_data)

        # Resize and write thumbnail
        write_to_path(f"{movie_dir}/{movie_id}-1.img", image1_data)

        # Resize and write thumbnail
        write_to_path(f"{movie_dir}/{movie_id}.img", image2_data)

        # Resize and write poster
        write_to_path(f"assets/special/{room_id}/h{pic_num}.img", tv_data)


def save_pic_data(
    images_data: list[bytes],
    tv_data: bytes,
    pic_id: int,
    pic_num: int,
    room_id: int,
):
    tv_data = room_tv_encode(tv_data)

    if s3:
        for i, img in enumerate(images_data):
            s3.upload_fileobj(
                BytesIO(room_big_img_encode(img)),
                config.r2_bucket_name,
                f"picture/{pic_id}-{i+1}.img",
                ExtraArgs={"ContentType": "image/jpeg"},
            )

        s3.upload_fileobj(
            BytesIO(tv_data),
            config.r2_bucket_name,
            f"special/{room_id}/img/i{pic_num}.img",
            ExtraArgs={"ContentType": "image/jpeg"},
        )
    else:
        pic_dir = "assets/picture"

        for i, img in enumerate(images_data):
            # Resize and write thumbnail
            write_to_path(f"{pic_dir}/{pic_id}-{i+1}.img", room_big_img_encode(img))

        # Resize and write poster
        write_to_path(f"assets/special/{room_id}/i{pic_num}.img", tv_data)


def save_coupon_data(
    movie_id: int,
    movie_data: bytes,
    image_after_data: bytes,
    tv_data: bytes,
    coupon_data: bytes,
    pic_num: int,
    room_id: int,
):
    image_after_data_enc = room_big_img_encode(image_after_data)
    tv_data = room_tv_encode(tv_data)

    if s3:
        s3.upload_fileobj(
            BytesIO(movie_data), config.r2_bucket_name, f"coupon/{movie_id}-H.mov"
        )

        s3.upload_fileobj(
            BytesIO(image_after_data_enc),
            config.r2_bucket_name,
            f"coupon/{movie_id}-W.img",
            ExtraArgs={"ContentType": "image/jpeg"},
        )

        s3.upload_fileobj(
            BytesIO(tv_data),
            config.r2_bucket_name,
            f"special/{room_id}/img/d{pic_num}.img",
            ExtraArgs={"ContentType": "image/jpeg"},
        )

        s3.upload_fileobj(
            BytesIO(coupon_data),
            config.r2_bucket_name,
            f"coupon/{movie_id}.enc",
        )
    else:
        movie_dir = "assets/coupon"

        # Write movie
        write_to_path(f"{movie_dir}/{movie_id}-H.mov", movie_data)

        # Resize and write thumbnail
        write_to_path(f"{movie_dir}/{movie_id}-W.img", image_after_data_enc)

        # Write coupon
        write_to_path(f"{movie_dir}/{movie_id}.enc", coupon_data)

        # Resize and write poster
        write_to_path(f"assets/special/{room_id}/d{pic_num}.img", tv_data)
