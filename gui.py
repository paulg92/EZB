from PyQt4 import QtGui, QtCore, Qt # Import the PyQt4 module we'll need
import sys, math # We need sys so that we can pass argv to QApplication
import design  # This file holds our MainWindow and all design related things
from PyQt4.QtGui import QPainter, QImage, QImageWriter, QPen, qRgb
# it also keeps events etc that we defined in Qt Designer
import os,re  # For listing directory methods
import graphicsview

from buttons import GraphicsView


class ExampleApp(QtGui.QMainWindow, design.Ui_MainWindow, QtGui.QGraphicsView):
    def __init__(self, parent = None):
        super(self.__class__, self).__init__()
        QtGui.QMainWindow.__init__(self, parent = parent)
        self.setupUi(self)  # This is defined in design.py file automatically

        self.pen = QtGui.QPen(QtCore.Qt.black, 3, QtCore.Qt.SolidLine)

        self.graphicsView = GraphicsView(self)
        self.graphicsView.clearImage()
        self.setCentralWidget(self.graphicsView)

        self.resize(600, 600)

        ##### Action Open
        openFile = QtGui.QAction(None)
        self.actionOpen.setShortcut('Ctrl+O')
        self.actionOpen.setStatusTip('Open application')
        self.actionOpen.triggered.connect(self.file_open)

        # rectangleDraw = QtGui.QAction(None)
        # self.actionRectangle.setShortcut('Ctrl+R')
        # self.actionRectangle.triggered.connect(self.rectangleDraw)

        circleDraw = QtGui.QAction(None)
        self.actionCircle.setShortcut('Ctrl+C')
        self.actionCircle.triggered.connect(self.circleDraw)

        #Button Triangle Draw
        #self.Triangle.clicked.connect(self.triangleDraw)
        #Line drawing
        self.Line.clicked.connect(self.lineDraw)
        #Polygon drawing
        self.Polygon.clicked.connect(self.polygonDraw)

        #Button Polygon Draw
        #self.Polygon.clicked.connect(self.PolygonDraw)

        #Pen color
        penColor = QtGui.QAction(None)
        self.PenColor.setShortcut('Ctrl+C')
        self.PenColor.triggered.connect(self.penColor)

        #Pen width
        penWidth = QtGui.QAction(None)
        self.PenWidth.setShortcut('Ctrl+W')
        self.PenWidth.triggered.connect(self.penWidth)

        #clear image
        clearImage = QtGui.QAction(None)
        self.Clear_Screen.setShortcut('Ctrl+L')
        self.Clear_Screen.triggered.connect(self.clearImage)

        #action About
        self.actionAbout_GUI.triggered.connect(self.about)

        optionMenu = QtGui.QMenu("&Options", self)
        optionMenu.addAction(self.PenColor)
        optionMenu.addAction(self.PenWidth)
        optionMenu.addSeparator()
        #optionMenu.addAction(self.clearScreenAct)

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



    def polygonDraw(self, endPoint):
        painter = QPainter(self.image)
        painter.setPen(QPen(self.myPenColor, self.myPenWidth, Qt.SolidLine,
                Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(self.lastPoint, endPoint)
        self.modified = True

        rad = self.myPenWidth / 2 + 2
        self.update(QRect(self.lastPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))
        self.lastPoint = QPoint(endPoint)

    def lineDraw(self, end):
        painter = QPainter(self.image)
        painter.setPen(QPen(self.myPenColor, self.myPenWidth, Qt.SolidLine,
                Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(self.lastPoint, endPoint)
        self.modified = True

        rad = self.myPenWidth / 2 + 2
        self.update(QRect(self.lastPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))
        self.lastPoint = QPoint(endPoint)

    # def paintEvent(self, e):
    #
    #      qp = QtGui.QPainter()
    #      qp.begin(self)
    #      self.rectangleDraw(qp)
    #      qp.end()

    #def rectangleDraw(self, qp):

    #def PolygonDraw(self):

    #def circleDraw(self):


    def penColor(self):
        newColor = QtGui.QColorDialog.getColor(self.graphicsView.penColor())
        if newColor.isValid():
            self.graphicsView.setPenColor(newColor)

    def penWidth(self):
        newWidth, ok = QtGui.QInputDialog.getInteger(self, "Scribble",
            "Select pen width:", self.graphicsView.penWidth(), 1, 50, 1)
        if ok:
            self.graphicsView.setPenWidth(newWidth)

    def clearImage(self):
        self.image.fill(QtGui.qRgb(255, 255, 255))
        self.modified = True
        self.update()

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
            QtGui.QMessageBox.about(None,"About","George-Paul GUI-Interface 2018")

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
