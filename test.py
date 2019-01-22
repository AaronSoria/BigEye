import numpy as np
import cv2
import datetime
import matplotlib.pyplot as plt


video= cv2.VideoCapture('/home/stark28/Documentos/tecnica3.mp4')

fps=video.get(cv2.CAP_PROP_FPS)
codec =cv2.VideoWriter_fourcc(*'XVID')
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
nuevoVideo= cv2.VideoWriter('/home/stark28/python_projects/Big_Eye/resultados/something.mp4',codec,fps,tuple(it//2 for it in size))  

frame=video.read()
rgb1= cv2.cvtColor(frame[::2,::2], cv2.COLOR_BGR2RGB)
rgb2= cv2.cvtColor(frame[::2,::2], cv2.COLOR_BGR2RGB)
cv2.imshow('1',rgb1)
cv2.imshow('1',rgb2)

