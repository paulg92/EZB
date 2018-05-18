# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu1.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Rectangle = QtGui.QPushButton(self.centralwidget)
        self.Rectangle.setGeometry(QtCore.QRect(80, 270, 97, 27))
        self.Rectangle.setObjectName(_fromUtf8("Rectangle"))
        self.Circle = QtGui.QPushButton(self.centralwidget)
        self.Circle.setGeometry(QtCore.QRect(250, 270, 111, 27))
        self.Circle.setObjectName(_fromUtf8("Circle"))
        self.Line = QtGui.QPushButton(self.centralwidget)
        self.Line.setGeometry(QtCore.QRect(440, 270, 97, 27))
        self.Line.setObjectName(_fromUtf8("Line"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 170, 2, 2))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(80, 40, 451, 231))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile_Menu = QtGui.QMenu(self.menubar)
        self.menuFile_Menu.setObjectName(_fromUtf8("menuFile_Menu"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionHelp_2 = QtGui.QAction(MainWindow)
        self.actionHelp_2.setObjectName(_fromUtf8("actionHelp_2"))
        self.actionAbout_GUI = QtGui.QAction(MainWindow)
        self.actionAbout_GUI.setObjectName(_fromUtf8("actionAbout_GUI"))
        self.actionDocumentation = QtGui.QAction(MainWindow)
        self.actionDocumentation.setObjectName(_fromUtf8("actionDocumentation"))
        self.actionFAQ = QtGui.QAction(MainWindow)
        self.actionFAQ.setObjectName(_fromUtf8("actionFAQ"))
        self.menuFile_Menu.addSeparator()
        self.menuFile_Menu.addAction(self.actionOpen)
        self.menuFile_Menu.addSeparator()
        self.menuFile_Menu.addAction(self.actionSave)
        self.menuFile_Menu.addAction(self.actionSave_As)
        self.menuFile_Menu.addSeparator()
        self.menuFile_Menu.addAction(self.actionQuit)
        self.menuFile_Menu.addSeparator()
        self.menuAbout.addSeparator()
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout_GUI)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionFAQ)
        self.menubar.addAction(self.menuFile_Menu.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "GUI", None))
        self.Rectangle.setText(_translate("MainWindow", "Rectangle", None))
        self.Circle.setText(_translate("MainWindow", "Circle", None))
        self.Line.setText(_translate("MainWindow", "Line", None))
        self.menuFile_Menu.setTitle(_translate("MainWindow", "File Menu", None))
        self.menuAbout.setTitle(_translate("MainWindow", "Help", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionSave.setText(_translate("MainWindow", "Save As", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionHelp_2.setText(_translate("MainWindow", "Help", None))
        self.actionAbout_GUI.setText(_translate("MainWindow", "About GUI", None))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation", None))
        self.actionFAQ.setText(_translate("MainWindow", "FAQ", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

