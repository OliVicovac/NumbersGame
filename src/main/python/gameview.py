"""
Created on 17.11.2017

@author: Michael Borko <mborko@tgm.ac.at>, Hans Brabenetz <hbrabenetz@tgm.ac.at>
@version: 20171117

@description: Implementation eines einfachen Spiels
              
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial

xybh = [
    (130, 180, 75, 23), (210, 180, 75, 23), (290, 180, 75, 23), (370, 180, 75, 23), (450, 180, 75, 23),
    (130, 150, 75, 23), (210, 150, 75, 23), (290, 150, 75, 23), (370, 150, 75, 23), (450, 150, 75, 23),
    (130, 120, 75, 23), (210, 120, 75, 23), (290, 120, 75, 23), (370, 120, 75, 23), (450, 120, 75, 23)
    ]


class GameView(object):

    def setupUi(self, Game_ovicovac):
        """
        Erstellung des GUI und Erstellen der Buttonsliste
        :param Game_ovicovac: MainWindow auf dem das GUI gezeichnet wird
        :return: nichts
        """
        Game_ovicovac.setObjectName("Game_ovicovac")
        Game_ovicovac.resize(560, 330)
        self.centralwidget = QtWidgets.QWidget(Game_ovicovac)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(130, 180, 75, 23))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 180, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 180, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 180, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(450, 180, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(130, 150, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(210, 150, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(290, 150, 75, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(370, 150, 75, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(450, 150, 75, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(130, 120, 75, 23))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(210, 120, 75, 23))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(290, 120, 75, 23))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(370, 120, 75, 23))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(450, 120, 75, 23))
        self.pushButton_15.setObjectName("pushButton_15")
        self.lineEdit_0 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_0.setGeometry(QtCore.QRect(70, 120, 31, 20))
        self.lineEdit_0.setObjectName("lineEdit")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_1.setGeometry(QtCore.QRect(70, 150, 31, 20))
        self.lineEdit_1.setObjectName("lineEdit_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 180, 31, 20))
        self.lineEdit_2.setObjectName("lineEdit_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 210, 31, 20))
        self.lineEdit_3.setObjectName("lineEdit_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 240, 31, 20))
        self.lineEdit_4.setObjectName("lineEdit_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 60, 391, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 240, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 210, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 150, 41, 16))
        self.label_5.setObjectName("label_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 120, 41, 16))
        self.label_6.setObjectName("label_7")
        self.pushButton_Neu = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Neu.setGeometry(QtCore.QRect(210, 240, 75, 23))
        self.pushButton_Neu.setObjectName("pushButton")
        self.pushButton_End = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_End.setGeometry(QtCore.QRect(370, 240, 75, 23))
        self.pushButton_End.setObjectName("pushButton_16")
        Game_ovicovac.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Game_ovicovac)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 21))
        self.menubar.setObjectName("menubar")
        Game_ovicovac.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Game_ovicovac)
        self.statusbar.setObjectName("statusbar")
        Game_ovicovac.setStatusBar(self.statusbar)

        self.retranslateUi(Game_ovicovac)
        QtCore.QMetaObject.connectSlotsByName(Game_ovicovac)

        self.buttons = [self.pushButton_1, self.pushButton_2, self.pushButton_3, self.pushButton_4, self.pushButton_5,
                        self.pushButton_6, self.pushButton_7, self.pushButton_8, self.pushButton_9, self.pushButton_10,
                        self.pushButton_11, self.pushButton_12, self.pushButton_13, self.pushButton_14, self.pushButton_15]

    def retranslateUi(self, Game_ovicovac):
        """
        Wird für setupUi benötigt
        :param Game_ovicovac: MainWindow auf dem das GUI gezeichnet wird
        :return: nichts
        """
        _translate = QtCore.QCoreApplication.translate
        Game_ovicovac.setWindowTitle(_translate("Game_ovicovac", "MyGame"))
        self.pushButton_1.setText(_translate("Game_ovicovac", "12"))
        self.pushButton_2.setText(_translate("Game_ovicovac", "6"))
        self.pushButton_3.setText(_translate("Game_ovicovac", "5"))
        self.pushButton_4.setText(_translate("Game_ovicovac", "11"))
        self.pushButton_5.setText(_translate("Game_ovicovac", "7"))
        self.pushButton_6.setText(_translate("Game_ovicovac", "10"))
        self.pushButton_7.setText(_translate("Game_ovicovac", "0"))
        self.pushButton_8.setText(_translate("Game_ovicovac", "14"))
        self.pushButton_9.setText(_translate("Game_ovicovac", "8"))
        self.pushButton_10.setText(_translate("Game_ovicovac", "2"))
        self.pushButton_11.setText(_translate("Game_ovicovac", "3"))
        self.pushButton_12.setText(_translate("Game_ovicovac", "9"))
        self.pushButton_13.setText(_translate("Game_ovicovac", "13"))
        self.pushButton_14.setText(_translate("Game_ovicovac", "1"))
        self.pushButton_15.setText(_translate("Game_ovicovac", "4"))
        self.lineEdit_0.setText(_translate("Game_ovicovac", "15"))
        self.lineEdit_1.setText(_translate("Game_ovicovac", "0"))
        self.lineEdit_2.setText(_translate("Game_ovicovac", "0"))
        self.lineEdit_3.setText(_translate("Game_ovicovac", "0"))
        self.lineEdit_4.setText(_translate("Game_ovicovac", "1"))
        self.label.setText(_translate("Game_ovicovac", "<html><head/><body><p align=\"center\">Drücken Sie die Buttons in aufsteigender Richtung</p></body></html>"))
        self.label_2.setText(_translate("Game_ovicovac", "Spiele"))
        self.label_3.setText(_translate("Game_ovicovac", "gesamt"))
        self.label_4.setText(_translate("Game_ovicovac", "falsch"))
        self.label_5.setText(_translate("Game_ovicovac", "korrekt"))
        self.label_6.setText(_translate("Game_ovicovac", "offen"))
        self.pushButton_Neu.setText(_translate("Game_ovicovac", "Neu"))
        self.pushButton_End.setText(_translate("Game_ovicovac", "Ende"))