#!/usr/bin/#!/usr/bin/env python3
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
def myfunc():
    print("Hello World!")

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ClassicMenu(object):
    def circleDraw(self):
        print("You want to print a circle!")
    def rectangleDraw(self):
        print("You want to print a rectangle!")
    # def exitClicked(self):
    #     print("You want to quit")
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
            ### Button Event Circle #############
        self.circle.clicked.connect(self.circleDraw)
        ###########################################
        self.rectangle = QtGui.QPushButton(self.centralwidget)
        self.rectangle.setObjectName(_fromUtf8("rectangle"))
        self.horizontalLayout_2.addWidget(self.rectangle)
            ### Button Event Rectangle #############
        self.rectangle.clicked.connect(self.rectangleDraw)
        ###########################################
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
        ##### Action Open
        self.actionOpen = QtGui.QAction(ClassicMenu)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpen.setShortcut('Ctrl+O')
        self.actionOpen.setStatusTip('Open application')
        self.actionOpen.triggered.connect(self.file_open)
        ###### Save
        self.actionSave = QtGui.QAction(ClassicMenu)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave.triggered.connect(self.save)

        self.actionAbout = QtGui.QAction(ClassicMenu)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionAbout_2 = QtGui.QAction(ClassicMenu)
        self.actionAbout_2.setObjectName(_fromUtf8("actionAbout_2"))
        ############
        self.actionExit = QtGui.QAction(ClassicMenu)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.setStatusTip('Exit application')
        self.actionExit.triggered.connect(QtGui.qApp.quit)
        ###########
        self.actionAbout_3 = QtGui.QAction(ClassicMenu)
        self.actionAbout_3.setObjectName(_fromUtf8("actionAbout_3"))
        self.actionAbout_3.triggered.connect(self.about)
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

    def save(self):
        f = open(self.afilename, "w")
        f.write(self.textEdit.toPlainText())
        f.close()
        sel.statusbar.showMessage("File saved.")

    def about(self):
        QtGui.QMessageBox.about(None,"About","Paul GUI 2018")

    def file_open(self):
        self.afilename = QtGui.QFileDialog.getOpenFileName(None,"Open File")
        f = open(self.afilename,"r")

        self.editor()

        with f:
            text = f.read()
            self.textEdit.setText(text)


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
