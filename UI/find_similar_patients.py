#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example, we determine the event sender
object.

author: Jan Bodnar
website: zetcode.com 
last edited: October 2011
"""

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

	btn = QtGui.QPushButton("Find", self)
        btn.move(150, 50)
        text = btn.clicked.connect(self.buttonClicked)
      
        self.statusBar()
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Find Similar Patients')
        self.show()
        
    def buttonClicked(self, text):
	text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
	#In this function, you can pass text from str(text)
	return str(text)

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
