# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ClassicMenu(object):
    def setupUi(self, ClassicMenu):
        ClassicMenu.setObjectName(_fromUtf8("ClassicMenu"))
        ClassicMenu.resize(616, 504)
        self.centralwidget = QtGui.QWidget(ClassicMenu)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.circle = QtGui.QPushButton(self.centralwidget)
        self.circle.setObjectName(_fromUtf8("circle"))
        self.horizontalLayout_2.addWidget(self.circle)
        self.rectangle = QtGui.QPushButton(self.centralwidget)
        self.rectangle.setObjectName(_fromUtf8("rectangle"))
        self.horizontalLayout_2.addWidget(self.rectangle)
        ClassicMenu.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(ClassicMenu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 616, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile_open = QtGui.QMenu(self.menubar)
        self.menuFile_open.setObjectName(_fromUtf8("menuFile_open"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        ClassicMenu.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(ClassicMenu)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        ClassicMenu.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(ClassicMenu)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(ClassicMenu)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionAbout = QtGui.QAction(ClassicMenu)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout_2 = QtGui.QAction(ClassicMenu)
        self.actionAbout_2.setObjectName(_fromUtf8("actionAbout_2"))
        self.actionExit = QtGui.QAction(ClassicMenu)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionAbout_3 = QtGui.QAction(ClassicMenu)
        self.actionAbout_3.setObjectName(_fromUtf8("actionAbout_3"))
        self.menuFile_open.addSeparator()
        self.menuFile_open.addAction(self.actionOpen)
        self.menuFile_open.addAction(self.actionSave)
        self.menuFile_open.addSeparator()
        self.menuFile_open.addSeparator()
        self.menuFile_open.addAction(self.actionExit)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_3)
        self.menubar.addAction(self.menuFile_open.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(ClassicMenu)
        QtCore.QMetaObject.connectSlotsByName(ClassicMenu)

    def retranslateUi(self, ClassicMenu):
        ClassicMenu.setWindowTitle(_translate("ClassicMenu", "Classic Menu", None))
        self.circle.setText(_translate("ClassicMenu", "Circle", None))
        self.rectangle.setText(_translate("ClassicMenu", "Rectangle", None))
        self.menuFile_open.setTitle(_translate("ClassicMenu", "File", None))
        self.menuHelp.setTitle(_translate("ClassicMenu", "Help", None))
        self.actionOpen.setText(_translate("ClassicMenu", "Open", None))
        self.actionSave.setText(_translate("ClassicMenu", "Save", None))
        self.actionAbout.setText(_translate("ClassicMenu", "About", None))
        self.actionAbout_2.setText(_translate("ClassicMenu", "About", None))
        self.actionExit.setText(_translate("ClassicMenu", "Exit", None))
        self.actionAbout_3.setText(_translate("ClassicMenu", "About", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ClassicMenu = QtGui.QMainWindow()
    ui = Ui_ClassicMenu()
    ui.setupUi(ClassicMenu)
    ClassicMenu.show()
    sys.exit(app.exec_())

