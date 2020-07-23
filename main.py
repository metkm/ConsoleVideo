import cv2
import numpy
import sys
import time
from PIL import Image

videon_name = input("Video Name: ")
print("don't forget to add extension of vide")
vidcap = cv2.VideoCapture(videon_name)

success, image = vidcap.read()
numpy.set_printoptions(threshold=sys.maxsize)
thresh = 70

while success:
    img = Image.fromarray(image)
    img.thumbnail((50, 50))
    fn = lambda x: 255 if x > thresh else 0
    r = img.convert('L').point(fn, mode='1')

    pixels = r.load()
    image_size = r.size

    row_count = 0
    star_string = ""
    for height in range(image_size[1]):
        for width in range(image_size[0]):
            pixel = pixels[width, height]
            if not pixel == 255:
                star_string += "*"
                continue
            else:
                star_string += " "
        star_string += "\n"
    print(star_string)
    time.sleep(0.0145)

    success, image = vidcap.read()
