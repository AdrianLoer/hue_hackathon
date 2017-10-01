import base64
from PIL import Image
import cv2
from io import StringIO
import numpy as np

IMAGE_SIZE = (128, 128)

def load_image(base64_string):
    sbuf = StringIO()
    sbuf.write(base64.decodebytes(base64_string))
    pimg = Image.open(sbuf)
    return cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)


def decode_image(bgr_img, running=False):
    img = cv2.resize(bgr_img, IMAGE_SIZE)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    #colors = ['GREEN', 'BLUE', 'RED', 'PINK', 'ORANGE']
    # Color Boundaries BGR
    start_boundaries = ([3, 100, 100], [23, 255, 255]) # Starting color orange
    boundaries = [
        ([22, 100, 100], [42, 255, 255]), # Green
        ([121, 100, 100], [141, 255, 255]), # Blue
        ([165, 100, 100], [185, 255, 255]), # Red
        ([140, 100, 100], [160, 255, 255]) # Ending color Pink
    ]

    # Bit-values:
    # Green: Most Significant Bit
    # Blue : middle Bit
    # Red : Least Significant Bit
    bits = [0] * 4

    # loop over the boundaries

    while not running:
        lower = np.array(start_boundaries[0], dtype="uint8")
        upper = np.array(start_boundaries[1], dtype="uint8")

        mask = cv2.inRange(hsv, lower, upper)
        output = cv2.bitwise_and(img, img, mask=mask)
        gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)

        if cv2.countNonZero(gray)/(IMAGE_SIZE[0]*IMAGE_SIZE[1]) > 0.25:
            print("ORANGE: Start transmission")
            running = True
            return None


    idx = 0
    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(hsv, lower, upper)
        output = cv2.bitwise_and(img, img, mask=mask)
        gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)

        if cv2.countNonZero(gray)/(IMAGE_SIZE[0]*IMAGE_SIZE[1]) > 0.02 and idx < 3:
            bits[idx] = 1
        elif idx == 3 and cv2.countNonZero(gray)/(IMAGE_SIZE[0]*IMAGE_SIZE[1]) > 0.25:
            print("PINK: End transmission!")
            return None

        idx += 1

    return bits

