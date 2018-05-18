from PyQt4 import QtGui  # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication

import design  # This file holds our MainWindow and all design related things

# it also keeps events etc that we defined in Qt Designer
import os  # For listing directory methods
import graphicsview
import re

class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically


        ##### Action Open
        openFile = QtGui.QAction(None)
        self.actionOpen.setShortcut('Ctrl+O')
        self.actionOpen.setStatusTip('Open application')
        self.actionOpen.triggered.connect(self.file_open)

        #Button Circle Draw
        self.Circle.clicked.connect(self.circleDraw)

        #action About
        self.actionAbout_GUI.triggered.connect(self.about)

        # Add exit button
        exitButton = QtGui.QAction(None)
        self.actionQuit.setShortcut('Ctrl+Q')
        self.actionQuit.setStatusTip('Exit application')
        self.actionQuit.triggered.connect(QtGui.qApp.quit)

        #Add save button
        saveButton = QtGui.QAction(None)
        self.actionSave.setShortcut('Ctrl+S')
        self.actionSave.setStatusTip("Save Application")
        self.actionSave.triggered.connect(self.file_save)

    def circleDraw(self):
        print("Circle drawed!")
        gcode = [
            ';TYPE:SKIN',
            'G1 F1200 X-9.914 Y-9.843 E3.36222',
            'G0 F9000 X-9.843 Y-9.914',
            'G1 F1200 X9.914 Y9.843 E3.65844',
            'G0 F9000 X9.914 Y9.702',
            'G1 F1200 X-9.702 Y-9.914 E3.95254',
            'G0 F9000 X-9.560 Y-9.914',
            'G1 F1200 X9.914 Y9.560 E4.24451',
            'G0 F9000 X9.914 Y9.419',
            'G1 F1200 X-9.419 Y-9.914 E4.53437',
            'G0 F9000 X-9.277 Y-9.914',
            'G1 F1200 X9.914 Y9.277 E4.82211',
            'G0 F9000 X9.914 Y9.136',
            'G1 F1200 X-9.136 Y-9.914 E5.10772',
            'G0 F9000 X-8.995 Y-9.914',
            'G1 F1200 X9.914 Y8.995 E5.39123',
            'G0 F9000 X9.914 Y8.853',
            'G1 F1200 X-8.853 Y-9.914 E5.67260'
            ]

        for line in gcode:
            coord = re.findall(r'[XY]-\d.\d\d\d', line)
            if coord:
                print("{} - {}".format(coord[0], coord[1]))


    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File','/home/paul/EZB/Project/GUI')
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def file_open(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                '/home/paul/EZB/Project/GUI')

        f = open('circle.gcode', 'r')
        for line in f:
            coord = re.findall(r'[XY]-\d.\d\d\d', line)
            if coord:
                print("{} - {}".format(coord[0], coord[1]))

    def about(self):
        QtGui.QMessageBox.about(None,"About","George-Paul GUI-Interface 2018")



def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
