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
        MainWindow.resize(775, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 4)
        self.Line = QtGui.QPushButton(self.centralwidget)
        self.Line.setObjectName(_fromUtf8("Line"))
        self.gridLayout.addWidget(self.Line, 1, 0, 1, 1)
        self.Polygon = QtGui.QPushButton(self.centralwidget)
        self.Polygon.setObjectName(_fromUtf8("Polygon"))
        self.gridLayout.addWidget(self.Polygon, 1, 1, 1, 1)
        self.Triangle = QtGui.QPushButton(self.centralwidget)
        self.Triangle.setObjectName(_fromUtf8("Triangle"))
        self.gridLayout.addWidget(self.Triangle, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 775, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile_Menu = QtGui.QMenu(self.menubar)
        self.menuFile_Menu.setObjectName(_fromUtf8("menuFile_Menu"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
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
        self.PenWidth = QtGui.QAction(MainWindow)
        self.PenWidth.setObjectName(_fromUtf8("PenWidth"))
        self.PenColor = QtGui.QAction(MainWindow)
        self.PenColor.setObjectName(_fromUtf8("PenColor"))
        self.Clear_Screen = QtGui.QAction(MainWindow)
        self.Clear_Screen.setObjectName(_fromUtf8("Clear_Screen"))
        self.actionRectangle = QtGui.QAction(MainWindow)
        self.actionRectangle.setObjectName(_fromUtf8("actionRectangle"))
        self.actionCircle = QtGui.QAction(MainWindow)
        self.actionCircle.setObjectName(_fromUtf8("actionCircle"))
        self.actionHello = QtGui.QAction(MainWindow)
        self.actionHello.setObjectName(_fromUtf8("actionHello"))
        self.menuFile_Menu.addSeparator()
        self.menuFile_Menu.addAction(self.actionOpen)
        self.menuFile_Menu.addSeparator()
        self.menuFile_Menu.addSeparator()
        self.menuFile_Menu.addAction(self.actionSave)
        self.menuFile_Menu.addSeparator()
        self.menuFile_Menu.addAction(self.actionQuit)
        self.menuAbout.addSeparator()
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout_GUI)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionFAQ)
        self.menuOptions.addAction(self.PenWidth)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.PenColor)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.Clear_Screen)
        self.menubar.addAction(self.menuFile_Menu.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "GUI", None))
        self.Line.setText(_translate("MainWindow", "Line", None))
        self.Polygon.setText(_translate("MainWindow", "Polygon", None))
        self.Triangle.setText(_translate("MainWindow", "Triangle", None))
        self.menuFile_Menu.setTitle(_translate("MainWindow", "File Menu", None))
        self.menuAbout.setTitle(_translate("MainWindow", "Help", None))
        self.menuOptions.setTitle(_translate("MainWindow", "Options", None))
        self.actionOpen.setText(_translate("MainWindow", "Open Ctrl-O", None))
        self.actionSave.setText(_translate("MainWindow", "Save As Ctrl-S", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit Ctrl-Q", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionHelp_2.setText(_translate("MainWindow", "Help", None))
        self.actionAbout_GUI.setText(_translate("MainWindow", "About GUI", None))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation", None))
        self.actionFAQ.setText(_translate("MainWindow", "FAQ", None))
        self.PenWidth.setText(_translate("MainWindow", "Pen width", None))
        self.PenColor.setText(_translate("MainWindow", "Pen color", None))
        self.Clear_Screen.setText(_translate("MainWindow", "Clear Screen Ctrl-L", None))
        self.actionRectangle.setText(_translate("MainWindow", "Rectangle", None))
        self.actionCircle.setText(_translate("MainWindow", "Circle", None))
        self.actionHello.setText(_translate("MainWindow", "hello", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

