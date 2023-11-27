from JarvisUI import Ui_Form
from PyQt5 import QtCore , QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import Jarvis
import sys


class MainThread(QThread):

    def __init__(self):
        super(MainThread, self).__init__()



    def run(self):
        Jarvis.Task_Gui()

startExe = MainThread()    

class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.gui = Ui_Form()
        self.gui.setupUi(self)

        self.gui.start.clicked.connect(self.startTask)
        self.gui.end.clicked.connect(self.close)

    def startTask(self):

        # self.gui.label1 = QtGui.QMovie("images//gifloader.gif")
        self.gui.label1 = QtGui.QMovie("images//gifloader.gif")
        self.gui.Gif.setMovie(self.gui.label1)
        self.gui.label1.start()

GuiApp = QApplication(sys.argv)
Jarvis_GUI = Gui_Start()
Jarvis_GUI.show()
exit(GuiApp.exec_())
