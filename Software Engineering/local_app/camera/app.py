import requests
import cv2
import os
from PIL import Image

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    success, img = cap.read()

    if success:    
        cv2.imshow("OUTPUT", img)
        
        _, imdata = cv2.imencode('.JPG', img)

        print('.', end='', flush=True)

        requests.put('http://127.0.0.1:5000/upload', data=imdata.tobytes())
    
    # 40ms = 25 frames per second (1000ms/40ms), 
    # 1000ms = 1 frame per second (1000ms/1000ms)
    # but this will work only when `imshow()` is used.
    # Without `imshow()` it will need `time.sleep(0.04)` or `time.sleep(1)`

    if cv2.waitKey(100) == 1000:  # 40ms = 25 frames per second (1000ms/40ms) 
        break

cv2.destroyAllWindows()
cap.release()