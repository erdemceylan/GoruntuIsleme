# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:28:59 2021

@author: Software
"""

import cv2
import numpy as np
import requests

url = "http://192.168.1.107:8080//shot.jpg"

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype = np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    img = cv2.resize(img, (1080,720))
    
    cv2.imshow("Android Camera", img)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()