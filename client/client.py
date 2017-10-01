import image_decoder
import re
import cv2
import queue
import os


message = []
frames = queue.Queue()

images_path = "/home/rob/workspace/Hue_hackerthon/client/images/"

images = [os.path.join(images_path, f) for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))]

def reconstruct_message(bits):
    message.extend(bits)
    print(message)

def receive_data(images):
    running = False
    for i in images:
        bgr_image = cv2.imread(i)
        print(i)
        bits = image_decoder.decode_image(bgr_image, running)
        if bits:
            reconstruct_message(bits[:3])
        else:
            running = True
        print(message)


if __name__ == "__main__":
    images_ordered = sorted(images, key=lambda x: (int(re.sub('\D', '', x)), x))
    receive_data(images_ordered)