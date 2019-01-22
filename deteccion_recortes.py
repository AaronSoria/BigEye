import numpy as np
import cv2
import datetime
import matplotlib.pyplot as plt
from multiprocessing import Process, Queue

def detectar(imagen,ident,q):
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
    #cv2.imwrite("/home/stark28/python_projects/Big_Eye/resultados/face-" + str(ident) + ".jpg", imagen)
    q.put(imagen)


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
	i+=2
	if __name__ == '__main__':
		q = Queue()
		
		rgb1= cv2.cvtColor(frame[::2,::2], cv2.COLOR_BGR2RGB)

		success, frame = video.read()
		rgb2= cv2.cvtColor(frame[::2,::2], cv2.COLOR_BGR2RGB)
		

		p1= Process(target=detectar, args=(rgb1,i-1,q))
		p2= Process(target=detectar, args=(rgb2,i,q))

		if rgb1 is not None:
			p1.start()
			img1=q.get()
			p1.join()

		if rgb2 is not None:
			p2.start()
			img2=q.get()
			p2.join()

		success, frame = video.read()
	print(str(i))
	img1= cv2.cvtColor(img1, cv2.COLOR_RGB2BGR)
	img2= cv2.cvtColor(img2, cv2.COLOR_RGB2BGR)
	nuevoVideo.write(img1)
	nuevoVideo.write(img2)


video.release()
nuevoVideo.release()

print("")
print("[INFO] Listo")
print("[INFO] tiempo: {}s".format((datetime.datetime.now() - myTime).total_seconds()))
