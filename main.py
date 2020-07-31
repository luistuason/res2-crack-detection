#Developed Crack Detection Algorithm implemented in Python 2.7
#OpenCV and Numpy libraries were used

#Author: Luis Tuason
#version2.0 : Automated Crack Detection

import cv2
import numpy as np
import time
from matplotlib import pylab

start_time = time.clock()

for x in xrange(1,3):
	for y in xrange(1,17):

		#Reading image
		s = str(y)
		c = str(x)
		if y < 10:
			im_name = 'S0'+s+'_C0'+c+'.jpg'
		else :
			im_name = 'S'+s+'_C0'+c+'.jpg'
		src = cv2.imread(im_name)

		#Converting the image from RGB to Grayscale
		gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

		#Set threshold values for edge detection
		v = np.median(gray)
		sigma = 0.5
		lower_thresh = int(max(0, (1.0-sigma) *v))
		upper_thresh = int(min(255, (1.0+sigma) *v))

		#Canny Edge Detection
		edges = cv2.Canny(gray,lower_thresh,upper_thresh)
		np.set_printoptions(threshold=np.inf)

		#Dilation and Erosion
		kernel_d = np.ones((3,3), np.uint8) #Dilation kernel
		kernel_e = np.ones((4,4), np.uint8)  #Erosion kernel

		dilated = cv2.dilate(edges, kernel_d, iterations=1)
		eroded = cv2.erode(dilated, kernel_e, iterations=1)

		cv2.imwrite(im_name+'_edge.png', eroded)

		#Proximity check
		img = cv2.imread(im_name+'_edge.png')

		h, w, channels = src.shape
		for r in range(0, h-10):
			for c in range(0, w-10):
				if img[r][c][0] == 255 and img[r][c][1] == 255 and img[r][c][2] == 255:
					if img[r+5][c][2] == 0 and img[r-5][c][2] == 0 and img[r][c+5][2] == 0 and img[r][c-5][2] == 0  and img[r+1][c-5][2] == 0 and img[r+2][c-4][2] == 0 and img[r+3][c-3][2] == 0 and img[r+4][c-2][2] == 0 and img[r+5][c-1][2] == 0 and img[r+5][c+1][2] == 0 and img[r+4][c+2][2] == 0 and img[r+3][c+3][2] == 0 and img[r+2][c+4][2] == 0 and img[r+1][c+5][2] == 0 and img[r-1][c+5][2] == 0 and img[r-2][c+4][2] == 0 and img[r-3][c+3][2] == 0 and img[r-4][c+2][2] == 0 and img[r-5][c+1][2] == 0 and img[r-5][c-1][2] == 0 and img[r-4][c-2][2] == 0 and img[r-3][c-3][2] == 0 and img[r-2][c-4][2] == 0 and img[r-1][c-5][2] == 0:
						img[r][c] = [0,0,0]

		cv2.imwrite(im_name, img)

		print("%s" % (time.clock() - start_time))