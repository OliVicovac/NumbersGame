"""
Created on 17.11.2017

@author: Michael Borko <mborko@tgm.ac.at>, Hans Brabenetz <hbrabenetz@tgm.ac.at>
@version: 20171117

@description: Implementation eines einfachen Spiels
              
"""

from gameview import GameView
from gamemodel import GameModel

from PyQt5 import QtCore, QtGui, QtWidgets
import random
import sys
from functools import partial


class GameController(object):
    """
        GameController
        Das Spiel wird mit der Funktion :func:`__init__` gestartet
            - **Methoden**:
                * :func:`GameController.show`: Zeigt das GUI an
                * :func:`GameController.game_playing`: bekommt button und schaut ob es der richtige Button ist
                * :func:`GameController.updateStatistik`: aktualisiert die Statistik
                * :func:`GameController.reshuffle`: Zufällige Zahlen werden den Buttons zugewiesen
                * :func:`GameController.push_button_new_click`: neues Spiel wird gestarten
                * :func:`GameController.push_button_end_click`: Spiel wird geschlossen
        """
    def __init__(self):
        """
        Konstruktor
        """
        self.Dialog = QtWidgets.QMainWindow()
        self.view = GameView()
        self.model = GameModel()
        self.view.setupUi(self.Dialog)

    def show(self):
        """
        Zeigt das GUI des Spiels an
        :return: nichts
        """
        self.Dialog.show()
        self.reshuffle()
        self.view.pushButton_Neu.clicked.connect(partial(self.push_button_new_click))
        self.view.pushButton_End.clicked.connect(partial(self.push_button_end_click))

        for button in self.view.buttons:
            button.clicked.connect(partial(self.game_playing, button))



    def game_playing(self, p):
        """
        bekommt button und schaut ob es der richtige Button ist
        :param p: button der gedrückt wurde
        :type p: `QPushButton`
        :return: nichts
        """
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
        """
        Aktualisiert die Statistik
        :return: nichts
        """
        self.view.lineEdit_0.setText(str(self.model.isOpen))
        self.view.lineEdit_1.setText(str(self.model.isCorrect))
        self.view.lineEdit_2.setText(str(self.model.isWrong))
        self.view.lineEdit_3.setText(str(self.model.isTotal))
        self.view.lineEdit_4.setText(str(self.model.Ngame))


    def reshuffle(self):
        """
        Zufällige Zahlen (0 - 14) werden den Buttons zugewiesen
        :return:  nichts
        """
        for button in self.view.buttons:
            button.setEnabled(True)
        i = 0
        buttonValues = []
        while i < 15:
            randnum = random.randrange(0, 15)
            if not (randnum in buttonValues):
                buttonValues.append(randnum)
                i += 1

        i = 0
        for button in self.view.buttons:
            button.setText(str(buttonValues[i]))
            i += 1




    def push_button_new_click(self):
        """
        Neues Spiel wird gestartet beim klicken des Neu-buttons
        :return: nichts
        """
        self.model.new_game()
        self.updateStatistik()
        self.reshuffle()

    def push_button_end_click(self):
        """
        Spiel wird beendet beim klicken des Ende-buttons
        :return: nichts
        """
        sys.exit()
