from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from setup import Ui_MainWindow
import os
from voice_installer import install_voices

class setup_window(QMainWindow):        
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint)
        self.center()
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()
        self.setWindowFlags(self.windowFlags()|Qt.Tool)
        self.setWindowFlag(QtCore.Qt.Tool)

        # buttons
        self.ui.finish.clicked.connect(self.done)
        self.ui.email.returnPressed.connect(self.done)
        
        self.user_info=QSettings("Yash Akarsh\\ZERA-The Advanced AI",'user_info')
        self.settings=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Settings")
        self.ai_settings=QSettings("Yash Akarsh\\ZERA-The Advanced AI","AI_Settings")
        self.other=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Other")
    def done(self):
        # from female_voice_confirmer_implementation import voice_confirmer_1
        from settingupzera_implementation import settingupzera
        user_name=self.ui.username.text()
        # user_birth=self.ui.dob.text()
        get_dob=self.ui.dob.date()
        user_age=self.ui.AgeSelection.text()
        user_gender=''
        user_email=self.ui.email.text()
        user_birth=f"{get_dob.year()},{get_dob.month()},{get_dob.day()}"

        if self.ui.male.isChecked():
                user_gender='sir'
        elif self.ui.female.isChecked():
                user_gender='mam'
        
        # checking if blank
        
        import os
        if os.path.exists('C:\\ProgramData\\ZeraAI'):
                try:
                        import shutil
                        shutil.rmtree('C:\\ProgramData\\ZeraAI')
                        os.mkdir('C:\\ProgramData\\ZeraAI')
                except:
                        pass
        else:
                os.mkdir('C:\\ProgramData\\ZeraAI')
        if len(user_name)!=0 and len(user_gender)!=0 and not len(user_name.strip())>11:
                # with open('C:\\ProgramData\\ZeraAI\\info.txt','w') as f:
                #         f.write(f"{user_name}\n{user_birth}\n{user_age}\n{user_gender}\n{user_email}")
                self.user_info.setValue("name",user_name)
                self.user_info.setValue("birth_date",user_birth)
                self.user_info.setValue("user_age",user_age)
                self.user_info.setValue("gender",user_gender)
                self.user_info.setValue("email",user_email)

                # with open("C:\\ProgramData\\ZeraAI\\hotkeys.txt",'w') as f:
                #         f.write('tab\nhome')
                self.settings.setValue("waking_hotkey","Tab")
                self.settings.setValue("sleeping_hotkey","Home")
   
                # with open("C:\\ProgramData\\ZeraAI\\AI_Settings.txt",'w') as f:
                #         f.write('Zera')
                self.ai_settings.setValue("ai_name","Zera")
                self.ai_settings.setValue("ai_voice","")

                # with open('C:\\ProgramData\\ZeraAI\\Tutorial_link.txt','w') as f:
                #         f.write('https://www.youtube.com/channel/UCSIbbWhj3a6E7E0wu6EuK1Q/videos')
                self.other.setValue("tutorial_link","https://www.youtube.com/channel/UCSIbbWhj3a6E7E0wu6EuK1Q/videos")

                # with open('C:\\ProgramData\\ZeraAI\\condition.txt','w') as f:
                #         f.write('')
                self.other.setValue("condition","")

                # with open("C:\\ProgramData\\ZeraAI\\user_occurence.txt","w") as f:
                #         f.write('new')
                self.other.setValue("user_occurence","new_2")
                try:
                #         os.mkdir('C:\\ProgramData\\ZeraAI\\Programs')
                        self.programs=QSettings("Yash Akarsh\\ZERA-The Advanced AI",'Programs')
                        self.programs.setValue("program_names",'')
                except:
                        pass
                try:
                        os.mkdir('C:\\ProgramData\\ZeraAI\\voices')
                except:
                        pass
                install_voices()
                self.settingupzera_win=settingupzera()
                self.settingupzera_win.show()
                self.close()
        if len(user_name.strip())==0:
                self.ui.username.setPlaceholderText('Username-(required)')
        elif len(user_name.strip())>11:
                self.ui.username.setText('')
                self.ui.username.setPlaceholderText('max 11 letters only')
        if len(user_gender.strip())==0:
                        self.ui.male.setStyleSheet("font: 17pt \"orbitron\";\n"
"\ncolor:red;")
                        self.ui.female.setStyleSheet("font: 17pt \"orbitron\";\n"
"\ncolor:red;")
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #Get the position of the mouse relative to the window
            event.accept()
        #     self.setCursor(QCursor(Qt.OpenHandCursor))  #Change mouse icon
    
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

if __name__ == "__main__":
        import sys
        # if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        #         QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_DisableHighDpiScaling, True)
        # if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        #         QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
        # QApplication.setAttribute(Qt.AA_DisableHighDpiScaling)
        QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        app=QApplication(sys.argv)
        setup_win=setup_window()
        
        setup_win.show()
        exit(app.exec_())        