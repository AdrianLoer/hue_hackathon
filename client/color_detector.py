import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to the image")
args = vars(ap.parse_args())


img = cv2.imread(args["image"], cv2.IMREAD_COLOR)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Color Boundaries BGR
boundaries = [
    ([165, 100, 100], [185, 255, 255]), # Red
    ([22, 100, 100], [42, 255, 255]), # Green
    ([121, 100, 100], [141, 255, 255]), # Blue
]

# loop over the boundaries
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(img, img, mask=mask)

    # show the images
    cv2.namedWindow("images", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("images", 1024, 768)
    cv2.imshow("images", np.hstack([img, output]))
    cv2.waitKey(0)
