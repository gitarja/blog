# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainView.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.setTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.setTextEdit.setGeometry(QtCore.QRect(90, 10, 621, 71))
        self.setTextEdit.setObjectName("setTextEdit")
        self.setButton = QtWidgets.QPushButton(self.centralwidget)
        self.setButton.setGeometry(QtCore.QRect(290, 120, 231, 111))
        self.setButton.setObjectName("setButton")
        self.setLabel = QtWidgets.QLabel(self.centralwidget)
        self.setLabel.setGeometry(QtCore.QRect(100, 260, 611, 171))
        self.setLabel.setText("")
        self.setLabel.setObjectName("setLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.setButton.setText(_translate("MainWindow", "Set"))

