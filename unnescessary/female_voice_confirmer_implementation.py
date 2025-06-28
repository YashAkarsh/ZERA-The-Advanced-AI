from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
from female_voice_confirmer import Ui_MainWindow


class voice_confirmer_1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.Tool)
        # main function
        self.ui.pushButton.clicked.connect(self.ok_pressed)
        self.ui.pushButton_3.clicked.connect(self.closing)
        if self.ui.pushButton.text()=='Done':
            self.ui.pushbutton.clicked.connect(self.done_pressed)
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #Get the position of the mouse relative to the window
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  #Change mouse icon
        
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

    def center(self):
            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
    def ok_pressed(self):
        import os

        try:
            os.startfile('C:\\ProgramData\\ZeraAI\\voices\\zera voice.reg')
            print('successful')
        except Exception as e:
            print(e)
            print('unable to install zera voice')
        from male_voice_confirmer_implementation import voice_confirmer_2
        self.confirmer_2=voice_confirmer_2()
        self.confirmer_2.show()
        self.close()

            
    def closing(self):
        from male_voice_confirmer_implementation import voice_confirmer_2
        self.confirmer_2=voice_confirmer_2()
        self.confirmer_2.show()
        self.close()
    
if __name__=='__main__':
    app=QApplication(sys.argv)
    confirmer_1=voice_confirmer_1()
    confirmer_1.show()
    confirmer_1.setAttribute(QtCore.Qt.WA_QuitOnClose)
    exit(app.exec_())
