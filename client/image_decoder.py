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


def decode_image(bgr_img):
    img = cv2.resize(bgr_img, IMAGE_SIZE)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    colors = ['GREEN', 'BLUE', 'RED']
    # Color Boundaries BGR
    boundaries = [
        ([22, 100, 100], [42, 255, 255]), # Green
        ([121, 100, 100], [141, 255, 255]), # Blue
        ([165, 100, 100], [185, 255, 255]), # Red
    ]

    # Bit-values:
    # Green: Most Significant Bit
    # Blue : middle Bit
    # Red : Least Significant Bit
    bits = [0] * 3

    # loop over the boundaries
    idx = 0
    for (lower, upper) in boundaries:
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(hsv, lower, upper)
        output = cv2.bitwise_and(img, img, mask=mask)
        gray = cv2.cvtColor(output, cv2.COLOR_BGR2GRAY)
        if cv2.countNonZero(gray)/(IMAGE_SIZE[0]*IMAGE_SIZE[1]) > 0.01:
            bits[idx] = 1

        # show the images
        cv2.namedWindow("{}-image".format(colors[idx]), cv2.WINDOW_NORMAL)
        cv2.resizeWindow("{}-image".format(colors[idx]), 1024, 768)
        cv2.imshow("{}-image".format(colors[idx]), np.hstack([img, output]))
        idx += 1
        cv2.waitKey(0)
        print(bits)




if __name__ == '__main__':
    load_image()
