# Project Laboratory B
Wake a sleeping student up by using BB8!

## Applications

This can be used by students who have to stay up all night for studying.

### Programs

(Dlib + OpenCV / Python) + (Cylon / Node.js)

To detect drowsiness: drowsiness_detection_for_bb8.py  
To move BB8: bb8_server.js  

or  

To detect drowsiness: face_and_eye_recognition.py  
To move BB8: bb8_server.js  

### Requirements
Python (Both of 2.x and 3.x)  
Node.js (v5.3.0)  

### Dependencies
Python:  
import cv2  
import imutils  
import dlib  
import scipy  

import requests  

Javascript:  
npm install nodebrew  
npm install cylon  
npm install cylon-ble  

npm install express  
npm install body-parser  

### References
Dlib + OpenCV:  
(drowsiness_detection_for_bb8.py)  
https://github.com/akshaybahadur21/Drowsiness_Detection/blob/master/readme.md  
https://www.pyimagesearch.com/2017/05/08/drowsiness-detection-opencv/  

(face_and_eye_recognition.py)  
https://blog.shimabox.net/2018/08/29/recognize_the_face_of_webcam_image_with_python_opencv/  

Node.js(Cylon):  
(documentation for bb8)  
https://cylonjs.com/documentation/drivers/bb8/  

(To detect collision)  
https://www.ibm.com/developerworks/jp/cloud/library/cl-watson-bb8/index.html  

Communication(Python + Javascript):  
(From Python to Node.js)  
https://teratail.com/questions/122666  
https://garafu.blogspot.com/2017/02/nodejs-express-webapi.html?m=1  
