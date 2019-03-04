import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)  #para controlar el inicio de la aplicacion

w = QWidget()  #se incializa el objeto widget, es el conmaximo contenedor de todos lo elementos
w.resize(250, 150) #definimos el tamaño
w.move(300, 300) #definimos la ubicacion con respecto a los margenes de la pantalla
w.setWindowTitle('Simple') # definimos el titulo de la pantalla
w.show() #decimos que se muestre la pantall
sys.exit(app.exec_()) #con esto iniciamos el manejador de eventos 
