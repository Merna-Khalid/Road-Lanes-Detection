import cv2
import numpy as np
import matplotlib.pyplot as plt

# image from cv2.imread
def cannyEdgeDetection(image):
	gray = cv2.cvtColor(image, cv2.COLOR_RBG2GRAY)
	#blur = cv2.GaussianBlur(gray, (5,5), 0)
	canny = cv2.Canny(gray, 50, 150)