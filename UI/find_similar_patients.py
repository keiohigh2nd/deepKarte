#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
sys.path.append('src')
import select_similar

class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

	btn = QtGui.QPushButton("Find", self)
        btn.move(50, 50)
        btn.clicked.connect(self.buttonClicked)
      
	self.lbl = QtGui.QLabel(self)
        self.statusBar()
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Alpha Karte')
        self.show()
        
    def buttonClicked(self, text):
	text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter Patient Id')
	#In this function, you can pass text from str(text)
	pid = select_similar.find_similar_patient(text)
	self.statusBar().showMessage(pid + ' is Similar')

	#self.lbl.move(10, 10)
        #self.lbl.setText('<a href="http://0.0.0.0:5601/app/kibana#/doc/test/test/karte?id=%s">Stackoverflow/</a>'%pid)
        #self.lbl.setOpenExternalLinks(True)
	return str(text)

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
