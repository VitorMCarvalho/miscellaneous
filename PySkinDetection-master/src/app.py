import sys # for Command Line Arguments
from jeanCV import skinDetector
import cv2
import matplotlib.pyplot as plt
import numpy as num
import numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open webcam")
ret, check = cap.read()    
fundo = cv2.resize(check, None,fx=0.5,fy=0.5, interpolation=cv2.INTER_AREA)

while True:
    ret, frame = cap.read()    
    imageName = cv2.resize(frame, None,fx=0.5,fy=0.5, interpolation=cv2.INTER_AREA)
    detector = skinDetector(imageName, fundo)
    detector.find_skin()

cap.release()
cv2.destroyAllWindows()
