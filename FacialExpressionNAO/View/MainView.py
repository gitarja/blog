# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(801, 520)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.videoPanel = QtGui.QLabel(self.centralwidget)
        self.videoPanel.setGeometry(QtCore.QRect(20, 20, 431, 421))
        self.videoPanel.setObjectName(_fromUtf8("videoPanel"))
        self.expressionFrame = QtGui.QFrame(self.centralwidget)
        self.expressionFrame.setGeometry(QtCore.QRect(480, 20, 301, 311))
        self.expressionFrame.setStyleSheet(_fromUtf8(""))
        self.expressionFrame.setFrameShape(QtGui.QFrame.Box)
        self.expressionFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.expressionFrame.setLineWidth(1)
        self.expressionFrame.setObjectName(_fromUtf8("expressionFrame"))
        self.label = QtGui.QLabel(self.expressionFrame)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("font: 87 10pt \"Arial Black\";\n"
"color: rgb(0, 0, 0);"))
        self.label.setFrameShadow(QtGui.QFrame.Sunken)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName(_fromUtf8("label"))
        self.frame = QtGui.QFrame(self.expressionFrame)
        self.frame.setGeometry(QtCore.QRect(10, 50, 271, 41))
        self.frame.setStyleSheet(_fromUtf8("background-color: rgb(71, 182, 255);"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.angryLabel = QtGui.QLabel(self.frame)
        self.angryLabel.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.angryLabel.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"font: 11pt \"Arial\";"))
        self.angryLabel.setObjectName(_fromUtf8("angryLabel"))
        self.angryProb = QtGui.QProgressBar(self.frame)
        self.angryProb.setGeometry(QtCore.QRect(80, 10, 181, 23))
        self.angryProb.setProperty("value", 0)
        self.angryProb.setObjectName(_fromUtf8("angryProb"))
        self.frame_3 = QtGui.QFrame(self.expressionFrame)
        self.frame_3.setGeometry(QtCore.QRect(10, 100, 271, 41))
        self.frame_3.setStyleSheet(_fromUtf8("background-color: rgb(71, 182, 255);"))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.happyLabel = QtGui.QLabel(self.frame_3)
        self.happyLabel.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.happyLabel.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"font: 11pt \"Arial\";"))
        self.happyLabel.setObjectName(_fromUtf8("happyLabel"))
        self.happyProb = QtGui.QProgressBar(self.frame_3)
        self.happyProb.setGeometry(QtCore.QRect(80, 10, 181, 23))
        self.happyProb.setProperty("value", 0)
        self.happyProb.setObjectName(_fromUtf8("happyProb"))
        self.frame_4 = QtGui.QFrame(self.expressionFrame)
        self.frame_4.setGeometry(QtCore.QRect(10, 150, 271, 41))
        self.frame_4.setStyleSheet(_fromUtf8("background-color: rgb(71, 182, 255);"))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.neutralLabel = QtGui.QLabel(self.frame_4)
        self.neutralLabel.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.neutralLabel.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"font: 11pt \"Arial\";"))
        self.neutralLabel.setObjectName(_fromUtf8("neutralLabel"))
        self.neutralProb = QtGui.QProgressBar(self.frame_4)
        self.neutralProb.setGeometry(QtCore.QRect(80, 10, 181, 23))
        self.neutralProb.setProperty("value", 0)
        self.neutralProb.setObjectName(_fromUtf8("neutralProb"))
        self.frame_5 = QtGui.QFrame(self.expressionFrame)
        self.frame_5.setGeometry(QtCore.QRect(10, 200, 271, 41))
        self.frame_5.setStyleSheet(_fromUtf8("background-color: rgb(71, 182, 255);"))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.sadLabel = QtGui.QLabel(self.frame_5)
        self.sadLabel.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.sadLabel.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"font: 11pt \"Arial\";"))
        self.sadLabel.setObjectName(_fromUtf8("sadLabel"))
        self.sadProb = QtGui.QProgressBar(self.frame_5)
        self.sadProb.setGeometry(QtCore.QRect(80, 10, 181, 23))
        self.sadProb.setProperty("value", 0)
        self.sadProb.setObjectName(_fromUtf8("sadProb"))
        self.frame_6 = QtGui.QFrame(self.expressionFrame)
        self.frame_6.setGeometry(QtCore.QRect(10, 250, 271, 41))
        self.frame_6.setStyleSheet(_fromUtf8("background-color: rgb(71, 182, 255);"))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.surprisedLabel = QtGui.QLabel(self.frame_6)
        self.surprisedLabel.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.surprisedLabel.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
"font: 11pt \"Arial\";"))
        self.surprisedLabel.setObjectName(_fromUtf8("surprisedLabel"))
        self.surprisedProb = QtGui.QProgressBar(self.frame_6)
        self.surprisedProb.setGeometry(QtCore.QRect(80, 10, 181, 23))
        self.surprisedProb.setProperty("value", 0)
        self.surprisedProb.setObjectName(_fromUtf8("surprisedProb"))
        self.gazeFrame = QtGui.QFrame(self.centralwidget)
        self.gazeFrame.setGeometry(QtCore.QRect(480, 340, 301, 121))
        self.gazeFrame.setFrameShape(QtGui.QFrame.Box)
        self.gazeFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.gazeFrame.setObjectName(_fromUtf8("gazeFrame"))
        self.label_2 = QtGui.QLabel(self.gazeFrame)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 91, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("font: 87 10pt \"Arial Black\";\n"
"color: rgb(0, 0, 0);"))
        self.label_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lookAtRobLabel = QtGui.QLabel(self.gazeFrame)
        self.lookAtRobLabel.setGeometry(QtCore.QRect(10, 30, 181, 16))
        self.lookAtRobLabel.setObjectName(_fromUtf8("lookAtRobLabel"))
        self.gazeAnalysisLabel = QtGui.QLabel(self.gazeFrame)
        self.gazeAnalysisLabel.setGeometry(QtCore.QRect(110, 50, 111, 41))
        self.gazeAnalysisLabel.setStyleSheet(_fromUtf8("font: 87 14pt \"Arial Black\";\n"
"color: rgb(0, 0, 0);"))
        self.gazeAnalysisLabel.setObjectName(_fromUtf8("gazeAnalysisLabel"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.videoPanel.setText(_translate("MainWindow", "TextLabel", None))
        self.label.setText(_translate("MainWindow", "Expression:", None))
        self.angryLabel.setText(_translate("MainWindow", "angry", None))
        self.happyLabel.setText(_translate("MainWindow", "happy", None))
        self.neutralLabel.setText(_translate("MainWindow", "neutral", None))
        self.sadLabel.setText(_translate("MainWindow", "sad", None))
        self.surprisedLabel.setText(_translate("MainWindow", "surprised", None))
        self.label_2.setText(_translate("MainWindow", "Gaze", None))
        self.lookAtRobLabel.setText(_translate("MainWindow", "Look at the robot?", None))
        self.gazeAnalysisLabel.setText(_translate("MainWindow", "TextLabel", None))

