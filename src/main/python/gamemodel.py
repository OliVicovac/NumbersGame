"""
Created on 17.11.2017

@author: Michael Borko <mborko@tgm.ac.at>, Hans Brabenetz <hbrabenetz@tgm.ac.at>
@version: 20171117

@description: Implementation eines einfachen Spiels
              
"""

class GameModel(object):
    """
        GameModel
        Das GameModel wird mit der Funktion :func:`__init__` gestartet
            - **Methoden**:
                * :func:`GameModel.new_game`: Aktualisiert Statistik für neues Spiel
        """

    def __init__(self):
        """
        Konstruktor
        """
        self.isCorrect = 0
        self.isOpen = 15
        self.isWrong = 0
        self.isTotal = 0
        self.Ngame = 1
        self.nextValue = 0


    def new_game(self):
        """
        Aktualisiert neue Statistik für neues Spiel
        :return: nichts
        """
        self.Ngame += 1
        self.isCorrect = 0
        self.isOpen = 15
        self.isWrong = 0
        self.isTotal = 0
        self.nextValue = 0

