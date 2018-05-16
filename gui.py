from PyQt4 import QtGui  # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication

import design  # This file holds our MainWindow and all design related things

# it also keeps events etc that we defined in Qt Designer
import os  # For listing directory methods


class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined
        #self.btnBrowse.clicked.connect(self.browse_folder)  # When the button is pressed
                                                            # Execute browse_folder function
        ##### Action Open
        openFile = QtGui.QAction(None)
        self.actionOpen.setShortcut('Ctrl+O')
        self.actionOpen.setStatusTip('Open application')
        self.actionOpen.triggered.connect(self.file_open)

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

    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()

    def file_open(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                '/home')

        f = open(fname, 'r')

        with f:
            data = f.read()
            self.textEdit.setText(data)

    def about(self):
        QtGui.QMessageBox.about(None,"About","George-Paul GUI-Interface 2018")


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = ExampleApp()  # We set the form to be our ExampleApp (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function
