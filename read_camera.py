import os
import cv2
import urllib.request
import requests

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"]="rtsp_transport;udp"


#print("Before URL")
#print("After URL")
adr = 'rtsp://192.168.100.86:554'
try:
    stream = cv2.VideoCapture(adr)
except Exception as g:
    print("no stream")

while True:
    img_res = stream.read()
    #ret,img_res = stream.read()
    #print('About to show frame of Video.')
    try:
        cv2.imshow("Capturing",img_res)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except Exception as e:
        print(e)
