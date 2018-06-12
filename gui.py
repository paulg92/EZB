from PyQt4 import QtGui, QtCore  # Import the PyQt4 module we'll need
import sys, math # We need sys so that we can pass argv to QApplication
import design  # This file holds our MainWindow and all design related things
from PyQt4.QtGui import QPainter
# it also keeps events etc that we defined in Qt Designer
import os,re  # For listing directory methods
import graphicsview


class GraphicsView(QtGui.QWidget):
    """
      this scales the image but it's not good, too many refreshes really mess it up!!!
    """
    def __init__(self, parent=None):
        super(GraphicsView, self).__init__(parent)

        self.setAttribute(QtCore.Qt.WA_StaticContents)
        self.modified = False
        self.scribbling = False
        self.myPenWidth = 1
        self.myPenColor = QtCore.Qt.blue
        imageSize = QtCore.QSize(500, 500)
        self.image = QtGui.QImage(imageSize, QtGui.QImage.Format_RGB32)
        self.lastPoint = QtCore.QPoint()

    def openImage(self, fileName):
        loadedImage = QtGui.QImage()
        if not loadedImage.load(fileName):
            return False

        w = loadedImage.width()
        h = loadedImage.height()
        self.mainWindow.resize(w, h)

#       newSize = loadedImage.size().expandedTo(self.size())
#       self.resizeImage(loadedImage, newSize)
        self.image = loadedImage
        self.modified = False
        self.update()
        return True

    def saveImage(self, fileName, fileFormat):
        visibleImage = self.image
        self.resizeImage(visibleImage, self.size())

        if visibleImage.save(fileName, fileFormat):
            self.modified = False
            return True
        else:
            return False

    def setPenColor(self, newColor):
        self.myPenColor = newColor

    def setPenWidth(self, newWidth):
        self.myPenWidth = newWidth

    def clearImage(self):
        self.image.fill(QtGui.qRgb(255, 255, 255))
        self.modified = True
        self.update()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.lastPoint = event.pos()
            self.scribbling = True

    def mouseMoveEvent(self, event):
        if (event.buttons() & QtCore.Qt.LeftButton) and self.scribbling:
            self.drawLineTo(event.pos())

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.scribbling:
            self.drawLineTo(event.pos())
            self.scribbling = False

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawImage(event.rect(), self.image)

    def resizeEvent(self, event):

        self.resizeImage(self.image, event.size())

        super(GraphicsView, self).resizeEvent(event)

    def drawLineTo(self, endPoint):
        painter = QtGui.QPainter(self.image)
        painter.setPen(QtGui.QPen(self.myPenColor, self.myPenWidth,
            QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        painter.drawLine(self.lastPoint, endPoint)
        self.modified = True

        self.update()
        self.lastPoint = QtCore.QPoint(endPoint)

    def resizeImage(self, image, newSize):
        if image.size() == newSize:
            return

# this resizes the canvas without resampling the image
        newImage = QtGui.QImage(newSize, QtGui.QImage.Format_RGB32)
        newImage.fill(QtGui.qRgb(255, 255, 255))
        painter = QtGui.QPainter(newImage)
        painter.drawImage(QtCore.QPoint(0, 0), image)


        self.image = newImage

    def print_(self):
        printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)

        printDialog = QtGui.QPrintDialog(printer, self)
        if printDialog.exec_() == QtGui.QDialog.Accepted:
            painter = QtGui.QPainter(printer)
            rect = painter.viewport()
            size = self.image.size()
            size.scale(rect.size(), QtCore.Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image.rect())
            painter.drawImage(0, 0, self.image)
            painter.end()

    def isModified(self):
        return self.modified

    def penColor(self):
        return self.myPenColor

    def penWidth(self):
        return self.myPenWidth


class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow, QtGui.QGraphicsView):
    def __init__(self, parent = None):
        super(self.__class__, self).__init__()
        QtGui.QMainWindow.__init__(self, parent = parent)
        self.setupUi(self)  # This is defined in design.py file automatically

        self.graphicsView = GraphicsView(self)
        self.graphicsView.clearImage()
        self.graphicsView.mainWindow = self  # maybe not using this?
        self.setCentralWidget(self.graphicsView)


        ##### Action Open
        openFile = QtGui.QAction(None)
        self.actionOpen.setShortcut('Ctrl+O')
        self.actionOpen.setStatusTip('Open application')
        self.actionOpen.triggered.connect(self.file_open)

        #Button Rectangle Draw
        self.Rectangle.clicked.connect(self.rectangleDraw)
        #Button Triangle Draw
        self.Triangle.clicked.connect(self.triangleDraw)

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

    def rectangleDraw(self):
        gcode = [
            ';TYPE:SKIN',
            'G00 X-0 Y-0 F70',
            'G01 Z-1 F50',
            'G01 X0 Y20 F50',
            'G01 X25 Y20',
            'G01 X25 Y0',
            'G01 X0 Y0',
            'G00 Z0 F70',
            'M30'
            ]

        for line in gcode:
            coord = re.findall(r'[XY]-\d.\d\d\d', line)
            if coord:
                print("{} - {}".format(coord[0], coord[1]))

    def triangleDraw(self):
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

        txt_files = [f for f in os.listdir('.') if f.endswith('.gcode')]
        if len(txt_files) < 1:
            raise ValueError('There is no file with gcode extensions!')

        filename = txt_files[0]
        f = open('eample.gcode', 'r')
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
