from PIL import Image
import pytesseract
import cv2
import argparse
import os

# Constructing argument parse and parsing the arguements

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
    help="path to input image to be OCR'd"
)
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
    help="type of preprocessing to be done"
)
args=vars(ap.parse_args())


# Load image and convert it into grayscale

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)