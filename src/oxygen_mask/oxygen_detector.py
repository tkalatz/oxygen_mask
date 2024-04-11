#! /usr/bin/python3

import rospy
from sensor_msgs.msg import Image as msgImage
from cv_bridge import CvBridge, CvBridgeError
import cv2
from PIL import Image
import numpy as np
from mtcnn.mtcnn import MTCNN
import tensorflow as tf
import keras
import os
import sys

W = 160
H = 160

def extract_face(cv2img, required_size=(W, H)):
    cv2img = cv2.cvtColor(cv2img, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(cv2img)
    #image =  image.convert('RGB')
    pixels = np.asarray(image)
    detector = MTCNN()
    results = detector.detect_faces(pixels)
    if results != []:
        x1, y1, width, height = results[0]['box']
        x1, y1 = abs(x1), abs(y1)
        x2, y2 = x1 + width, y1 + height
        face = pixels[y1:y2, x1:x2]
        image = Image.fromarray(face)
        image = image.resize(required_size)
        image = image.convert('L')
        image.save('temp.jpg') # save the face area
        face_array = np.asarray(image)
        return face_array

bridge = CvBridge()
# change path location 
model = keras.models.load_model("/opt/oxygen_model.h5")


def image_callback(msg):
    try:
        # Convert your ROS Image message to OpenCV2
        cv2_img = bridge.imgmsg_to_cv2(msg, "bgr8")
    except CvBridgeError as  e:
        print(e)
    else:
        #time = msg.header.stamp
        #cv2.imwrite(''+str(time)+'.jpeg', cv2_img)
        Xtest = extract_face(cv2_img)
        Xtest=Xtest.reshape(1,160,160,1)
        predicted_output = model.predict(Xtest) #,1,0) #, batch_size=30)
        index_max = np.argmax(predicted_output[0])
        #print(index_max)
        #change output or subscribe to channel and post
        if index_max==0:
            print("Not wearing a mask")
        elif index_max==1:
            print("Correctly wearing a mask")
        else:
            print("Wrong wearing a mask")
        rospy.sleep(1)

def main():
    rospy.init_node('image_listener')
    image_topic = "/usb_cam/image_raw"
    rospy.Subscriber(image_topic, msgImage, image_callback)
    rospy.spin()

if __name__ == '__main__':
    main()
