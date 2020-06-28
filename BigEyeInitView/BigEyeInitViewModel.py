from BigEyeInit_ui import *
from PyQt5.QtWidgets import *
from FindSuspects import findSuspects
import datetime

class BigEyeInitView(QtWidgets.QMainWindow, Ui_MainWindow):
    currentFolderName = ""
    currentFileName = ""
     
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.ButtonAnalyze.clicked.connect(self.VideoAnalysis)
        self.ButtonSearchVideo.clicked.connect(self.VideoSearch)
        self.ButtonSetDestinyResults.clicked.connect(self.SetResultDestiny)

    def VideoAnalysis(self):
        if self.currentFileName != "" and self.currentFolderName != "":
            result = findSuspects(self.currentFileName)
            today = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            file = open(self.currentFolderName + "/resultados"+ str(today) + ".txt", "x")
            for item in result:
                videoMin = item/60
                line = "[ALERTA] revisar el minuto: " + str(videoMin) + "\n"
                file.write(line)
            file.close() 
            self.showMessage("Analisis finalizado","El analisis del video ha sido finalizado","BigEye")

    def VideoSearch(self):
        options = QFileDialog.Options()
        options = QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Buscar Video", "","All mp4 Files (*.mp4)", options=options)
        if fileName:
            self.set_currentFileName(fileName)
            self.EntryVideoPath.setPlainText(fileName)

    def SetResultDestiny(self):
        options = QFileDialog.Options()
        options = QFileDialog.DontUseNativeDialog
        folderName = QFileDialog.getExistingDirectory(self, "Seleccione carpeta de destino")
        if folderName:
            self.set_currentFolderName(folderName)
            self.EntryResultPath.setPlainText(folderName)

    def set_currentFileName(self, currentFileName):
        self.currentFileName = currentFileName

    def set_currentFolderName(self, currentFolderName):
        self.currentFolderName = currentFolderName
        
    def showMessage(self, message, informativeText, title):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setInformativeText(informativeText)
        msg.setWindowTitle(title)
        msg.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = BigEyeInitView()
    window.show()
    app.exec_()
