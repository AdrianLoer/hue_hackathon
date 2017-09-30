import image_decoder
import cv2

message = []


def reconstruct_message(bits):
    message.extend(bits)
    print(message)


def receive_data(base64_string):
    #bgr_image = image_decoder.load_image(base64_string)
    bgr_image = cv2.imread("/home/rob/Dropbox/Innohacks/IMG_20170930_221227.jpg")
    bits = image_decoder.decode_image(bgr_image)
    reconstruct_message(bits)


if __name__ == "__main__":
    bgr_image = cv2.imread("/home/rob/Dropbox/Innohacks/IMG_20170930_223929.jpg")
    bits = image_decoder.decode_image(bgr_image)
    reconstruct_message(bits)