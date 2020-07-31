import cv2

for x in xrange(1,3):
	for y in xrange(1,17):

		#Reading image
		s = str(y)
		c = str(x)
		if y < 10:
			im_name = 'S0'+s+'_C0'+c+'.jpg_final.png'
		else :
			im_name = 'S'+s+'_C0'+c+'.jpg_final.png'

		img = cv2.imread(im_name)
		img = cv2.bitwise_not(img)
		cv2.imwrite(im_name, img)