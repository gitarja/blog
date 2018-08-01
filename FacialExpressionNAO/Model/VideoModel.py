#Naoqi
import vision_definitions
from naoqi import ALProxy
#QT thread
from PyQt4.QtCore import QThread
from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL

class VideoModel(QThread):
    def __init__(self, IP, port):
        super(VideoModel, self).__init__()
        self.IP = IP
        self.port = port

    def run(self):
        # connect to nao video device
        videoRecorderProxy = ALProxy("ALVideoDevice", self.IP, self.port)

        resolution = vision_definitions.kQVGA
        # get nao color space
        colorSpace = 11
        # set fps
        fps = 3.0
        # set frame widht and height
        # do not change the width and height
        imageWidth = 320
        imageHeight = 240


        # create videorecorderproxy instace
        nameId = videoRecorderProxy.subscribe("python_client", resolution, colorSpace, fps)

        while(True):
           naoImage = videoRecorderProxy.getImageRemote(nameId)
           # Get the image size and pixel array.
           array = naoImage[6]
           imageQT = QtGui.QImage(array, imageWidth, imageHeight, QtGui.QImage.Format_RGB888)
           # transfer the imageQT as a signal newImage(QImage) to Main.py
           self.emit(SIGNAL('newImage(QImage)'), imageQT)
           videoRecorderProxy.releaseImage(nameId)

        # destroy the following objects
        videoRecorderProxy.unsubscribe(nameId)
