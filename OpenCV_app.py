import numpy as np 
import cv2

camera = cv2.VideoCapture(0)

while True:
	ret, frame = camera.read()
	key = cv2.waitKey(1)

	if key == 27:
		break

	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	ret, frame = cv2.threshold(frame,127,255,cv2.THRESH_TRUNC)
	cv2.imshow('image', frame)

cv2.destroyAllWindows()