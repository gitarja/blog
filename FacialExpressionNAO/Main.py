import sys
from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import Qt
from Model.VideoModel import VideoModel
from Model.EmotionModel import EmotionModel
import Setting
from View import MainView


class MainAPP(QtGui.QMainWindow, MainView.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainAPP, self).__init__(parent)
        self.setupUi(self)
        self.vidModel = VideoModel(Setting.IP, Setting.port)
        self.emotionModel = EmotionModel(Setting.IP, Setting.port)
        self.angryProb.connect(self.emotionModel, SIGNAL('emotionProb'), self.setEmotionProb, Qt.AutoConnection)
        self.videoPanel.connect(self.vidModel, SIGNAL('newImage(QImage)'), self.setFrame, Qt.AutoConnection)
        self.vidModel.start()
        self.emotionModel.start()

    # set the value of video panel with image
    def setFrame(self, frame):
        self.videoPanel.setPixmap(QtGui.QPixmap.fromImage(frame))

    #set emotion prob
    def setEmotionProb(self, prob):
        try:
            self.angryProb.setValue(prob[3])
            self.happyProb.setValue(prob[1])
            self.neutralProb.setValue(prob[0])
            self.sadProb.setValue(prob[4])
            self.surprisedProb.setValue(prob[2])
        except Exception:
            self.angryProb.setValue(0)
            self.happyProb.setValue(0)
            self.neutralProb.setValue(0)
            self.sadProb.setValue(0)
            self.surprisedProb.setValue(0)






def main(self):
    app = QtGui.QApplication(sys.argv)
    #create new instance of MainAPP()
    mainWindow = MainAPP()
    #show the window
    mainWindow.show()
    #execute the app
    app.exec_()



if __name__ == "__main__":
    main(self=None)