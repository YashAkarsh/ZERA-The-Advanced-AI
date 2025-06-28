from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
from male_voice_confirmer import Ui_MainWindow

class voice_confirmer_2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.Tool)

        self.ui.pushButton_2.clicked.connect(self.ok_pressed)
        self.ui.pushButton.clicked.connect(self.closing)
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
        try:
            import os
            os.startfile('C:\\ProgramData\\ZeraAI\\voices\\ /s jarvis voice.reg')
        except Exception:
            pass
        from settingupzera_implementation import settingupzera
        self.settingup=settingupzera()
        self.settingup.show()
        self.close()
    def closing(self):
        from settingupzera_implementation import settingupzera
        self.settingup=settingupzera()
        self.settingup.show()
        self.close()
if __name__=="__main__":
    app=QApplication(sys.argv)
    confirmer_2=voice_confirmer_2()
    confirmer_2.show()
    exit(app.exec_())