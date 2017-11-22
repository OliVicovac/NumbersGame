"""
Created on 17.11.2017

@author: Michael Borko <mborko@tgm.ac.at>, Hans Brabenetz <hbrabenetz@tgm.ac.at>
@version: 20171117

@description: Implementation eines einfachen Spiels
"""

from gamecontroller import GameController
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    controller = GameController()
    controller.show()
    sys.exit(app.exec_())
