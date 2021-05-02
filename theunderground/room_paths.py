from theunderground.encodemii import (
    room_tv_encode,
    room_big_img_encode,
    vote_picture_encode,
)


def write_to_path(filename: str, data: bytes):
    with open(filename, "wb") as file:
        file.write(data)


def save_delivery_data(
    movie_id: int, movie_data: bytes, image_data: bytes, tv_data: bytes, pic_num: int
):
    movie_dir = "assets/delivery"

    # Write movie
    write_to_path(f"{movie_dir}/{movie_id}-H.mov", movie_data)

    # Resize and write thumbnail
    image_data = room_big_img_encode(image_data)
    write_to_path(f"{movie_dir}/{movie_id}.img", image_data)

    # Resize and write poster
    tv_data = room_tv_encode(tv_data)
    write_to_path(f"assets/special-12/a{pic_num}.img", tv_data)


def save_vote_data(
    image_data: bytes,
    image2_data: bytes,
    image3_data: bytes,
    tv_data: bytes,
    pic_num: int,
):

    # Resize and write poster
    tv_data = room_tv_encode(tv_data)
    write_to_path(f"assets/special-12/b{pic_num}.img", tv_data)

    # Resize and write poster
    image_data = vote_picture_encode(image_data)
    write_to_path(f"assets/special-12/e{pic_num}-1.img", image_data)

    # Resize and write poster
    image2_data = vote_picture_encode(image2_data)
    write_to_path(f"assets/special-12/e{pic_num}-2.img", image2_data)

    # Resize and write poster
    image3_data = vote_picture_encode(image3_data)
    write_to_path(f"assets/special-12/e{pic_num}-3.img", image3_data)


def save_mov_data(pic_num: int, tv_data: bytes):
    tv_data = room_tv_encode(tv_data)
    write_to_path(f"assets/special-12/c{pic_num}-1.img", tv_data)


def save_link_data(
    movie_id: int,
    movie_data: bytes,
    image1_data: bytes,
    image2_data: bytes,
    tv_data: bytes,
    pic_num: int,
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
    write_to_path(f"assets/special-12/h{pic_num}.img", tv_data)
