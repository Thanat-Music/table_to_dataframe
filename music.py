import cv2
import numpy as np
import math

#img = cv2.imread("117014.jpg")

img = cv2.imread("table1.jpg")

scale_percent = 100 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

pos_con = []
list_index = []

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, threshold_img = cv2.threshold(gray_img, 230, 255, cv2.THRESH_BINARY)
kernel = np.ones((2,2))
erodesion = cv2.erode(threshold_img,kernel,iterations = 2)
ret, threshold_img = cv2.threshold(erodesion, 230, 255, cv2.THRESH_BINARY_INV)
#threshold_img = cv2.adaptiveThreshold(gray_img, 255,
                                      #cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,17,10)
dilation = cv2.dilate(threshold_img, (2, 2), 10)
#dilation = cv2.morphologyEx(threshold_img, cv2.MORPH_GRADIENT, (2, 2))
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

count = 0
for i, cnt in enumerate(contours):
      areas_con = cv2.contourArea(cnt)
      x, y, w, h = cv2.boundingRect(cnt)
      pos_con.append((x, y, w, h))
      if areas_con < 11000 and areas_con > 3000:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            list_index.append(i)
            count += 1
print(count)
print(list_index)
cv2.imshow("output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
#output = np.concatenate((threshold_img, dilation), axis = 1)
#cv2.imshow("output", output)
