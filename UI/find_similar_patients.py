#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
sys.path.append('src')
import select_similar, extract_P

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

	btn1 = QtGui.QPushButton("Find", self)
        btn1.move(5, 50)
        btn1.clicked.connect(self.buttonClicked1)

	btn2 = QtGui.QPushButton("Stat", self)
        btn2.move(100, 50)
        btn2.clicked.connect(self.buttonClicked2)

	btn3 = QtGui.QPushButton("Treatment", self)
        btn3.move(195, 50)
        btn3.clicked.connect(self.buttonClicked3)
      
	self.lbl = QtGui.QLabel(self)
        self.statusBar()
        
        self.setGeometry(200, 160, 300, 100)
        self.setWindowTitle('Alpha Karte')
        self.show()
        
    def buttonClicked1(self, text):
	text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter Patient Id')
	#In this function, you can pass text from str(text)
	#類似患者検索アルゴリズムの2つ
	#近傍行列に基づくもの
	#similar_pid = select_similar.find_similar_patient(text)

	#病名とBoGを利用した共起表現の所
	p_index = select_similar.return_patient_index(text)
	#extract_P.show_noun(p_index)
	#self.statusBar().showMessage(similar_pid + ' is Similar')

	self.lbl.move(10, 10)
        self.lbl.setText('<a href="file:///Users/keiohigh2nd/deepKarte/view/done_cumulativeLineChart.html">Patient Flow</a>')
        self.lbl.setOpenExternalLinks(True)


    def buttonClicked2(self, text):
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter Patient Id')

        #病名とBoGを利用した共起表現の所
        p_index = select_similar.return_patient_index(text)
        #extract_P.show_noun(p_index)

        self.lbl.move(100, 10)
        self.lbl.setText('<a href="file:///Users/keiohigh2nd/deepKarte/view/done_sunburst.html">Similar Patients</a>')
        self.lbl.setOpenExternalLinks(True)


    def buttonClicked3(self, text):
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter Patient Id')

        #病名とBoGを利用した共起表現の所
        p_index = select_similar.return_patient_index(text)
        #extract_P.show_noun(p_index)

        self.lbl.move(180, 10)
        self.lbl.setText('<a href="file:///Users/keiohigh2nd/deepKarte/view/done_parallelCoordinates.html">Patients Course</a>')
        self.lbl.setOpenExternalLinks(True)

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
