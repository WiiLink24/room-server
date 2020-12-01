# Encodes images
from PIL import Image
import base64
from os import remove


def parade_encode(infile):
    size = 184, 80
    im = Image.open(infile)
    im = im.resize(size)
    im.save("temp.jpg", "JPEG")
    encodemii = open("temp.jpg", "wb")
    data = base64.b64encode(encodemii.read())
    encodemii.close()
    remove("temp.jpg")
