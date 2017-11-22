import sys
import unittest
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from gamecontroller import GameController

app = QtWidgets.QApplication(sys.argv)

class MyGameTestDefaultState(unittest.TestCase):

    def setUp(self):        
        self.controller = GameController()
        self.controller.show()
        self.xybh = [(130, 180, 75, 23), (210, 180, 75, 23), (290, 180, 75, 23), (370, 180, 75, 23), (450, 180, 75, 23),
        (130, 150, 75, 23), (210, 150, 75, 23), (290, 150, 75, 23), (370, 150, 75, 23), (450, 150, 75, 23),
        (130, 120, 75, 23), (210, 120, 75, 23), (290, 120, 75, 23), (370, 120, 75, 23), (450, 120, 75, 23)
        ]

    def tearDown(self):
        del self.controller
        del self.xybh

    '''
    Test the GUI in its default state
    '''
    def test_layoutButton0(self):
        '''Test the GUI in its default state'''
        self.assertEqual(self.controller.view.buttons[0].geometry(), QtCore.QRect(130, 180, 75, 23))

    def test_layoutButton1(self):
        '''Test the GUI in its default state'''
        x,y,b,h = self.xybh[1]
        self.assertEqual(self.controller.view.buttons[1].geometry(), QtCore.QRect(x, y, b, h))

    def test_layoutButton2(self):
        '''Test the GUI in its default state'''
        x,y,b,h = self.xybh[2]
        self.assertEqual(self.controller.view.buttons[2].geometry(), QtCore.QRect(x, y, b, h))

    def test_layoutButton3(self):
        '''Test the GUI in its default state'''
        x,y,b,h = self.xybh[3]
        self.assertEqual(self.controller.view.buttons[3].geometry(), QtCore.QRect(x, y, b, h))

    def test_layoutButton4(self):
        '''Test the GUI in its default state'''
        x,y,b,h = self.xybh[4]
        self.assertEqual(self.controller.view.buttons[4].geometry(), QtCore.QRect(x, y, b, h))

    def test_layoutButton5(self):
        '''Test the GUI in its default state'''
        x,y,b,h = self.xybh[5]
        self.assertEqual(self.controller.view.buttons[5].geometry(), QtCore.QRect(x, y, b, h))

    def test_layoutButton6(self):
        '''Test the GUI in its default state'''
        x,y,b,h = self.xybh[6]
        self.assertEqual(self.controller.view.buttons[6].geometry(), QtCore.QRect(x, y, b, h))

    def test_layoutButton7(self):
        '''Test the GUI in its default state'''
        x,y,b,h = self.xybh[7]
        self.assertEqual(self.controller.view.buttons[7].geometry(), QtCore.QRect(x, y, b, h))

    def test_layoutButton8(self):
        '''Test the GUI in its default state'''
        x,y,b,h = self.xybh[8]
        self.assertEqual(self.controller.view.buttons[8].geometry(), QtCore.QRect(x, y, b, h))

    def test_layoutButton9(self):
        '''Test the GUI in its default state'''
        x,y,b,h = self.xybh[9]
        self.assertEqual(self.controller.view.buttons[9].geometry(), QtCore.QRect(x, y, b, h))

    def test_layoutButton10(self):
        '''Test the GUI in its default state'''
        x,y,b,h = self.xybh[10]
        self.assertEqual(self.controller.view.buttons[10].geometry(), QtCore.QRect(x, y, b, h))

    def test_layoutButton11(self):
        '''Test the GUI in its default state'''
        x,y,b,h = self.xybh[11]
        self.assertEqual(self.controller.view.buttons[11].geometry(), QtCore.QRect(x, y, b, h))

    def test_layoutButton12(self):
        '''Test the GUI in its default state'''
        x,y,b,h = self.xybh[12]
        self.assertEqual(self.controller.view.buttons[12].geometry(), QtCore.QRect(x, y, b, h))

    def test_layoutButton13(self):
        '''Test the GUI in its default state'''
        x,y,b,h = self.xybh[13]
        self.assertEqual(self.controller.view.buttons[13].geometry(), QtCore.QRect(x, y, b, h))

    def test_layoutButton14(self):
        '''Test the GUI in its default state'''
        x,y,b,h = self.xybh[14]
        self.assertEqual(self.controller.view.buttons[14].geometry(), QtCore.QRect(x, y, b, h))

    def test_layoutAllButtons(self):
        '''Test the GUI in its default state'''
        for i in range (15):
            x,y,b,h = self.xybh[i]
            self.assertEqual(self.controller.view.buttons[i].geometry(), QtCore.QRect(x, y, b, h))

    def test_layoutLabel(self):
        self.assertEqual(self.controller.view.label.geometry(), QtCore.QRect(130, 60, 391, 31))

    def test_layoutLabel2(self):
        self.assertEqual(self.controller.view.label_2.geometry(), QtCore.QRect(20, 240, 41, 16))

    def test_layoutLabel3(self):
        self.assertEqual(self.controller.view.label_3.geometry(), QtCore.QRect(20, 210, 41, 16))

    def test_layoutLabel4(self):
        self.assertEqual(self.controller.view.label_4.geometry(), QtCore.QRect(20, 180, 41, 16))

    def test_layoutLabel5(self):
        self.assertEqual(self.controller.view.label_5.geometry(), QtCore.QRect(20, 150, 41, 16))

    def test_layoutLabel6(self):
        self.assertEqual(self.controller.view.label_6.geometry(), QtCore.QRect(20, 120, 41, 16))

    def test_lineEdit_0(self):
        self.assertEqual(self.controller.view.lineEdit_0.geometry(), QtCore.QRect(70, 120, 31, 20))

    def test_lineEdit_1(self):
        self.assertEqual(self.controller.view.lineEdit_1.geometry(), QtCore.QRect(70, 150, 31, 20))

    def test_lineEdit_2(self):
        self.assertEqual(self.controller.view.lineEdit_2.geometry(), QtCore.QRect(70, 180, 31, 20))

    def test_lineEdit_3(self):
        self.assertEqual(self.controller.view.lineEdit_3.geometry(), QtCore.QRect(70, 210, 31, 20))

    def test_lineEdit_4(self):
        self.assertEqual(self.controller.view.lineEdit_4.geometry(), QtCore.QRect(70, 240, 31, 20))

    def test_pushButton_Neu(self):
        self.assertEqual(self.controller.view.pushButton_Neu.geometry(), QtCore.QRect(210, 240, 75, 23))

    def test_pushButton_End(self):
        self.assertEqual(self.controller.view.pushButton_End.geometry(), QtCore.QRect(370, 240, 75, 23))

    def test_defaults0(self):
        '''Test the GUI in its default state'''
        self.assertEqual(self.controller.view.label_2.text(), "Spiele")

    def test_defaults1(self):
        '''Test the GUI in its default state'''
        self.assertEqual(self.controller.view.label_3.text(), "gesamt")

    def test_defaults2(self):
        '''Test the GUI in its default state'''
        self.assertEqual(self.controller.view.label_4.text(), "falsch")

    def test_defaults3(self):
        '''Test the GUI in its default state'''
        self.assertEqual(self.controller.view.label_5.text(), "korrekt")

    def test_defaults4(self):
        '''Test the GUI in its default state'''
        self.assertEqual(self.controller.view.label_6.text(), "offen")

    def test_defaults5(self):
        '''Test the GUI in its default state'''
        self.assertEqual(self.controller.view.label.text(), "<html><head/><body><p align=\"center\">Drücken Sie die Buttons in aufsteigender Richtung</p></body></html>")

    def test_defaults6(self):
        '''Test the GUI in its default state'''
        self.assertEqual(self.controller.view.pushButton_Neu.text(), "Neu")

    def test_defaults7(self):
        '''Test the GUI in its default state'''
        self.assertEqual(self.controller.view.pushButton_End.text(), "Ende")

    def test_defaults8(self):
        '''Test the GUI in its default state'''
        self.assertEqual(self.controller.Dialog.windowTitle(), "MyGame")

    def test_defaults9(self):
        '''Test the GUI in its default state'''
        self.assertEqual(self.controller.view.lineEdit_4.text(), "1")

    def test_defaults10(self):
        '''Test the GUI in its default state'''
        self.assertEqual(self.controller.view.lineEdit_0.text(), "15")

    def test_defaults11(self):
        '''Test the GUI in its default state'''
        self.assertEqual(self.controller.view.lineEdit_1.text(), "0")

    def test_defaults12(self):
        '''Test the GUI in its default state'''
        self.assertEqual(self.controller.view.lineEdit_2.text(), "0")

    def test_defaults13(self):
        '''Test the GUI in its default state'''
        self.assertEqual(self.controller.view.lineEdit_3.text(), "0")

    def test_defaultData1(self):
        self.assertEqual(self.controller.model.isCorrect, 0)

    def test_defaultData2(self):
        self.assertEqual(self.controller.model.isOpen, 15)

    def test_defaultData3(self):
        self.assertEqual(self.controller.model.isWrong, 0)

    def test_defaultData4(self):
        self.assertEqual(self.controller.model.isTotal, 0)

    def test_defaultData5(self):
        self.assertEqual(self.controller.model.Ngame, 1)

    def test_defaults14(self):
        '''Test the GUI in its default state'''
        self.assertTrue(int(self.controller.view.buttons[0].text()) in range (15))

    def test_defaults15(self):
        '''Test the GUI in its default state'''
        self.assertTrue(int(self.controller.view.buttons[1].text()) in range (15))

    def test_defaults16(self):
        '''Test the GUI in its default state'''
        self.assertTrue(int(self.controller.view.buttons[2].text()) in range (15))
        # def test_defaults17(self):
        #     '''Test the GUI in its default state'''
        self.assertTrue(int(self.controller.view.buttons[3].text()) in range (15))

    def test_defaults18(self):
        '''Test the GUI in its default state'''
        self.assertTrue(int(self.controller.view.buttons[4].text()) in range (15))
        # def test_defaults19(self):
        #     '''Test the GUI in its default state'''
        self.assertTrue(int(self.controller.view.buttons[5].text()) in range (15))

    def test_defaults20(self):
        '''Test the GUI in its default state'''
        self.assertTrue(int(self.controller.view.buttons[6].text()) in range (15))
        # def test_defaults21(self):
        #     '''Test the GUI in its default state'''
        self.assertTrue(int(self.controller.view.buttons[7].text()) in range (15))

    def test_defaults22(self):
        '''Test the GUI in its default state'''
        self.assertTrue(int(self.controller.view.buttons[8].text()) in range (15))
        # def test_defaults23(self):
        #     '''Test the GUI in its default state'''
        self.assertTrue(int(self.controller.view.buttons[9].text()) in range (15))

    def test_defaults24(self):
        '''Test the GUI in its default state'''
        self.assertTrue(int(self.controller.view.buttons[10].text()) in range (15))
        # def test_defaults25(self):
        #     '''Test the GUI in its default state'''
        self.assertTrue(int(self.controller.view.buttons[11].text()) in range (15))

    def test_defaults26(self):
        '''Test the GUI in its default state'''
        self.assertTrue(int(self.controller.view.buttons[12].text()) in range (15))
        # def test_defaults27(self):
        #     '''Test the GUI in its default state'''
        self.assertTrue(int(self.controller.view.buttons[13].text()) in range (15))

    def test_defaults28(self):
        '''Test the GUI in its default state'''
        self.assertTrue(int(self.controller.view.buttons[14].text()) in range (15))

    def test_defaultsAllButtons(self):
        '''Test the GUI in its default state'''
        for i in range(15):
            self.assertTrue(int(self.controller.view.buttons[i].text()) in range (15))

    def test_isRandom(self):
        '''Test the GUI in its default state'''
        list0 = [int(self.controller.view.buttons[i].text()) for i in range(15)]
        #print(list0)
        listCompUp = [i for i in range(15)]
        #print(listCompUp)
        self.assertTrue(list0 != listCompUp)

    def test_isRandom1(self):
        '''Test the GUI in its default state'''
        list0 = [int(self.controller.view.buttons[i].text()) for i in range(15)]
        #print(list0)
        listCompUp = [i for i in range(14, -1, -1)]
        #print(listCompUp)
        self.assertTrue(list0 != listCompUp)

    def test_isUniqueNumbers(self):
        '''Test the GUI in its default state'''
        set0 = set()
        for i in range(15):
            set0.add(int(self.controller.view.buttons[i].text()))
        #print(set0)
        self.assertTrue(len(set0) == 15)
