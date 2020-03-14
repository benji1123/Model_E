from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np



#setting up picamera
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 24

rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.1)


template = cv2.imread("assets/stop_sign.jpg",0) #read template image (stop sign)
template = cv2.resize(template, (0,0), fx=0.7, fy=0.7) #change size of template to match size of sign in source image
w, h = template.shape[::-1] #get width and height of sign

stop = False

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    time.sleep(0.0)
    image = frame.array
 
    source_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    
    result = cv2.matchTemplate(source_gray,template,cv2.TM_CCOEFF_NORMED) #find match in source image

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result) #get location of match in source image (max_loc), get correlation (max_val)

    threshold = 0.5 #set threshold for correlation of match to template image

    if max_val >= threshold:
        stop = True
        cv2.rectangle(image, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)  #draw rectangle based on max_loc
    else:
        stop = False


    if stop == True:
        print("STOP!")

    # Display the resulting frame 
    cv2.imshow('frame',image)
    rawCapture.truncate(0)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): 
      break 


cv2.destroyAllWindows() 
