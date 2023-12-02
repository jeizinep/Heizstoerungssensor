import cv2
import time
import numpy as np

pervious_time = time.time()

# Read the image
while True:
    image = cv2.imread('Screenshot 2023-12-01 195102.png')
    image = cv2.resize(image, (0, 0), fx=0.2, fy=0.2)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a threshold to get the specific lighting distribution
    _, threshold = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)

    # Find the contours of the thresholded image
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    image_copy = image.copy()

    cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    cv2.imshow('None approximation', image_copy)
    cv2.waitKey(0)
    print(time.time() - pervious_time)
    pervious_time = time.time()





"""
# Iterate over each contour
for contour in contours:
    # Find the bounding rectangle for each contour
    x, y, w, h = cv2.boundingRect(contour)

    image_copy = image.copy()

    # Draw contours on cropped image
    image_copy = image_copy[y:y+h, x:x+w]
"""