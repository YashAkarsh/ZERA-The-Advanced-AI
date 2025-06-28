from time import sleep
from Settings_AI_info import Ui_ai_info
from Settings_general import General
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import webbrowser
import keyboard,os
from file_location_implementation import file_location_window
from Settings_premium_implementation import premium_window

line_edit_focus=False
class general_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=General()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint)
        self.center()
        
        self.setWindowFlag(QtCore.Qt.Tool)

        # making settings class
        self.storage_folder=QSettings("Yash Akarsh","ZERA-The Advanced AI")
        self.settings=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Settings")
        # buttons
        self.ui.back.clicked.connect(self.closing)
        self.ui.pushButton_7.clicked.connect(self.reset_info)
        self.ui.pushButton_6.clicked.connect(self.send_to_file_location)
        self.ui.pushButton_5.clicked.connect(self.send_to_premium)
        self.ui.pushButton_2.clicked.connect(self.send_to_personal_info)
        self.ui.pushButton_3.clicked.connect(self.send_to_ai_info)
        # self.ui.lineEdit_3.setReadOnly(True)

        # main functions
        # with open('C:\\ProgramData\\ZeraAI\\hotkeys.txt') as f:
        #     wake_detector=f.readline().strip()
        #     sleep_detector=f.readline()
        try:
            wake_detector=self.settings.value("waking_hotkey")
        except:
            wake_detector='Tab'
        try:
            sleep_detector=self.settings.value("sleeping_hotkey")
        except:
            sleep_detector='Home'

        self.ui.lineEdit_2.setText(str(sleep_detector).capitalize())
        self.ui.lineEdit_3.setText(str(wake_detector).capitalize())
        
        # with open('C:\\ProgramData\\ZeraAI\\Settings.txt') as f:
        #     a=f.readline().strip()
        #     b=f.readline().strip()
        #     c=f.readline().strip()

        a=self.settings.value("wake_greeting")
        b=self.settings.value("goodbye_greeting")
        c=self.settings.value("exit_dialog_box")
        if a=="true":
            a=True
        elif a=="false":
            a=False
        if b=="true":
            b=True
        elif b=="false":
            b=False
        if c=="true":
            c=True
        elif c=="false":
            c=False


        if a==True and b==False or a=='True ~~' and b==False:
            self.ui.checkBox.setChecked(True)
            self.ui.checkBox_2.setChecked(False)
        elif a==False and b==True:
            self.ui.checkBox_2.setChecked(True)
            self.ui.checkBox.setChecked(False)
        elif a==True and b==True:
            self.ui.checkBox.setChecked(True)
            self.ui.checkBox_2.setChecked(True)
        elif a=='none' and len(b)==0:
            self.ui.checkBox.setChecked(False)
            self.ui.checkBox_2.setChecked(False)
        if c==False:
            self.ui.checkBox_3.setChecked(False)
        elif c==True and a==False and b==False:
            self.ui.checkBox_3.setChecked(True)
            self.ui.checkBox.setChecked(False)
            self.ui.checkBox_2.setChecked(False)
        elif c==True and a==False and b==True:
            self.ui.checkBox_3.setChecked(True)
            self.ui.checkBox_2.setChecked(True)
            self.ui.checkBox.setChecked(False)
        elif c==True and a==False and b==True:
            self.ui.checkBox_3.setChecked(True)
            self.ui.checkBox_2.setChecked(False)
            self.ui.checkBox.setChecked(True)
        elif c==True and a==True and b==True:
            self.ui.checkBox_3.setChecked(True)
            self.ui.checkBox_2.setChecked(True)
            self.ui.checkBox.setChecked(True)
        elif c==True and a=="True ~~" and b==True:
            self.ui.checkBox_3.setChecked(True)
        elif c==True and a=="True ~~" and b==False:
            self.ui.checkBox_3.setChecked(True)

        if a==False and b==False and c==False:
            self.ui.checkBox.setChecked(False)
            self.ui.checkBox_2.setChecked(False)
            self.ui.checkBox_3.setChecked(False)
    # centering the window
    def center(self):
            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
    def reset_info(self):
        try:
            # with open('C:\\ProgramData\\ZeraAI\\Tutorial_link.txt','r') as f:
            #     link=f.read()
            #     webbrowser.open(link)
            # with open('C:\\ProgramData\\ZeraAI\\condition.txt','w') as f:
            #             f.write('reset')
            other_reset=QSettings("Yash Akarsh\\ZERA-The Advanced AI",'Other')
            other_reset.setValue("condition","reset")
            self.close()
         
        except Exception as e:
            print(e)
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
    def send_to_file_location(self):
        self.settings_5=file_location_window()
        self.settings_5.show()
        self.closing()
    def send_to_premium(self):
        self.settings_4=premium_window()
        self.settings_4.show()
        self.closing()
    def send_to_personal_info(self):
        from Settings_Personal_info_implementation import personal_info
        self.settings_2=personal_info()
        self.settings_2.show()
        self.closing()
    def send_to_ai_info(self):
        from Settings_AI_info_implementation import ai_info
        self.settings_3=ai_info()
        self.settings_3.show()
        self.closing()
    def closing(self):
        sleeping_hotword=self.ui.lineEdit_2.text()
        waking_hotword=self.ui.lineEdit_3.text()
        wake_greeting=self.ui.checkBox.isChecked()
        goodbye_greeting=self.ui.checkBox_2.isChecked()
        exit_dialog_box=self.ui.checkBox_3.isChecked()
        
        # try:
        #     os.remove('C:\\ProgramData\\ZeraAI\\hotkeys.txt')
        # except Exception:
        #     pass
        # with open('C:\\ProgramData\\ZeraAI\\hotkeys.txt','w') as f:
        #     f.write(f'{waking_hotword}\n{sleeping_hotword}')

        self.settings.setValue("waking_hotkey",waking_hotword)
        self.settings.setValue('sleeping_hotkey',sleeping_hotword)

        if wake_greeting:
            wake_greeting=True
        else:
            wake_greeting=False
        if goodbye_greeting:
            goodbye_greeting=True
        else:
            goodbye_greeting=False
        if exit_dialog_box:
            exit_dialog_box=True
        else:
            exit_dialog_box=False
        
        # with open('C:\\ProgramData\\ZeraAI\\Settings.txt','w') as f:
        #     f.write(f"{wake_greeting}\n{goodbye_greeting}\n{exit_dialog_box}")

        self.settings.setValue("wake_greeting",wake_greeting)
        self.settings.setValue("goodbye_greeting",goodbye_greeting)
        self.settings.setValue("exit_dialog_box",exit_dialog_box)
        general_window.close(self)
        # print(True)
if __name__=="__main__":
        app=QApplication(sys.argv)
        settings_1=general_window()
        settings_1.show()
        exit(app.exec_())