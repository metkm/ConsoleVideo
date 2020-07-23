import cv2
import numpy
import sys
import time
from PIL import Image

thresh = 70
TIMEOUT = .0416

print("don't forget to add extension of video like mp4")
videon_name = input("Video Name: ")

vidcap = cv2.VideoCapture(videon_name)
success, image = vidcap.read()


def fn(x):
    if x > thresh:
        return 255
    return 0


old_timestamp = time.time()
while success:

    if (time.time() - old_timestamp) > TIMEOUT:
        img = Image.fromarray(image)
        img.thumbnail((50, 50))
        r = img.convert('L').point(fn, mode="1")

        pixels = r.load()
        image_size = r.size

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

        old_timestamp = time.time()
        print(star_string)

        success, image = vidcap.read()
