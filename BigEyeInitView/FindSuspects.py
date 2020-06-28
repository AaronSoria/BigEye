import numpy as np
import cv2
import datetime
import matplotlib.pyplot as plt

def searchPerson(imagen):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector() )
    # Capturo los puntos en donde posiblemente se encuentre la persona
    rects, weights = hog.detectMultiScale(imagen,winStride=(8, 8),padding=(16, 16),scale=1.05)
    return len(rects) != 0

def findSuspects(path):
    # Empiezo a capturar el tiempo
    myTime =  datetime.datetime.now()

    video= cv2.VideoCapture(path)

    fps=video.get(cv2.CAP_PROP_FPS)
    codec =cv2.VideoWriter_fourcc(*'XVID')

    timestamps = [video.get(cv2.CAP_PROP_POS_MSEC)]
    calc_timestamps = [0.0]

    size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    i=0
    success, frame = video.read()
    while success:
        i+=1
        #frame=cv2.resize(frame,(1280, 720))
        isPerson = False
        rgb= cv2.cvtColor(frame[::2,::2], cv2.COLOR_BGR2RGB)
        if (i%2 == 0):
            isPerson = searchPerson(rgb)
        success, frame = video.read()

        if isPerson:
            if success:
                timestamps.append(video.get(cv2.CAP_PROP_POS_MSEC))
                calc_timestamps.append(calc_timestamps[-1] + 1000/fps)
    
    video.release()

    result = []
    for i, (ts, cts) in enumerate(zip(timestamps, calc_timestamps)):
        result.append((abs(ts - cts))/1000)
    return result

