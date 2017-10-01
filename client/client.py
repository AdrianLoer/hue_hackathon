import image_decoder
import re
import cv2
import queue
import os


message = []
frames = queue.Queue()

images_path = "/home/rob/workspace/Hue_hackerthon/client/images/"

images = [os.path.join(images_path, f) for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))]

def decode(bitArray):
    s = ""
    bitBuffer = ""
    for i in range(len(bitArray), 0, -7):
        bitBuffer = bitArray[i-7:i]
        x = "".join([str(x) for x in bitBuffer])
        try:
            s = chr(int(x, 2)) + s
        except:
            pass
    return s

def reconstruct_message(bits):
    message.extend(bits)

def receive_data(images):
    running = False
    for i in images:
        bgr_image = cv2.imread(i)
        bits = image_decoder.decode_image(bgr_image, running)
        if bits:
            reconstruct_message(bits[:3])
            print(bits[:3])
        else:
            running = True

if __name__ == "__main__":
    images_ordered = sorted(images, key=lambda x: (int(re.sub('\D', '', x)), x))
    receive_data(images_ordered)
    print(message)
    print(decode(message))