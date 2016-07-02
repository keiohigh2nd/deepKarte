#encoding:utf-8
import sys
from PyQt4 import QtGui,QtWebKit,QtCore
class Example(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)
        self.resize(150, 150)
        self.setWindowTitle("msb")
        self.web = QtWebKit.QWebView(self)
        self.web.load(QtCore.QUrl("http://google.com"))
        #self.web.setUrl(QtCore.QUrl("http://google.com")) #代替になると書かれているけどどこかに差があったりするのかな
        self.show()

def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
