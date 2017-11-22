import sys
import unittest
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from gamecontroller import GameController

app = QtWidgets.QApplication(sys.argv)

class MyGameTestDefaultState(unittest.TestCase):

    def setUp(self):        
        self.controller = GameController()
        self.controller.show()

    def tearDown(self):
        del self.controller

    '''
    Now lets test the more difficult stuff
    EK, Test the GUI in game...
    '''
    def test_hasFocus(self):
        '''Test the GUI in its default state'''
        # when we start the game, has Button '0' the focus?
        for i in range(15):
            if int(self.controller.view.buttons[i].text()) == 0:
                self.assertTrue(self.controller.view.buttons[i].hasFocus())

    def test_hasFocus1(self):
        #after successfully clicing 5 times, does button 4 have the focus?
        for g in range(5):
            p = [i for i in range(15) if (int(self.controller.view.buttons[i].text()) == g)]
            #self.controller.show()
            self.controller.view.buttons[p[0]].click()
            #self.assertTrue(self.controller.view.buttons[p[0]].hasFocus())
        for i in range(15):
            if int(self.controller.view.buttons[i].text()) == 4:
                self.assertTrue(self.controller.view.buttons[i].hasFocus())

    def test_hasFocus2(self):
        # clicking the right buttons all along
        # when we start the game, has Button '0' the focus and each correctly clicked button afterwards has focus ?
        for g in range(14): #the 14th button will be disabled immediately so cannot have focus anymore
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            #self.controller.show()
            self.controller.view.buttons[p[0]].click()
            self.assertTrue(self.controller.view.buttons[p[0]].hasFocus())

    def test_hasFocus3(self):
        # clicking whatever buttons all along
        # when we play the game, each clicked button has focus ?
        for g in range(50): #Attention, somewhen this might eventually fail bec a shuffle will come in its way
            self.controller.show() # show is needed for so many clicks. Until ~range 20 it will do without show
            self.controller.view.buttons[g%15].click()
            self.assertTrue(self.controller.view.buttons[g%15].hasFocus())

    def test_hasFocus4(self):
        # clicking whatever buttons all along
        # when we play the game, each clicked button has focus ?
        #self.controller.view.timer.stop()
        for g in range(50): 
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g%15]
            self.controller.show() # show is needed for so many clicks. Until ~range 20 it will do without show
            self.controller.view.buttons[p[0]].click()
            #time.sleep(1)   
            self.assertTrue(self.controller.view.buttons[p[0]].hasFocus())         

    def test_hasFocus5(self):
        # Are all buttons without focus after successful 7 clicks, a reShuffle and a successful finish
        for g in range(7):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.controller.view.buttons[p[0]].click()
        self.controller.reshuffle()
        for g in range(7, 15):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.controller.view.buttons[p[0]].click()
        for i in range(15):
            #if int(self.controller.view.buttons[i].text()) == 0:
                self.assertTrue(self.controller.view.buttons[i].hasFocus() == False)

    def test_hasFocus6(self):
        # After a reShuffle when Button 6 had focus before, does it still have focus afterwards?
        for g in range(6, 7):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.controller.view.buttons[p[0]].click()
            self.assertTrue(self.controller.view.buttons[p[0]].hasFocus())
        self.controller.reshuffle()
        for g in range(6, 7):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.controller.view.buttons[p[0]].click()
            self.assertTrue(self.controller.view.buttons[p[0]].hasFocus())

    def test_hasFocus7(self):
        # Are all buttons with focus during successful 7 clicks, a reShuffle and a successful continuation
        # but the very last button looses its focus when clicked since it gets disable immediaely!
        for g in range(7):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.controller.view.buttons[p[0]].click()
            self.assertTrue(self.controller.view.buttons[p[0]].hasFocus())
        self.controller.reshuffle()
        for g in range(6,14):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.controller.view.buttons[p[0]].click()
            self.assertTrue(self.controller.view.buttons[p[0]].hasFocus())
        for g in range(14,15):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.controller.view.buttons[p[0]].click()
            self.assertTrue(self.controller.view.buttons[p[0]].hasFocus() == False)


    def test_isDisabled(self):
        # is button 0 disabled after button 0 and button 1 was hitted successfully? 
        for g in range(2):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.controller.view.buttons[p[0]].click()
        for i in range (15):
            if int(self.controller.view.buttons[i].text()) == 0:
                self.assertTrue(self.controller.view.buttons[i].isEnabled() == False)

    def test_isDisabled1(self):
        # is button 0 to 5 disabled after button 6 was hitted successfully? 
        # but button 6 is not yet disabled
        # all remaining buttons are still enabled
        for g in range(7):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.controller.view.buttons[p[0]].click()
        for g in range(6):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.assertTrue(self.controller.view.buttons[p[0]].isEnabled() == False)
        for g in range(6,7):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.assertTrue(self.controller.view.buttons[p[0]].isEnabled() == True)
        for g in range(7, 15):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.assertTrue(self.controller.view.buttons[p[0]].isEnabled() == True)

    def test_isDisabled2(self):
        # is button 0 to 5 disabled after button 6 was hitted successfully? 
        # but button 6 is not yet disabled
        # not button 7 is hitted correctly now
        # is Button 6 now disabled?
        for g in range(7):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.controller.view.buttons[p[0]].click()
        for g in range(6):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.assertTrue(self.controller.view.buttons[p[0]].isEnabled() == False)
        for g in range(6, 7):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.assertTrue(self.controller.view.buttons[p[0]].isEnabled() == True)
        for g in range(7, 8):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.controller.view.buttons[p[0]].click()
        for g in range(6, 7):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.assertTrue(self.controller.view.buttons[p[0]].isEnabled() == False)

    def test_isDisabled3(self):
        # is button 0 to 5 disabled after button 6 was hitted successfully? 
        # but button 6 is not yet disabled
        # not button 10 is hitted in error
        # is Button 6 still enabled?
        for g in range(7):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.controller.view.buttons[p[0]].click()
        for g in range(6):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.assertTrue(self.controller.view.buttons[p[0]].isEnabled() == False)
        for g in range(6, 7):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.assertTrue(self.controller.view.buttons[p[0]].isEnabled() == True)
        for g in range(10, 11):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.controller.view.buttons[p[0]].click()
        for g in range(6, 7):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.assertTrue(self.controller.view.buttons[p[0]].isEnabled() == True)

    def test_isDisabled4(self):
        # Are all buttons disabled after a successful run?
        for g in range(15):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.controller.view.buttons[p[0]].click()
        for i in range (15):
            #if int(self.controller.view.buttons[i].text()) == 0:
                self.assertTrue(self.controller.view.buttons[i].isEnabled() == False)

    def test_isDisabled5(self):
        # Are all buttons disabled after a successful 7 clicks, a reShuffle and a successful finish
        for g in range(7):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.controller.view.buttons[p[0]].click()
        self.controller.reshuffle()
        for g in range(7,15):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.controller.view.buttons[p[0]].click()
        for i in range (15):
            #if int(self.controller.view.buttons[i].text()) == 0:
                self.assertTrue(self.controller.view.buttons[i].isEnabled() == False)

    '''
    EK is there a timer to reshuffle the numbers in game?
    '''
    def test_isthereaTimer(self):
        self.assertIsNone(self.controller.view.timer.stop())

    def test_Timer1(self):
        self.assertTrue(self.controller.view.timer.interval() == 2000)

    def test_Timer2(self):
        self.assertIsNone(self.controller.view.timer.start())

    def test_Timer3(self):
        # does the timer call reShuffle and does reShuffle really shuffle?
        list0 = [int(self.controller.view.buttons[i].text()) for i in range(15)]
        #print(list0)
        self.assertIsNone(self.controller.view.timer.setInterval(1))
        #self.controller.reShuffle()
        self.controller.show() 
        list1 = [int(self.controller.view.buttons[i].text()) for i in range(15)]
        #print(list1)
        #print("Intervall = ", str(self.controller.view.timer.interval()))
        self.assertTrue(list0 != list1)

    def test_Timer4(self):
        self.assertIsNone(self.controller.view.timer.setInterval(2000))

    def test_Timer5(self):
        self.assertIsNone(self.controller.view.timer.start())
