##########################################################################
# This will listen to the broker on IBMCloud container and save it into
# the bucket. 
# 
# Developer=jonathan.zhou@berkeley.edu
##########################################################################

import numpy as np
import cv2 as cv
import paho.mqtt.client as paho

def on_connect(client, userdata, flags, rc):
    print("Connected to broker with result code "+str(rc))
    client.subscribe("faces")

img_number = 0

def on_message(client, userdata, msg):
    global img_number

    f = np.frombuffer(msg.payload, dtype='uint8')
    img = cv.imdecode(f, flags=1)
    img_name = "/s3fs_faces/face_" + str(img_number) + ".png"
    cv.imwrite(img_name, img)

    print(img_name)

    img_number = img_number + 1
    
client= paho.Client()
client.connect("169.63.90.153", 1883, 60)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()
