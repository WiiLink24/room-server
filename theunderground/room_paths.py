from theunderground.encodemii import room_tv_encode, room_big_img_encode, vote_picture_encode


def save_delivery_data(
    movie_id: int, movie_data: bytes, image_data: bytes, tv_data: bytes, pic_num: int
):
    movie_dir = "assets/delivery"

    # Write movie
    movie = open(f"{movie_dir}/{movie_id}-H.mov", "wb")
    movie.write(movie_data)
    movie.close()

    # Resize and write thumbnail
    image_data = room_big_img_encode(image_data)
    image = open(f"{movie_dir}/{movie_id}.img", "wb")
    image.write(image_data)
    image.close()

    # Resize and write poster
    tv_data = room_tv_encode(tv_data)
    tv = open(f"assets/special-12/a{pic_num}.img", "wb")
    tv.write(tv_data)
    tv.close()


def save_vote_data(image_data: bytes, image2_data: bytes, image3_data: bytes, tv_data: bytes, pic_num: int):

    # Resize and write poster
    tv_data = room_tv_encode(tv_data)
    tv = open(f"assets/special-12/b{pic_num}.img", "wb")
    tv.write(tv_data)
    tv.close()

    # Resize and write poster
    image_data = vote_picture_encode(image_data)
    image1 = open(f"assets/special-12/e{pic_num}-1.img", "wb")
    image1.write(image_data)
    image1.close()

    # Resize and write poster
    image2_data = vote_picture_encode(image2_data)
    image2 = open(f"assets/special-12/e{pic_num}-2.img", "wb")
    image2.write(image2_data)
    image2.close()

    # Resize and write poster
    image3_data = vote_picture_encode(image3_data)
    image3 = open(f"assets/special-12/e{pic_num}-3.img", "wb")
    image3.write(image3_data)
    image3.close()


def save_mov_data(pic_num: int, tv_data: bytes):
    tv_data = room_tv_encode(tv_data)
    tv = open(f"assets/special-12/c{pic_num}.img", "wb")
    tv.write(tv_data)
    tv.close()


def save_link_data(
    movie_id: int, movie_data: bytes, image1_data: bytes, image2_data: bytes, tv_data: bytes, pic_num: int
):
    movie_dir = "assets/urllink"

    # Write movie
    movie = open(f"{movie_dir}/{movie_id}-H.mov", "wb")
    movie.write(movie_data)
    movie.close()

    # Resize and write thumbnail
    image1_data = room_big_img_encode(image1_data)
    image1 = open(f"{movie_dir}/{movie_id}-1.img", "wb")
    image1.write(image1_data)
    image1.close()

    # Resize and write thumbnail
    image2_data = room_big_img_encode(image2_data)
    image2 = open(f"{movie_dir}/{movie_id}.img", "wb")
    image2.write(image2_data)
    image2.close()

    # Resize and write poster
    tv_data = room_tv_encode(tv_data)
    tv = open(f"assets/special-12/h{pic_num}.img", "wb")
    tv.write(tv_data)
    tv.close()
