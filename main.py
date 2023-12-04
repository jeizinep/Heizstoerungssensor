import time
import timeit
import cv2
import numpy as np
from imageprocessing import image_recognition
from charactermatching import find_character

def square_define(input_image, digit_index, centerpoint_percentage_square_x, centerpoint_percentage_square_y, square_size_percentage_x=5, square_size_percentage_y=5):
    segments = [0 for i in range(7)]
    center_row = len(input_image[digit_index]) * centerpoint_percentage_square_x // 100
    center_col = len(input_image[digit_index][center_row]) * centerpoint_percentage_square_y // 100

    # Calculate 5% of the image's width and height
    offset_row = len(input_image[digit_index]) * square_size_percentage_x // 100
    offset_col = len(input_image[digit_index][center_row]) * square_size_percentage_y // 100

    # Calculate the start and end indices for rows and columns
    start_row = max(0, center_row - offset_row)
    end_row = min(len(input_image[digit_index]), center_row + offset_row)
    start_col = max(0, center_col - offset_col)
    end_col = min(len(input_image[digit_index][center_row]), center_col + offset_col)

    # Get the square region around the center pixel
    square_region = input_image[digit_index][start_row:end_row, start_col:end_col]/255

    # Now you can perform any operations on this square region
    # For example, print its shape
    return square_region

def segment_recognition(cropped_binary_image, theshold_percentage=50):
    segment = np.full(7, None, dtype=object)
    segments = []
    for i in range(len(cropped_binary_image)):
        segment_copy = segment.copy()
        segment_copy[0] = square_define(cropped_binary_image, i, 50, 10 , 3, 3)
        segment_copy[1] = square_define(cropped_binary_image, i, 75, 25 , 3, 3)
        segment_copy[2] = square_define(cropped_binary_image, i, 75, 75 , 3, 3)
        segment_copy[3] = square_define(cropped_binary_image, i, 50, 90 , 3, 3)
        segment_copy[4] = square_define(cropped_binary_image, i, 25, 75 , 3, 3)
        segment_copy[5] = square_define(cropped_binary_image, i, 25, 25 , 3, 3)
        segment_copy[6] = square_define(cropped_binary_image, i, 50, 50 , 3, 3)
        mean = [np.mean(matrix) for matrix in segment_copy]
        res = [1 if mean[i] > (theshold_percentage // 100) else 0 for i in range(len(mean))]
        segments.append(res)
        print(mean)
        print(segment_copy)
        print(np.sum(segment_copy))
    print(segments)

    return segments

if __name__ == "__main__":
    processed_image = image_recognition('PXL_20231201_190244090.jpg')
    segment_array = segment_recognition(processed_image)
    characters = find_character(segment_array)
    print(characters)



"""
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
"""