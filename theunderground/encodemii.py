# Encodes images for use in the parade.

import os  # os is used for calling required commands, 'magick', 'base64', 'cat', and 'mv'


def encode(input_file, output):
    """
    encode(input_file,output) -> None
    Arguments:
    input (str): file to encode
    output (str): where to encode it to
    """
    os.system("cat {} | base64 > {}".format(input_file, output))


def resize(input_file, output):
    # DO NOT SET OUTPUT TO .IMG
    # IT WILL **FAIL** AS IT CAN
    # NOT DETERMINE WHAT TO OUTPUT AS!!
    # INSTEAD USE SHUTIL.MOVE!
    os.system(
        "magick convert {} -resize 160x120 -interlace none {}".format(
            input_file, output
        )
    )
