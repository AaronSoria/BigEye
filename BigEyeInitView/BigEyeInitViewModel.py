from BigEyeInit_ui import *
from PyQt5.QtWidgets import *

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
        #llamar al metodo que hace analisis de video
        pass

    def VideoSearch(self):
        options = QFileDialog.Options()
        options = QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Buscar Video", "","All mp4 Files (*.mp4)", options=options)
        if fileName:
            self.set_currentFileName(fileName)
            self.entryVideoInput.setPlainText(fileName)

    def SetResultDestiny(self):
        options = QFileDialog.Options()
        options = QFileDialog.DontUseNativeDialog
        folderName = QFileDialog.getExistingDirectory(self, "Seleccione carpeta de destino")
        if folderName:
            self.set_currentFolderName(folderName)
            self.entryImageOutput.setPlainText(folderName)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = BigEyeInitView()
    window.show()
    app.exec_()
