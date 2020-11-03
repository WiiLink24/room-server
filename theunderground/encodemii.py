# Encodes images for use in the parade.
# TODO: Use a library such as Pillow instead of external calls

import os


def encode(input_file, output):
    """
    encode(input,output) -> None
    Arguments:
    input (str): file to encode
    output (str): where to encode it to
    """
    os.system("cat {} | base64 > {}".format(input, output))


def resize(input_file, output):
    # DO NOT SET OUTPUT TO .IMG
    # IT WILL **FAIL** AS IT CAN
    # NOT DETERMINE WHAT TO OUTPUT AS!!
    # INSTEAD USE SHUTIL.MOVE!
    os.system(
        "magick convert {} -resize 160x120 -interlace none {}".format(input, output)
    )
