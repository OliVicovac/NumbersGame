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

    def setup_ui(self, Dialog, Controller):
        pass

    def retranslate_ui(self, Dialog, Controller):
        pass
