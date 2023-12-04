import cv2

def image_recognition(file_name):
    # Read the image
    image = cv2.imread(file_name)
    image = cv2.resize(image, (0, 0), None, .25, .25)

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
    cropped_binary_matrix = []

    for contour in contours:
        # Find the bounding rectangle for each contour
        x, y, w, h = cv2.boundingRect(contour)

        start_index += 1

        print(x, y, w, h)

        # Crop the image to the bounding rectangle
        cropped_image = image_copy[y:y+h, x:x+h]
        cropped_binary_matrix.append(cropped_image)

        #cv2.rectangle(image_copy, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #save the image
        #cv2.imwrite(f'image{start_index}.png', cropped_image)
        #cv2.imshow('None approximation', cropped_binary_matrix[start_index-1])
        #cv2.waitKey(1000)
    return cropped_binary_matrix