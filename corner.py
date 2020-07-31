#Author: Luis Tuason & Ericka Torio    
#version2.0-1 : Corner Detection

import numpy as np
import cv2
from matplotlib import pyplot as plt

s = int(raw_input("Sample: "))
c = int(raw_input("Camera: "))

x = str(s)
y = str(c)

if s<10:
    im_name = 'S0'+x+'_C0'+y+'.jpg_final.png'
else:
    im_name = 'S'+x+'_C0'+y+'.jpg_final.png'

img = cv2.imread(im_name)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,1000,0.01,5)
corners = np.int0(corners)
a = (corners.size)/2

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),1,[255,255,0],-1)
print str(a)

cv2.imwrite(im_name, img)
