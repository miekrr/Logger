#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

This example shows
how to use QtGui.QComboBox widget.
 
author: Jan Bodnar
website: zetcode.com 
last edited: September 2011
"""

import sys
from PyQt4 import QtGui, QtCore

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

WINDOW_TITLE = "AVAYA Logger"

list_data = [
    "kasdkfkaksdflkaj sdfklasdf",
    "aslkdfjaskdfjasldflkasdf",
    "0129394saodfjasdfjasldfjfasdlfasdfl",
    "09asd8f-0a8sfj2oj34o2342p3r",
    "23900000000000000000000004",
    "fjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj",
    "111111111111111111111111111111111111111"
]

class MyModel(QtCore.QAbstractListModel):
    def __init__(self,data=[],parent=None):
        QtCore.QAbstractListModel.__init__(self,parent)
        self._data=data

    def rowCount(self,parent):
        return len(self._data)

    def data(self,index,role):

        if role==QtCore.Qt.DisplayRole:
            return self._data[index.row()]


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def combo_box(self, From):
        self.combo = QtGui.QComboBox(Form)
        self.combo.move(140, 0)
        self.combo.addItem("Gentoo")
        self.combo.activated[str].connect(self.onActivated)

    def onActivated(self, text):
        pass

    def setupUi(self, Form):
        self.combo_box()
        Form.resize(640, 480)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        #self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listView = QtGui.QListView(Form)
        #self.listView.setObjectName(_fromUtf8("listView"))

        self.verticalLayout.addWidget(self.combo)
        self.verticalLayout.addWidget(self.listView)
        #self.lineEdit = QtGui.QLineEdit(Form)
        #self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        #self.verticalLayout.addWidget(self.lineEdit)
        data=["one","two","three","four"]
        model=MyModel(data)
        self.listView.setModel(model)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        #QtCore.QObject.connect(self.listView ,     QtCore.SIGNAL(_fromUtf8("listclicked()")),self.PrintIT)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))

    def PrintIT(self,selected):
        #print "Asdf"
        self.lineEdit.text(str(self.listView.selectedItem()))


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(WINDOW_TITLE)
        self.show()
        
                
def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()