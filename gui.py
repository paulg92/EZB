from PyQt4 import QtGui, QtCore, Qt # Import the PyQt4 module we'll need
import sys, math # We need sys so that we can pass argv to QApplication
import design  # This file holds our MainWindow and all design related things
from PyQt4.QtGui import QPainter, QImage, QImageWriter, QPen, qRgb
# it also keeps events etc that we defined in Qt Designer
import os,re  # For listing directory methods
import graphicsview
from PyQt4.QtSvg import QSvgGenerator
from buttons import GraphicsView
from PyQt4.QtCore import QSize,QRect


class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow, QtGui.QGraphicsView):
    def __init__(self, parent = None):
        super(self.__class__, self).__init__()
        QtGui.QMainWindow.__init__(self, parent = parent)
        self.setupUi(self)  # This is defined in design.py file automatically

        self.myPenWidth = 1
        self.myPenColor = QtCore.Qt.blue
        imageSize = QtCore.QSize(500, 500)
        self.image = QtGui.QImage(imageSize, QtGui.QImage.Format_RGB32)
        self.pen = QtGui.QPen(QtCore.Qt.black, 3, QtCore.Qt.SolidLine)
        self.lastPoint = QtCore.QPoint()

        self.graphicsView = GraphicsView(self)
        self.graphicsView.clearImage()
        self.setCentralWidget(self.graphicsView)

        self.resize(600, 600)
        self.hasChanged = False

        circleDraw = QtGui.QAction(None)
        self.actionCircle.setShortcut('Ctrl+M')
        self.actionCircle.triggered.connect(self.circleDraw)

        #Pen Color
        penColor = QtGui.QAction(None)
        self.PenColor.setShortcut('Ctrl+C')
        self.PenColor.triggered.connect(self.penColor)

        #Pen Width
        penWidth = QtGui.QAction(None)
        self.PenWidth.setShortcut('Ctrl+W')
        self.PenWidth.triggered.connect(self.penWidth)

        #Clear Image
        clearImage = QtGui.QAction(None)
        self.Clear_Screen.setShortcut('Ctrl+L')
        self.Clear_Screen.triggered.connect(self.graphicsView.clearImage)

        #action About
        self.actionAbout_GUI.triggered.connect(self.about)

        # Add Exit button
        exitButton = QtGui.QAction(None)
        self.actionQuit.setShortcut('Ctrl+Q')
        self.actionQuit.setStatusTip('Exit application')
        self.actionQuit.triggered.connect(QtGui.qApp.quit)

        #Add Save button
        saveButton = QtGui.QAction(None)
        self.actionSave.setShortcut('Ctrl+S')
        self.actionSave.triggered.connect(self.file_save)

        #Add Open button
        openButton = QtGui.QAction(None)
        self.actionOpen.setShortcut("Ctrl+O")
        self.actionOpen.triggered.connect(self.file_open)


    def saveImage(self, fileName):
        visibleImage = self.image
        self.resizeImage(visibleImage, self.size())

        if visibleImage.save(fileName):
            self.modified = False
            return True
        else:
            return False


    def save(self):
        action = self.sender()
        self.file_save()

    def circleDraw(self, event):
        super(ExampleApp, self).circleDraw(event)
        self.setGeometry(200,200, 500,500)
        self.show()
        painter = QtGui.QPainter()
        painter.begin(self.ExampleApp())
        painter.setPen(QColor(Qt.red))
        painter.setFont(QFont('Arial', 20))
        painter.drawText(10,50, "hello Python")


    def penColor(self):
        newColor = QtGui.QColorDialog.getColor(self.graphicsView.penColor())
        if newColor.isValid():
            self.graphicsView.setPenColor(newColor)

    def penWidth(self):
        newWidth, ok = QtGui.QInputDialog.getInteger(self, "Write",
            "Select pen width:", self.graphicsView.penWidth(), 1, 50, 1)
        if ok:
            self.graphicsView.setPenWidth(newWidth)

    def clearImage(self):
        self.image.fill(QtGui.qRgb(255, 255, 255))
        self.modified = True
        self.update()


    def file_save(self):
        initialPath = QtCore.QDir.currentPath()

        fileName = QtGui.QFileDialog.getSaveFileName(self, "Save As",
            initialPath,
            "png(*);")
        if fileName:
            return self.graphicsView.saveImage(fileName, 'png')

        return False


    def file_open(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                '/home/paul/EZB/Project/GUI')

        txt_files = [f for f in os.listdir('.') if f.endswith('.gcode')]
        if len(txt_files) < 1:
            raise ValueError('There is no file with gcode extensions!')
        filename = txt_files[0]
        with open('eample.gcode') as gcode:
            for line in gcode:
                line = line.strip()
                coord = re.findall(r'[XY].?\d+.\d+', line)
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
