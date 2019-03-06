from BigEyeInit_ui import *
class BigEyeInitView(QtWidgets.QMainWindow, Ui_MainWindow):
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
        pass

    def SetResultDestiny(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = BigEyeInitView()
    window.show()
    app.exec_()
