from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from exit_confirmer import Ui_MainWindow
import Main_AI
# from Main_AI import Zera
import sys

class exit_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton.clicked.connect(self.close)
        self.ui.pushButton_2.clicked.connect(self.ok_pressed)
        self.setWindowFlag(QtCore.Qt.Tool)
        self.center()
    def center(self):
            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #Get the position of the mouse relative to the window
            event.accept()
            # self.setCursor(QCursor(Qt.OpenHandCursor))  #Change mouse icon
    
    def mouseMoveEvent(self, QMouseEvent):
        try:
            if Qt.LeftButton and self.m_flag:  
                self.move(QMouseEvent.globalPos()-self.m_Position)#Change window position
                QMouseEvent.accept()
        except:
            pass
        
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))
    
    def ok_pressed(self):
        # with open("C:\\ProgramData\\ZeraAI\\condition.txt",'w') as f:
        #     f.write('exit')
        self.other=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Other")
        self.other.setValue("condition",'exit')
        self.close()

if __name__=="__main__":
    app=QApplication(sys.argv)
    exit_window=exit_window()
    exit_window.show()
    exit_window.setAttribute(QtCore.Qt.WA_QuitOnClose)
    sys.exit(app.exec_())

