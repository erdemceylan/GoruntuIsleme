# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 15:09:34 2021

@author: Software
"""

import cv2
import numpy as np

img = cv2.imread("C:/Users/Software/Desktop/YOLO/mask_detection/mask.jpg")

img_width = img.shape[1]
img_height = img.shape[0]

img_blob = cv2.dnn.blobFromImage(img,1/255,(416,416),swapRB = True, crop = False)

labels = ["good", "bad"]

colors = ["0,255,0", "0,0,255"]
colors = [np.array(color.split(",")).astype("int") for color in colors]
colors = np.array(colors)
colors = np.tile(colors,(18,1))

model = cv2.dnn.readNetFromDarknet("C:/Users/Software/Desktop/YOLO/mask_detection/yolov3_mask.cfg","C:/Users/Software/Desktop/YOLO/mask_detection/yolov3_mask_last.weights")

layers = model.getLayerNames()
output_layer = [layers[layer[0]-1] for layer in model.getUnconnectedOutLayers()]

model.setInput(img_blob)

detection_layers = model.forward(output_layer)

for detection_layer in detection_layers:
    for object_detection in detection_layer:
        
        scores = object_detection[5:]
        predicted_id = np.argmax(scores)
        confidence = scores[predicted_id]
        
        if confidence > 0.30:
            label = labels[predicted_id]
            bounding_box = object_detection[0:4]*np.array([img_width,img_height,img_width,img_height])
            (box_center_x, box_center_y,box_width,box_height) = bounding_box.astype("int")
            
            start_x = int(box_center_x -(box_width/2))
            start_y = int(box_center_y -(box_width/2))
            
            end_x = start_x + box_width
            end_y = start_y + box_height
            
            box_color = colors[predicted_id]
            box_color = [int(each) for each in box_color]
            
            label = "{}: {:.2f}%".format(label,confidence*100)
            print("predicted object {}".format(label))
            
            cv2.rectangle(img, (start_x,start_y),(end_x,end_y),box_color,2)
            cv2.putText(img,label,(start_x,start_y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,box_color,1)
          
cv2.imshow("Detection Window", img)
            