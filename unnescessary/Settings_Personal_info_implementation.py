from Settings_Personal_info import Ui_PersonalInfo
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys

class personal_info(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_PersonalInfo()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.Tool)
        

        self.user_info=QSettings("Yash Akarsh\\ZERA-The Advanced AI","user_info")
        # setting items
        # with open('C:\\ProgramData\\ZeraAI\\info.txt','r') as f:
        user_name=self.user_info.value("name")
        user_dob=self.user_info.value("birth_date")
        user_age=self.user_info.value("user_age")
        user_gender=self.user_info.value("gender")
        user_email=self.user_info.value("email")

        self.ui.name_area.setText(user_name)
        self.ui.name_area_2.setText(user_dob)
        self.ui.name_area_3.setText(user_email)

        # buttons
        self.ui.back.clicked.connect(self.closing)
        self.ui.general.clicked.connect(self.send_to_general)
        self.ui.Premium.clicked.connect(self.send_to_premium)
        self.ui.credits.clicked.connect(self.send_to_file_location)
        self.ui.Ai_info.clicked.connect(self.send_to_ai_info)

    def closing(self):
        get_name=self.ui.name_area.text().split()
        get_dob=self.ui.name_area_2.text().strip()
        get_email=self.ui.name_area_3.text().strip()

        # with open('C:\\ProgramData\\ZeraAI\\info.txt','r') as f:
        user_name=self.user_info.value("name")
        user_dob=self.user_info.value("birth_date")
        user_age=self.user_info.value("user_age")
        user_gender=self.user_info.value("gender")
        user_email=self.user_info.value("email")

        get_name=" ".join(get_name)
        # with open('C:\\ProgramData\\ZeraAI\\info.txt','w') as f:
        #     f.write(f"{get_name}\n{get_dob}\n{user_age}\n{user_gender}\n{get_email}")
        self.user_info.setValue("name",get_name)
        self.user_info.setValue("date_birth",get_dob)
        self.user_info.setValue("email",get_email)
        self.close()

    def send_to_premium(self):
        from Settings_premium_implementation import premium_window
        self.settings_4=premium_window()
        self.settings_4.show()
        self.closing()
    def send_to_file_location(self):
        from file_location_implementation import file_location_window
        self.settings_5=file_location_window()
        self.settings_5.show()
        self.closing()
    def send_to_general(self):
        from settings_general_implementation import general_window
        self.settings_1=general_window()
        self.settings_1.show()
        self.closing()
    def send_to_ai_info(self):
        from Settings_AI_info_implementation import ai_info
        self.settings_3=ai_info()
        self.settings_3.show()
        self.closing()
        # moving window
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
    settings_2=personal_info()
    settings_2.show()
    exit(app.exec_())

