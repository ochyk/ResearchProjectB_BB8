# -*- coding: utf-8 -*-
from scipy.spatial import distance
from imutils import face_utils
import imutils
import dlib
import cv2
import requests # This is for the communication between python and node.js
import time

def eye_aspect_ratio(eye):
	A = distance.euclidean(eye[1], eye[5])
	B = distance.euclidean(eye[2], eye[4])
	C = distance.euclidean(eye[0], eye[3])
	ear = (A + B) / (2.0 * C)
	return ear

thresh = 0.25
frame_check_sleepy_1 = 50 #少し眠い
frame_check_sleepy_2 = 100 #眠い
frame_check_sleepy_3 = 150 #かなり眠い
frame_check_sleepy_4 = 200 #超眠い
detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")# Dat file is the crux of the code

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]
cap=cv2.VideoCapture(0)
flag = [0] * 10
while True:
	ret, frame=cap.read()
	frame = imutils.resize(frame, width=450)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	subjects = detect(gray, 0)
	for subject in subjects:
		shape = predict(gray, subject)
		shape = face_utils.shape_to_np(shape)#converting to NumPy Array
		leftEye = shape[lStart:lEnd]
		rightEye = shape[rStart:rEnd]
		leftEAR = eye_aspect_ratio(leftEye)
		rightEAR = eye_aspect_ratio(rightEye)
		ear = (leftEAR + rightEAR) / 2.0
		leftEyeHull = cv2.convexHull(leftEye)
		rightEyeHull = cv2.convexHull(rightEye)
		cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
		cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
		if ear < thresh:
			flag[0] += 1
			print (flag[0])
			if flag[0] >= frame_check_sleepy_1:
				flag[1] = 1
				cv2.putText(frame, "****************ALERT!****************", (10, 30),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
				cv2.putText(frame, "****************ALERT!****************", (10,325),
					cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
				#print ("Drowsy")
				if flag[2] == 0:
					id = {'ID':'sleepy1'} #少し眠い
					response = requests.post('http://localhost:3000/',data=id)
					print(response.text)
					flag[2] = 1
				if flag[0] >= frame_check_sleepy_4 and flag[2] == 1 and flag[3] == 0:
					id = {'ID':'sleepy4'} #超眠い
					response = requests.post('http://localhost:3000/',data=id)
					print(response.text)
					flag[3] = 1
				if flag[0] >= frame_check_sleepy_3 and flag[2] == 1 and flag[4] == 0:
					id = {'ID':'sleepy3'} #かなり眠い
					response = requests.post('http://localhost:3000/',data=id)
					print(response.text)
					flag[4] = 1
				if flag[0] >= frame_check_sleepy_2 and flag[2] == 1 and flag[5] == 0:
					id = {'ID':'sleepy2'} #眠い
					response = requests.post('http://localhost:3000/',data=id)
					print(response.text)
					flag[5] = 1
		else:
			flag[0] = 0
			if flag[1] == 1:
				id = {'ID':'awake'} #起きている
				response = requests.post('http://localhost:3000/',data=id)
				print(response.text)
				for i in range(10):
					flag[i] = 0

	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break
cv2.destroyAllWindows()
cap.stop()
