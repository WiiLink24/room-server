from theunderground.encodemii import room_tv_encode, room_big_img_encode


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
