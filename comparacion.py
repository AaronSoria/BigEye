import numpy as np
import cv2
import datetime
import matplotlib.pyplot as plt

def detectar(imagen):
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector() )
    # Capturo los puntos en donde posiblemente se encuentre la persona
    rects, weights = hog.detectMultiScale(imagen,winStride=(8, 8),padding=(16, 16),scale=1.05)

    # Dibujo rectangulo
    for i, (x, y, w, h) in enumerate(rects):
        cv2.rectangle(imagen,(x,y),(x+w,y+h),(0,255,0),10)  
        fuente=cv2.FONT_HERSHEY_SIMPLEX
        peso=weights[i]
        y2 = x - 15 if x - 15 > 15 else x + 15
        cv2.putText(imagen, str(peso), (h, y2), fuente, 0.75, (0, 255, 0),2)
    return imagen

# Empiezo a capturar el tiempo
myTime =  datetime.datetime.now()

video= cv2.VideoCapture('/home/stark28/Documentos/tecnica3.mp4')

fps=video.get(cv2.CAP_PROP_FPS)
codec =cv2.VideoWriter_fourcc(*'XVID')
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
nuevoVideo= cv2.VideoWriter('/home/stark28/python_projects/Big_Eye/resultados/something.mp4',codec,fps,tuple(it//2 for it in size))  

i=0
success, frame = video.read()
while success:
    i+=1
    #frame=cv2.resize(frame,(1280, 720))
    rgb= cv2.cvtColor(frame[::2,::2], cv2.COLOR_BGR2RGB)
    if (i%2 == 0):
        nuevo_rgb= detectar(rgb)
    else:
        nuevo_rgb=rgb
    print(str(i))
    nuevo_bgr= cv2.cvtColor(nuevo_rgb, cv2.COLOR_RGB2BGR)
    nuevoVideo.write(nuevo_bgr)
    success, frame = video.read()    
video.release()
nuevoVideo.release()

print("")
print("[INFO] Listo")
print("[INFO] tiempo: {}s".format((datetime.datetime.now() - myTime).total_seconds()))
