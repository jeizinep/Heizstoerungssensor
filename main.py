import time
import timeit
import cv2



def image_recognition(file_name, start_index):
    # Read the image
    #image = cv2.imread(file_name)
    image = cv2.resize(file_name, (0, 0), None, .25, .25)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    clahe_img = clahe.apply(gray)

    # Apply a threshold to get the specific lighting distribution
    _, threshold = cv2.threshold(clahe_img, 230, 255, cv2.THRESH_BINARY)

    # Find the contours of the thresholded image
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    image_copy = threshold.copy()

    start_index=0

    for contour in contours:
        # Find the bounding rectangle for each contour
        x, y, w, h = cv2.boundingRect(contour)

        start_index += 1

        print(x, y, w, h)

        # Crop the image to the bounding rectangle
        cropped_image = image_copy[y:y+h, x:x+h]

        #cv2.rectangle(image_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #save the image
        #cv2.imwrite(f'image{start_index}.png', cropped_image)
        cv2.imshow('None approximation', cropped_image)
        cv2.waitKey(100)


Images = ['PXL_20231201_190244090.jpg']
name = 0

cap = cv2.VideoCapture(0)
print(cap)

#for i in Images:
while True:
    ret, frame = cap.read()
    name += 1
    t = timeit.Timer(lambda: image_recognition(frame, (name - 1)))
    print(t.timeit(number=1))
