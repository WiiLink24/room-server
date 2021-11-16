from theunderground.encodemii import (
    room_tv_encode,
    room_big_img_encode,
    vote_picture_encode,
)


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
    movie_dir = "assets/delivery"

    # Write movie
    write_to_path(f"{movie_dir}/{movie_id}-H.mov", movie_data)

    # Resize and write thumbnail
    image_data = room_big_img_encode(image_data)
    write_to_path(f"{movie_dir}/{movie_id}.img", image_data)

    # Resize and write poster
    tv_data = room_tv_encode(tv_data)
    write_to_path(f"assets/special/{room_id}/a{pic_num}.img", tv_data)


def save_vote_data(
    image_data: bytes,
    image2_data: bytes,
    image3_data: bytes,
    tv_data: bytes,
    pic_num: int,
    room_id: int,
):
    # Resize and write poster
    tv_data = room_tv_encode(tv_data)
    write_to_path(f"assets/special/{room_id}/b{pic_num}.img", tv_data)

    # Resize and write poster
    image_data = vote_picture_encode(image_data)
    write_to_path(f"assets/special/{room_id}/e{pic_num}-1.img", image_data)

    # Resize and write poster
    image2_data = vote_picture_encode(image2_data)
    write_to_path(f"assets/special/{room_id}/e{pic_num}-2.img", image2_data)

    # Resize and write poster
    image3_data = vote_picture_encode(image3_data)
    write_to_path(f"assets/special/{room_id}/e{pic_num}-3.img", image3_data)


def save_mov_data(pic_num: int, tv_data: bytes, room_id: int):
    tv_data = room_tv_encode(tv_data)
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
    movie_dir = "assets/urllink"

    # Write movie
    write_to_path(f"{movie_dir}/{movie_id}-H.mov", movie_data)

    # Resize and write thumbnail
    image1_data = room_big_img_encode(image1_data)
    write_to_path(f"{movie_dir}/{movie_id}-1.img", image1_data)

    # Resize and write thumbnail
    image2_data = room_big_img_encode(image2_data)
    write_to_path(f"{movie_dir}/{movie_id}.img", image2_data)

    # Resize and write poster
    tv_data = room_tv_encode(tv_data)
    write_to_path(f"assets/special/{room_id}/h{pic_num}.img", tv_data)


def save_pic_data(
    image1_data: bytes,
    image2_data: bytes,
    image3_data: bytes,
    tv_data: bytes,
    pic_id: int,
    pic_num: int,
    room_id: int,
):
    pic_dir = "assets/picture"

    # Resize and write thumbnail
    image1_data = room_big_img_encode(image1_data)
    write_to_path(f"{pic_dir}/{pic_id}-1.img", image1_data)

    image2_data = room_big_img_encode(image2_data)
    write_to_path(f"{pic_dir}/{pic_id}-2.img", image2_data)

    image3_data = room_big_img_encode(image3_data)
    write_to_path(f"{pic_dir}/{pic_id}-3.img", image3_data)

    # Resize and write poster
    tv_data = room_tv_encode(tv_data)
    write_to_path(f"assets/special/{room_id}/i{pic_num}.img", tv_data)
