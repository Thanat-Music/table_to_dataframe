import cv2
import numpy as np
import math

#img = cv2.imread("117014.jpg")
img = cv2.imread("cropped.jpg")
scale_percent = 100 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
pos_con = []
list_index = []
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

"""dst = cv2.Canny(gray_img,50,200,None,apertureSize = 3)
cdst = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
cdstP = np.copy(cdst)
lines = cv2.HoughLinesP(dst,1,np.pi/180,150,None,0,0)
if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            cv2.line(cdst, pt1, pt2, (0,0,255), 1, cv2.LINE_AA)
    
linesP = cv2.HoughLinesP(dst, 1, np.pi / 180, 100, None, 50, 10)
    
if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv2.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 1, cv2.LINE_AA)

cv2.imshow('houghlines3',cdstP)"""

ret, threshold_img = cv2.threshold(gray_img, 230, 255, cv2.THRESH_BINARY_INV)
#threshold_img = cv2.adaptiveThreshold(gray_img, 255,
                                      #cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,17,10)
dilation = cv2.dilate(threshold_img, (2, 2), 10)
#dilation = cv2.morphologyEx(threshold_img, cv2.MORPH_GRADIENT, (2, 2))
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
"""count = 0
if (len(contours) > 0):
      areas_con = [cv2.contourArea(c) for c in contours]
      max_index = np.argmax(areas_con)
      cnt = contours[max_index]
      cv2.drawContours(img, [cnt], -1, (0, 255, 0), 3)"""
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
"""while areas_con >= 100:
                  cnt = contours[i]
                  cv2.drawContours(img, [cnt], 0, (0, 255, 0), 1)"""
      
#output = np.concatenate((threshold_img, dilation), axis = 1)
#cv2.imshow("output", output)
