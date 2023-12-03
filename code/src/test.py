import cv2
import numpy as np
import matplotlib.pyplot as plt

# Path to your image
image_path = 'PXL_20231201_190244090.jpg'
crop_percentage = 0.2
threschold = 200

# Read the image
image = cv2.imread(image_path)


img_array = np.array(image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print(gray.shape)


count = 0
count_1 = 0
y_sum = np.zeros(len(gray), dtype=bool)
x_sum = np.zeros(len(gray[0]), dtype=bool)


for i in range(len(gray)):
    for j in range(len(gray[i])):
        if gray[i][j] < threschold:
            gray[i][j] = False
        y_sum[i] += gray[i][j]
        x_sum[j] += gray[i][j]

non_zero_y_sum = [i for i, e in enumerate(y_sum) if e != 0]     #y_sum[y_sum != 0]
non_zero_x_sum = [i for i, e in enumerate(x_sum) if e != 0]     #x_sum[x_sum != 0]


crop_add_val_y = int(crop_percentage * (non_zero_y_sum[len(non_zero_y_sum)-1] - non_zero_y_sum[0]))
crop_add_val_x = int(crop_percentage * (non_zero_x_sum[len(non_zero_x_sum)-1] - non_zero_x_sum[0]))
print(crop_add_val_y, crop_add_val_x)


lower = non_zero_y_sum[0] - crop_add_val_y
upper = non_zero_y_sum[len(non_zero_y_sum)-1] + crop_add_val_y
left_crop = non_zero_x_sum[0] - crop_add_val_x
right_crop = non_zero_x_sum[len(non_zero_x_sum)-1] + crop_add_val_x


fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(x_sum)
axs[1].plot(y_sum)
#plt.show()

cropped_image = gray[lower:upper, left_crop:right_crop]
cv2.imshow('None approximation', cropped_image)
cv2.waitKey(0)

############################

"""
ret, thresh = cv2.threshold(cropped_image, 150, 255, cv2.THRESH_BINARY)
print(thresh.shape)
"""
# detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
contours, hierarchy = cv2.findContours(image=cropped_image, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

# draw contours on the original image
image_copy = image.copy()
image_copy = image_copy[lower:upper, left_crop:right_crop]
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                 lineType=cv2.LINE_AA)
cv2.imshow('None approximation', image_copy)
cv2.waitKey(0)
cv2.imwrite('contours_none_image1.jpg', image_copy)
cv2.destroyAllWindows()

#######################

#cv2.imshow('image', cropped_image)
cv2.waitKey(0)



