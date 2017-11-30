"""
Created on 17.11.2017

@author: Michael Borko <mborko@tgm.ac.at>, Hans Brabenetz <hbrabenetz@tgm.ac.at>
@version: 20171117

@description: Implementation eines einfachen Spiels
              
"""

class GameModel(object):

    def __init__(self):
        self.isCorrect = 0
        self.isOpen = 15
        self.isWrong = 0
        self.isTotal = 0
        self.Ngame = 1
        self.nextValue = 0


    def new_game(self):
        pass

