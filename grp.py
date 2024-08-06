import cv2 as cv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

matrix =  np.zeros((1000,1000,3),dtype='uint8')

matrix[:] = 0,255,255

#text = str(input('Enter Text: \n'))

#needed = text.replace(' C','').replace('R','')

#print(needed)

cv.rectangle(matrix,pt1=(0,0),pt2=(750,1200),color=(0,0,255),thickness=2)

plt.imshow(matrix)

plt.show()