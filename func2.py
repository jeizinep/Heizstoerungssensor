import cv2

#################################GLOBAL VARIABLES#################################
DEBUG = False

DIGITS_LOOKUP = {
	(1, 1, 1, 0, 1, 1, 1): 0,
	(0, 0, 1, 0, 0, 1, 0): 1,
	(1, 0, 1, 1, 1, 0, 1): 2,
	(1, 0, 1, 1, 0, 1, 1): 3,
	(0, 1, 1, 1, 0, 1, 0): 4,
	(1, 1, 0, 1, 0, 1, 1): 5,
	(1, 1, 0, 1, 1, 1, 1): 6,
	(1, 0, 1, 0, 0, 1, 0): 7,
	(1, 1, 1, 1, 1, 1, 1): 8,
	(1, 1, 1, 1, 0, 1, 1): 9,
    (1, 1, 1, 1, 1, 1, 0): 'A',
    (1, 1, 0, 1, 1, 0, 1): 'E',
    (1, 1, 0, 1, 1, 0, 0): 'F',
    (0, 1, 1, 1, 1, 1, 0): 'H',
    (0, 1, 0, 0, 1, 0, 1): 'L'
}


def getPicture(url):
    cap = cv2.VideoCapture()
    cap.open(url)
    ret, image = cap.read()
    cap.release()
    return image

def processPicture(image):
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    clahe_img = clahe.apply(gray)

    #kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (2, 2))
    #thresh = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)

    _, threshold = cv2.threshold(clahe_img, 130, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


    
    prossesedPicture = threshold
    return prossesedPicture, contours

def getDigitsFromPixArr(contours, thresh, image):
    start_index=0
    cropped_binary_matrix = []
    digits = []
    for contour in contours:
            # Find the bounding rectangle for each contour
            x, y, w, h = cv2.boundingRect(contour)
            if(w > 5 and (h > w*1.2)):
                
                start_index += 1


                # Crop the image to the bounding rectangle
                cropped_image = []
                cropped_image = thresh[y:y+h, x:x+w]
                cropped_binary_matrix.append(cropped_image)


                (roiH, roiW) = cropped_image.shape
                (dW, dH) = (int(roiW * 0.4), int(roiH * 0.15))
                dHC = int(roiH * 0.1)
                
                segments = [
                    ((0, 0), (w, dH)),	# top
                    ((int(dW*0.2), dH), (dW, h // 2)),	# top-left
                    ((w - dW + int(dW*0.3), dH), (w, h // 2)),	# top-right
                    ((0, (h // 2) - dHC) , (w, (h // 2) + dHC)), # center
                    ((0, h // 2), (dW, h - dH)),	# bottom-left
                    ((w - dW, h // 2), (w, h - dH)),	# bottom-right
                    ((0, h - dH), (w, h))	# bottom
                ]

                """Original
                segments = [
                    ((0, 0), (w, dH)),	# top
                    ((0, 0), (dW, h // 2)),	# top-left
                    ((w - dW, 0), (w, h // 2)),	# top-right
                    ((0, (h // 2) - dHC) , (w, (h // 2) + dHC)), # center
                    ((0, h // 2), (dW, h)),	# bottom-left
                    ((w - dW, h // 2), (w, h)),	# bottom-right
                    ((0, h - dH), (w, h))	# bottom
                ]
                """
                on = [0] * len(segments)

                



                if(w > h*0.4):
                    for (i, ((xA, yA), (xB, yB))) in enumerate(segments):
                        segROI = cropped_image[yA:yB, xA:xB]
                        
                        total = cv2.countNonZero(segROI)
                        area = (xB - xA) * (yB - yA)
                        if total / float(area) > 0.4:
                            on[i] = 1
                        else:
                            on[i] = 0
                    

                else:
                    on = [0, 0, 1, 0, 0, 1, 0]

                digit = DIGITS_LOOKUP[tuple(on)]
                digits.append(digit)
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
                cv2.putText(image, str(digit), (x - 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 2)


    cv2.imwrite('output/thres.png', thresh)
    cv2.imwrite("output/output.png", image) 
    
    return digits

def get_status(url):
    image_unprocest = getPicture(url)
    image, contours = processPicture(image_unprocest)
    digits = getDigitsFromPixArr(contours, image, image_unprocest)
    return digits