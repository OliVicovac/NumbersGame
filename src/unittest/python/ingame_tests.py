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
    Now lets have fun, lets play
    Test the GUI in game...
    '''

    def test_ClickButtonNum0(self):
        ''' Test the GUI in game '''
        p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == 0]
        #print("Button with 0 is ", str(p))
        self.controller.view.buttons[p[0]].click()
        self.assertTrue(self.controller.model.isCorrect == 1)

    def test_ClickButtonNum01(self):
        ''' Test the GUI in game '''
        p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == 0]
        #print("Button with 0 is ", str(p))
        self.controller.view.buttons[p[0]].click()
        self.assertTrue(self.controller.model.isCorrect == 1)
        p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == 1]
        #print("Button with 0 is ", str(p))
        self.controller.view.buttons[p[0]].click()
        self.assertTrue(self.controller.model.isCorrect == 2)

    def test_ClickAllButtonsCorrectly(self):
        ''' Test the GUI in game '''
        for g in range (15):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            #print("Button with ", str(g), " is ", str(p))
            self.controller.view.buttons[p[0]].click()
            self.assertTrue(self.controller.model.isCorrect == g+1)

    def test_ClickAllButtonsCorrectly2(self):
        ''' Test the GUI in game '''
        for g in range (15):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            #print("Button with ", str(g), " is ", str(p))
            self.controller.view.buttons[p[0]].click()
            self.assertTrue(self.controller.model.isTotal == g+1)

    def test_ClickAllButtonsCorrectly3(self):
        ''' Test the GUI in game '''
        for g in range (15):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            #print("Button with ", str(g), " is ", str(p))
            self.controller.view.buttons[p[0]].click()
            self.assertTrue(self.controller.model.isOpen == 14-g)

    def test_ClickAllButtonsCorrectly4(self):
        ''' Test the GUI in game '''
        for g in range (15):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            #print("Button with ", str(g), " is ", str(p))
            self.controller.view.buttons[p[0]].click()
            self.assertTrue(self.controller.model.isWrong == 0)

    def test_ClickAllButtonsCorrectly5(self):
        ''' Test the GUI in game '''
        for g in range (15):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            #print("Button with ", str(g), " is ", str(p))
            self.controller.view.buttons[p[0]].click()
            self.assertTrue(self.controller.model.Ngame == 1)

    def test_ClickWrongButtonNum0(self):
        ''' Test the GUI in game '''
        p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == 0]
        #print("Button with 0 is ", str(p))
        self.controller.view.buttons[(p[0]+1)%15].click()
        self.assertTrue(self.controller.model.isCorrect == 0)
        self.assertTrue(self.controller.model.isWrong == 1)
        self.assertTrue(self.controller.model.isOpen == 15)
        self.assertTrue(self.controller.model.isTotal == 1)
        self.assertTrue(self.controller.model.Ngame == 1)

    def test_Click30TimesWrongButton(self):
        ''' Test the GUI in game '''
        for e in range(30):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == 0]
            #print("Button with 0 is ", str(p))
            self.controller.view.buttons[(p[0]+2)%15].click()
            self.assertTrue(self.controller.model.isCorrect == 0)
            self.assertTrue(self.controller.model.isWrong == e+1)
            self.assertTrue(self.controller.model.isOpen == 15)
            self.assertTrue(self.controller.model.isTotal == e+1)
            self.assertTrue(self.controller.model.Ngame == 1)

    def test_Click3TimesWrongThenStartaNewErrorFreeGame(self):
        ''' Test the GUI in game '''
        for e in range(3):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == 0]
            #print("Button with 0 is ", str(p))
            self.controller.view.buttons[(p[0]+2)%15].click()
            self.assertTrue(self.controller.model.isCorrect == 0)
            self.assertTrue(self.controller.model.isWrong == e+1)
            self.assertTrue(self.controller.model.isOpen == 15)
            self.assertTrue(self.controller.model.isTotal == e+1)
            self.assertTrue(self.controller.model.Ngame == 1)
        self.controller.view.pushButton_Neu.click()
        for g in range (15):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            #print("Button with ", str(g), " is ", str(p))
            self.controller.view.buttons[p[0]].click()
            self.assertTrue(self.controller.model.isOpen == 14-g)
            self.assertTrue(self.controller.model.isCorrect == g+1)
            self.assertTrue(self.controller.model.isWrong == 0)
            self.assertTrue(self.controller.model.isTotal == g+1)
            self.assertTrue(self.controller.model.Ngame == 2)

    def test_Click10timesNewGameOnly(self):
        ''' Test the GUI in game '''
        for g in range (10):
            self.controller.view.pushButton_Neu.click()
            self.assertTrue(self.controller.model.isOpen == 15)
            self.assertTrue(self.controller.model.isCorrect == 0)
            self.assertTrue(self.controller.model.isWrong == 0)
            self.assertTrue(self.controller.model.isTotal == 0)
            self.assertTrue(self.controller.model.Ngame == g+2)

    def test_DispClickButtonNum0(self):
        ''' Test the GUI in game '''
        p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == 0]
        self.controller.view.buttons[p[0]].click()
        self.assertEqual(self.controller.view.lineEdit_1.text(), "1")

    def test_DispClickButtonNum01(self):
        ''' Test the GUI in game '''
        p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == 0]
        self.controller.view.buttons[p[0]].click()
        self.assertEqual(self.controller.view.lineEdit_1.text(), "1")
        p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == 1]
        self.controller.view.buttons[p[0]].click()
        self.assertEqual(self.controller.view.lineEdit_1.text(), "2")


    def test_DispClickAllButtonsCorrectly(self):
        ''' Test the GUI in game '''
        for g in range (15):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.controller.view.buttons[p[0]].click()
            self.assertEqual(int(self.controller.view.lineEdit_1.text()), g+1)


    def test_DispClickAllButtonsCorrectly2(self):
        ''' Test the GUI in game '''
        for g in range (15):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.controller.view.buttons[p[0]].click()
            self.assertEqual(int(self.controller.view.lineEdit_3.text()), g+1)

    def test_DispClickAllButtonsCorrectly3(self):
        ''' Test the GUI in game '''
        for g in range (15):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.controller.view.buttons[p[0]].click()
            self.assertEqual(int(self.controller.view.lineEdit_0.text()), 14-g)
            self.assertEqual(int(self.controller.view.lineEdit_2.text()), 0)
            self.assertEqual(int(self.controller.view.lineEdit_4.text()), 1) 
        
    def test_DispClickWrongButtonNum0(self):
        ''' Test the GUI in game '''
        p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == 0]
        self.controller.view.buttons[(p[0]+1)%15].click()
        self.assertEqual(int(self.controller.view.lineEdit_0.text()), 15) #op
        self.assertEqual(int(self.controller.view.lineEdit_1.text()), 0) #correct
        self.assertEqual(int(self.controller.view.lineEdit_2.text()), 1) #wrong
        self.assertEqual(int(self.controller.view.lineEdit_3.text()), 1) #total
        self.assertEqual(int(self.controller.view.lineEdit_4.text()), 1) #Ngame

    def test_DispClick30TimesWrongButton(self):
        ''' Test the GUI in game '''
        for e in range(30):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == 0]
            self.controller.view.buttons[(p[0]+2)%15].click()
            self.assertEqual(int(self.controller.view.lineEdit_0.text()), 15) #op
            self.assertEqual(int(self.controller.view.lineEdit_1.text()), 0) #correct
            self.assertEqual(int(self.controller.view.lineEdit_2.text()), e+1) #wrong
            self.assertEqual(int(self.controller.view.lineEdit_3.text()), e+1) #total
            self.assertEqual(int(self.controller.view.lineEdit_4.text()), 1) #Ngame

    def test_DispClick3TimesWrongThenStartaNewErrorFreeGame(self):
        ''' Test the GUI in game '''
        for e in range(3):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == 0]
            self.controller.view.buttons[(p[0]+2)%15].click()
            self.assertEqual(int(self.controller.view.lineEdit_0.text()), 15) #op
            self.assertEqual(int(self.controller.view.lineEdit_1.text()), 0) #correct
            self.assertEqual(int(self.controller.view.lineEdit_2.text()), e+1) #wrong
            self.assertEqual(int(self.controller.view.lineEdit_3.text()), e+1) #total
            self.assertEqual(int(self.controller.view.lineEdit_4.text()), 1) #Ngame
        self.controller.view.pushButton_Neu.click()
        for g in range (15):
            p = [i for i in range(15) if int(self.controller.view.buttons[i].text()) == g]
            self.controller.view.buttons[p[0]].click()
            self.assertEqual(int(self.controller.view.lineEdit_0.text()), 14-g) #op
            self.assertEqual(int(self.controller.view.lineEdit_1.text()), g+1) #correct
            self.assertEqual(int(self.controller.view.lineEdit_2.text()), 0) #wrong
            self.assertEqual(int(self.controller.view.lineEdit_3.text()), g+1) #total
            self.assertEqual(int(self.controller.view.lineEdit_4.text()), 2) #Ngame


    def test_DispClick10timesNewGameOnly(self):
        ''' Test the GUI in game '''
        for g in range (10):
            self.controller.view.pushButton_Neu.click()
            self.assertEqual(int(self.controller.view.lineEdit_0.text()), 15) #op
            self.assertEqual(int(self.controller.view.lineEdit_1.text()), 0) #correct
            self.assertEqual(int(self.controller.view.lineEdit_2.text()), 0) #wrong
            self.assertEqual(int(self.controller.view.lineEdit_3.text()), 0) #total
            self.assertEqual(int(self.controller.view.lineEdit_4.text()), g+2) #Ngame
