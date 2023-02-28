# from main import *
# importing required libraries of opencv
import cv2

# importing library for plotting
from matplotlib import pyplot as plt

def histogram(img_file):
    # reads an input image
    img = cv2.imread(img_file,0)

    # find frequency of pixels in range 0-255
    histr = cv2.calcHist([img], [0], None, [256], [0, 256])

    # show the plotting graph of an image
    plt.plot(histr)
    plt.show()
