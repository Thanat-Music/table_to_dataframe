import cv2
import numpy as np

def box_cut(values):
      dtype = [('x', int), ('y', int), ('w', int), ('h', int)]
      box_array = np.array(values, dtype = dtype)
      sort_box_array = np.sort(box_array, order = 'x')
      for position in sort_box_array:
            x, y, w, h = position
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.imshow('img', img)
            bg_img = np.zeros((img.shape[0], img.shape[1]))
            bg_img[y:y+h, x:x+w] = 1
            img_cut = img_copy[y:y+h, x:x+w,:]
            pos_con.append(img_cut)
            cv2.waitKey(1000)
      return pos_con

pos_con = []
bitw_img = []
keep_monday = []
keep_tuesday = []
keep_wednesday = []
keep_thursday = []
keep_friday = []
keep_box_monday = []
keep_box_tuesday = []
keep_box_wednesday = []
keep_box_thursday = []
keep_box_friday = []

img = cv2.imread("cropped.jpg")
scale_percent = 100
width = int(img.shape[1] * scale_percent / 100)
hight = int(img.shape[0] * scale_percent / 100)
dim = (width, hight)
img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
img_copy = img.copy()
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshold_img = cv2.adaptiveThreshold(gray_img, 255,
                                      cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,29,0)
dilation = cv2.dilate(threshold_img, (2, 2), 10)
contours, hierarchy = cv2.findContours(dilation, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
contours = np.flip(contours, 0)
count = 0
if (len(contours) > 0):
      for i, con in enumerate(contours):
            areas_con = cv2.contourArea(con)
            x, y, w, h = cv2.boundingRect(con)
            if areas_con < 11000 and areas_con > 3000:
                  print("index : {0} ==> area_con = {1}".format(i, areas_con))
                  if (y>68) and (y<156):
                        #cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
                        keep_monday.append(x)
                        keep_box_monday.append((x, y, w, h))
                  elif (y>156) and (y<244):
                        #cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        keep_tuesday.append(x)
                        keep_box_tuesday.append((x, y, w, h))
                  elif (y>244) and (y<332):
                        #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
                        keep_wednesday.append(x)
                        keep_box_wednesday.append((x, y, w, h))
                  elif (y>332) and (y<420):
                        #cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)
                        keep_thursday.append(x)
                        keep_box_thursday.append((x, y, w, h))
                  else:
                        #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
                        keep_friday.append(x)
                        keep_box_friday.append((x, y, w, h))
                  count += 1
      keep_day = [keep_monday,
                              keep_tuesday,
                              keep_wednesday,
                              keep_thursday,
                              keep_friday]
      keep_box = {'monday': keep_box_monday,
                              'tuesday':keep_box_tuesday,
                              'wednesday':keep_box_wednesday,
                              'thursday':keep_box_thursday,
                              'friday':keep_box_friday}
      for day, row_day in keep_box.items():
             print("day = {}".format(day))
             img_append = box_cut(row_day)

for j in range(len(img_append)):
      img_j = img_append[j]

print("number of contours in condition is : {}".format(count))
cv2.waitKey(0)
cv2.destroyAllWindows()
