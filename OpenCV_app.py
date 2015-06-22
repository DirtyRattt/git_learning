import numpy as np 
import cv2

camera = cv2.VideoCapture(0)

while True:
	ret, frame = camera.read()
	cv2.imshow('image', frame)
	key = cv2.waitKey(1)

	if key == 27:
		break

frame = cv2.cvtColor(frame, cv2.cvtCOLOR_BGR2GRAY)
cv2.imshow('image', frame)

cv2.destroyAllWindows()