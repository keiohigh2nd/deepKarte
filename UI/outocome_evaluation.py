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
        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('Outcome Evaluation')    
	QtCore.QTextCodec.setCodecForCStrings( QtCore.QTextCodec.codecForLocale() )

        self.combo = QtGui.QComboBox(self)
        self.combo.addItem("Choose or Write")
        self.combo.addItem("Cataract")
        self.combo.addItem("PCI")
	self.combo.move(10,10)

	self.textbox = QtGui.QLineEdit(self)
	self.textbox.setText("例) Xのうち、Yをした割合")
        self.textbox.move(10,50)
        self.textbox.resize(140,20)

	btn = QtGui.QPushButton("Check", self)
        btn.move(30, 150)
        btn.clicked.connect(self.buttonClicked)

	self.lbl = QtGui.QLabel(self)
        self.statusBar()

        self.show()

    def buttonClicked(self, text):
	text = str(self.combo.currentText())
	if text.find("Choose") == 0:
		text = str(self.textbox.text())

	print text
        self.lbl.move(50, 200)
        self.lbl.setText('<a href="file:///Users/keiohigh2nd/deepKarte/view/done_cumulativeLineChart.html">Patient Flow</a>')
        self.lbl.setOpenExternalLinks(True)


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

