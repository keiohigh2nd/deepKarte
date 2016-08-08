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
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Outcome Evaluation')    

        self.combo = QtGui.QComboBox(self)
        self.combo.addItem("Cataract")
        self.combo.addItem("PCI")
	self.combo.move(10,10)

	text = str(self.combo.currentText())
	btn = QtGui.QPushButton("Check", self)
        btn.move(30, 50)
        btn.clicked.connect(self.buttonClicked)

	self.lbl = QtGui.QLabel(self)
        self.statusBar()

        self.show()

    def buttonClicked(self, text):
	text = str(self.combo.currentText())
	print text
        self.lbl.move(50, 100)
        self.lbl.setText('<a href="file:///Users/keiohigh2nd/deepKarte/view/done_cumulativeLineChart.html">Patient Flow</a>')
        self.lbl.setOpenExternalLinks(True)


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

