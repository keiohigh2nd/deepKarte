# -*- coding: utf-8 -*-
import sys, datetime
from PyQt4 import QtGui,QtWebKit,QtCore

class Browser(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Browser, self).__init__(parent)
        self.resize(150, 150)
        self.setWindowTitle("msb")
        self.web = QtWebKit.QWebView(self)
        self.web.load(QtCore.QUrl("http://google.com"))
        #self.web.setUrl(QtCore.QUrl("http://google.com")) #代替になると書かれているけどどこかに差があったりするのかな
        self.show()

class Tab1Widget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Tab1Widget, self).__init__()
        closeBtn = QtGui.QPushButton('Treatment')
        closeBtn.clicked.connect(parent.close)
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(closeBtn)
        self.setLayout(hbox)

class Tab2Widget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Tab2Widget, self).__init__()
        closeBtn = QtGui.QPushButton('Statistics')
        closeBtn.clicked.connect(parent.close)
        closeBtn2 = QtGui.QPushButton('Similar Patients')
        closeBtn.clicked.connect(parent.close)
        closeBtn3 = QtGui.QPushButton('Treatment')
        closeBtn.clicked.connect(self.browse)

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(closeBtn)
        hbox.addWidget(closeBtn2)
        hbox.addWidget(closeBtn3)
        self.setLayout(hbox)

    def browse(self):
	super(Tab2Widget, self).__init__()
	self.resize(150, 150)
        self.setWindowTitle("msb")
        self.web = QtWebKit.QWebView(self)
        self.web.load(QtCore.QUrl("http://google.com"))
        #self.web.setUrl(QtCore.QUrl("http://google.com")) #代替になると書かれているけどどこかに差があったりするのかな
        self.show()

class UI(QtGui.QWidget):
    def __init__(self):
        super(UI, self).__init__()
        self.initUI()

    def initUI(self):
        qtab = QtGui.QTabWidget()
        #qtab.addTab(Tab1Widget(parent=self), 'Function1')
        qtab.addTab(Tab2Widget(parent=self), 'Basic Function')

        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(qtab)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('DeepKarte')
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ui = UI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
