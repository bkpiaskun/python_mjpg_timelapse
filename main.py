import cv2
import urllib 
import numpy as np
from matplotlib import pyplot as plt
import time

url = 'http://192.168.0.179:8080/?action=stream'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter('./vid1_{0}.avi'.format(time.strftime('%y-%m-%d-%H-%M')), fourcc, 15,  (640, 480))
while(True):
    try: 
        cap = cv2.VideoCapture(url)
        result, frame = cap.read()
        if result == False: 
            print("Error in cap.read()") # this is for preventing a breaking error 
            # break; 
            pass; 
        writer.write(frame)
    except KeyboardInterrupt:
        cap.release()
        writer.release()
        cv2.destroyAllWindows()