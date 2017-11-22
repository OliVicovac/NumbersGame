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


class GameController(object):

    def __init__(self):
        pass

    def show(self):
        pass 

    def game_playing(self, p):
        pass

    def reshuffle(self):
        pass

    def push_button_new_click(self):
        pass

    def push_button_end_click(self):
        sys.exit()
