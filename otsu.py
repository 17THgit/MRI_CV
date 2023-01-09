#dicom image threshold=15 & min enclosing circle
import pydicom
import numpy as np
import cv2
import matplotlib.pyplot as plt

ct_filepath = '/Users/TH/Desktop/T1/i6812124.MRDC.1'
ct_dicom = pydicom.read_file(ct_filepath)
img = ct_dicom.pixel_array
img_2d = img.astype(float)
img_2d_scaled = (np.maximum(img_2d,0) / img_2d.max()) * 255.0   #grayscale

img_2d_scaled = np.uint8(img_2d_scaled)

#threshold 15
ret_thresh, thresh_result = cv2.threshold(img_2d_scaled, 15, 255, cv2.THRESH_BINARY)

plt.imshow(thresh_result, cmap='gray')
plt.show()

#contour
ret, imthres = cv2.threshold(thresh_result, 127, 255, cv2.THRESH_BINARY_INV)
contour, hierarchy = cv2.findContours(imthres, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# 모든 좌표를 갖는 컨투어 그리기
#cv2.drawContours(img_2d_scaled, contour, -1, (255,255,255), 1)

# min Enclosing Circle 그리기
for i in range(len(contour)):
    contr = contour[i]
    (x,y), radius = cv2.minEnclosingCircle(contr)
    if(8 < radius < 15):
        cv2.circle(img_2d_scaled, (int(x), int(y)), int(radius), (255,255,255), 1)
        #cv2.circle(img_2d_scaled, (int(x), int(y)), 12, (255,255,255), 1)
        print("i=", i, "x=", int(x), "y=", int(y), "radius=", int(radius))  #radius: 10 ~ 12
        #print("i=", i, "x=", int(x), "y=", int(y), "radius=", 12)   #radius 12 고정



plt.imshow(img_2d_scaled, cmap='gray')
plt.show()