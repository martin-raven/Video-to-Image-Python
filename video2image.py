import cv2
import os
import numpy
Videos = os.listdir("Videos")
for Video in Videos:
	vidcap = cv2.VideoCapture(
		"C:/Users/martin/Desktop/TestProject/Video to image/Videos/" + Video)
	success,image = vidcap.read()
	os.makedirs("Images/"+Video[0:-4])
	count = 0
	success = True
	while success:
		cv2.imwrite("Images/"+Video[0:-4] + "/" + "frame%d.jpg" % count, numpy.rot90(image,3))
		success, image = vidcap.read()
		print('Processing image '+ Video[0:-4] +"frame%d.jpg from " %count +Video, success)
		count += 1
