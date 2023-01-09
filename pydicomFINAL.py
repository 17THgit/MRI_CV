#   MRDC file image intensity with python FINAL
import pydicom
import cv2
import numpy as np
import matplotlib.pyplot as plt

#   i6812091.MRDC.1에서 얻은 minimum enclosing circle들의 center point(int형)
coordinate = np.array([[162, 162], [200, 162], [238, 163], [277, 163], [316, 164], [354, 164],
                        [161, 201], [200, 201], [238, 201], [277, 202], [315, 203], [353, 203],
                        [161, 239], [199, 240], [237, 240], [276, 241], [315, 241], [353, 242],
                        [160, 277], [199, 278], [237, 278], [276, 279], [314, 279], [352, 280],
                        [160, 316], [198, 316], [237, 316], [275, 317], [314, 317], [352, 318],
                        [159, 354], [198, 354], [237, 354], [275, 355], [314, 355], [352, 356]])
#   그릴 원의 반지름. 필요에 따라 변경 가능
radius = 12

#   DICOM 이미지 읽기
filepath = '/Users/TH/Desktop/2022S/T1/'
#filename = 'i6812090.MRDC.1'
filename = input('input file name like i6812090.MRDC.1: ') #input only file name
img_filepath = filepath + filename
img_dicom = pydicom.read_file(img_filepath)
#   DICOM 이미지 이진화
img = img_dicom.pixel_array
img_2d = img.astype(float)
img_2d_scaled = (np.maximum(img_2d, 0) / img_2d.max()) * 255.0   #grayscale

img_2d_scaled = np.uint8(img_2d_scaled)

#   이진화한 이미지 copy
img_copy = img_2d_scaled.copy()

#   36 circles image intensity
for i in range(len(coordinate)):
    mask = np.zeros(img_2d_scaled.shape, np.uint8)
    center = (coordinate[i, 0], coordinate[i, 1])
    r = radius

    cv2.circle(mask, center, r, 255, -1)
    #   img_copy에 원 그리기
    cv2.circle(img_copy, center, r, (255, 255, 255), 1)
    #   img_copy에 원 번호 추가
    textAlign = (center[0] - 20, center[1] - 10)
    text = str(i + 1)
    cv2.putText(img_copy, text, textAlign, cv2.FONT_HERSHEY_PLAIN, 0.5, (255, 255, 255), 1, cv2.LINE_8)

    #   image intensity
    where = np.where(mask == 255)
    intensity = img_2d_scaled[where[1], where[0]]

    print("-------------------------------------------------------------------")
    print("Circle", i+1, 'Center', center)
    print("area\t min\t max\t mean\t\t\t standard deviation")
    print(int(3.1415*r*r), "\t", np.min(intensity), "\t", np.max(intensity), "\t", np.mean(intensity), "\t", np.std(intensity))
print("-------------------------------------------------------------------")

#   image intensity from img_2d_scaled, print img_copy with circles
plt.subplot(1,2,1)
plt.imshow(img_2d_scaled, cmap='gray')
plt.subplot(1,2,2)
plt.imshow(img_copy, cmap = 'gray')
plt.show()