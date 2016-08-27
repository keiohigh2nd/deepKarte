#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        title = QtGui.QLabel('Disease Name')
        author = QtGui.QLabel('Intervention')
        review = QtGui.QLabel('Variable Files')

        titleEdit = QtGui.QLineEdit()
        authorEdit = QtGui.QLineEdit()
        reviewEdit = QtGui.QLineEdit()

        grid = QtGui.QVBoxLayout()

        self.groupBox = QtGui.QGroupBox("Settings")
        orivbox = QtGui.QVBoxLayout()

        layout1 = QtGui.QHBoxLayout()
        layout1.addWidget(title)
        layout1.addWidget(titleEdit)

        layout2 = QtGui.QHBoxLayout()
        layout2.addWidget(author)
        layout2.addWidget(authorEdit)

        orivbox.addLayout(layout1)
        orivbox.addLayout(layout2)

        self.groupBox.setLayout(orivbox)
        grid.addWidget(self.groupBox)

        self.groupBox2 = QtGui.QGroupBox("Files")
        mainbox = QtGui.QVBoxLayout()
        mainbox.addWidget(review)
        mainbox.addWidget(reviewEdit)
        self.groupBox2.setLayout(mainbox)
        grid.addWidget(self.groupBox2)
   
	btn1 = QtGui.QPushButton("Evaluate", self)
        btn1.move(5, 450)
     
        self.setLayout(grid) 
        self.setGeometry(400, 400, 450, 400)
        self.setWindowTitle('Outcome Evaluation')    
        self.show()


    def buttonClicked3(self, text):
        #text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Enter Patient Id')

        #病名とBoGを利用した共起表現の所
        p_index = select_similar.return_patient_index(text)
        #extract_P.show_noun(p_index)

        self.lbl.move(300, 10)
        self.lbl.setText('<a href="file:///Users/keiohigh2nd/deepKarte/view/done_parallelCoordinates.html">Patients Course</a>')
        self.lbl.setOpenExternalLinks(True)


        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
