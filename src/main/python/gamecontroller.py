"""
Created on 17.11.2017

@author: Michael Borko <mborko@tgm.ac.at>, Hans Brabenetz <hbrabenetz@tgm.ac.at>
@version: 20171117

@description: Implementation eines einfachen Spiels
              
"""

from gameview import GameView
from gamemodel import GameModel

from PyQt5 import QtCore, QtGui, QtWidgets
from random import *
import sys
from functools import partial


class GameController(object):
    def __init__(self):
        self.Dialog = QtWidgets.QMainWindow()
        self.view = GameView()
        self.model = GameModel()
        self.view.setupUi(self.Dialog)
        self.items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.x = sample(self.items, 1)


    def show(self):

        self.Dialog.show()

        self.view.pushButton_Neu.clicked.connect(partial(self.push_button_new_click))
        self.view.pushButton_End.clicked.connect(partial(self.push_button_end_click))

        for button in self.view.buttons:
            button.clicked.connect(partial(self.game_playing, button))



    def game_playing(self, p):
        button = p
        if int(button.text()) == self.model.nextValue:
            button.setEnabled(False)
            self.model.nextValue += 1
            self.model.isCorrect += 1
            self.model.isOpen -= 1
        else:
            self.model.isWrong += 1
        self.model.isTotal += 1
        self.updateStatistik()



    def updateStatistik(self):
        self.view.lineEdit_0.setText(str(self.model.isOpen))
        self.view.lineEdit_1.setText(str(self.model.isCorrect))
        self.view.lineEdit_2.setText(str(self.model.isWrong))
        self.view.lineEdit_3.setText(str(self.model.isTotal))
        self.view.lineEdit_4.setText(str(self.model.Ngame))


    def reshuffle(self):
        pass

    def push_button_new_click(self):
        self.model.new_game()
        self.updateStatistik()
        self.reshuffle()

    def push_button_end_click(self):
        sys.exit()
