from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Settings_Premium import Premium
import sys
class premium_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Premium()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.Tool)

        # self.center()
        # buttons
        self.ui.back.clicked.connect(self.closing)
        self.ui.general.clicked.connect(self.send_to_general)
        self.ui.credits.clicked.connect(self.send_to_file_location)
        self.ui.personal_info.clicked.connect(self.send_to_personal_info)
        self.ui.Ai_info.clicked.connect(self.send_to_ai_info)
    # functions
    def closing(self):
        self.close()
    def send_to_general(self):
        from settings_general_implementation import general_window
        self.settings_1=general_window()
        self.settings_1.show()
        self.close()
    def send_to_file_location(self):
        from file_location_implementation import file_location_window
        self.settings_5=file_location_window()
        self.settings_5.show()
        self.close()
    def send_to_personal_info(self):
        from Settings_Personal_info_implementation import personal_info
        self.settings_2=personal_info()
        self.settings_2.show()
        self.close()
    def send_to_ai_info(self):
        from Settings_AI_info_implementation import ai_info
        self.settings_3=ai_info()
        self.settings_3.show()
        self.close()
    # centerting the window
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
if __name__=="__main__":
        app=QApplication(sys.argv)
        settings_4=premium_window()
        settings_4.show()
        exit(app.exec_())