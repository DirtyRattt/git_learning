import numpy as np 
import cv2

camera = cv2.VideoCapture(0)

while True:
	ret, frame = camera.read()
	cv2.imshow('image', frame)
	cv2.waitKey(1)

cv2.destroyAllWindows()