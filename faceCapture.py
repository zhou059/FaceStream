##########################################
# App to capture faces on Jetson and pub
# Created by: Jonathan Zhou
##########################################

import numpy as np
import cv2 as cv
import time
import paho.mqtt.client as paho
import sys

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connection to broker: Success!")
    else:
        print("Connection to broker: Failed!")
        
# Connect to client
client = paho.Client()
client.on_connect = on_connect
client.connect("169.63.90.153", 1883, 60)

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv.VideoCapture(0)

client.loop_start()
while(True):
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    img = cv.imshow('frame', gray)
    
    for (x,y,w,h) in faces:
        captured_face = gray[y:y+h,x:x+w]
        cv.imshow("crop", captured_face)
        client.publish("faces", bytearray(cv.imencode('.png', captured_face)[1]), qos=1)

    if cv.waitKey(1) == 27:
        break
    
client.loop_stop()
client.disconnect()
cap.release()
cv.destroyAllWindows()
