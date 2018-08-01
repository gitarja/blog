import sys
import time
from naoqi import ALProxy
#QT thread
from PyQt4.QtCore import QThread
from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL

#numpy
import numpy as np

class EmotionModel(QThread):
    def __init__(self, IP, port):
        super(EmotionModel, self).__init__()
        self.IP = IP
        self.port = port

    def run(self):
        #create instance of ALFaceCharacteristics
        faceCharProxy = ALProxy("ALFaceCharacteristics", self.IP, self.port)
        period = 500
        faceCharProxy.subscribe("Test_FaceChar", period, 0.0)
        #create instance of ALMemory
        memProxy = ALProxy("ALMemory", self.IP, self.port)


        while (True):
            self.result = np.zeros(5)
            for i in (0, 15):
                time.sleep(0.05)
                #get personId of detected face
                val2 = memProxy.getData("PeoplePerception/VisiblePeopleList")


                #if there is detected face
                if val2:
                    #get probability of each expression [neutral, happy, surprised, angry or sad] of detected face
                    try:
                        memExVal = "PeoplePerception/Person/" + str(val2[0]) + "/ExpressionProperties"
                        self.result = np.dot(memProxy.getData(memExVal), 100)
                    except Exception:
                        sys.exc_clear()

            self.emit(SIGNAL('emotionProb'), self.result)

        faceCharProxy.unsubscribe("Test_FaceChar")