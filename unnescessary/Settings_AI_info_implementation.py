from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
from Settings_AI_info import Ui_ai_info
from settings_general_implementation import general_window
import pyttsx3

engine=pyttsx3.init()
class ai_info(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_ai_info()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.Tool)

        # buttons
        self.ui.pushButton_4.clicked.connect(self.closing)
        self.ui.pushButton.clicked.connect(self.send_to_general)
        self.ui.pushButton_6.clicked.connect(self.send_to_file_location)
        self.ui.pushButton_5.clicked.connect(self.send_to_premium)
        self.ui.pushButton_2.clicked.connect(self.send_to_personal_info)
        self.center()

        self.ai_info=QSettings("Yash Akarsh\\ZERA-The Advanced AI","AI_Settings")

        # extras
        # with open("C:\\ProgramData\\ZeraAI\\AI_settings.txt",'r') as f:
        name=self.ai_info.value("ai_name")
        voice_idx=self.ai_info.value("ai_voice")

        
        self.ui.label.setText(name.strip())
        if name.strip()=='Jarvis':
            self.ui.radioButton_3.setChecked(True)
    
        # voice management
        voices=engine.getProperty('voices')
        v_names=[]
        for i in range(len(voices)):
                # pass
            a=(str(voices[i]).split())
            if 'name=Cortana' in a[2]:
                a[2]=str(a[2]).replace("name=Cortana","Cortana")
                v_names.append(a[2])
            else:
                v_names.append(a[3])

        print(v_names)
        self.ui.comboBox.addItems(v_names)
        # for i in range(len(voices)):
        #     self.ui.comboBox.addItem(" ")
        #     id=str(voices[i]).split()
        #     print(id[1])
        #     if 'name=Cortana' in id[2]:
        #         id2=str(id[2]).replace('name=','')
        #         self.ui.comboBox.setItemText(i,id2)
        #     else:
        #         self.ui.comboBox.setItemText(i,id[3])
        
        try:
            self.ui.comboBox.setCurrentIndex(int(voice_idx))
        except Exception as e:
            print(e)
            if name.lower()=="zera":
                id=v_names.index("Cortana")
                try:
                    self.ui.comboBox.setCurrentIndex(id)
                except:
                    self.ui.comboBox.setCurrentIndex(0)
            else:
                id=v_names.index("Mark")
                try:
                    self.ui.comboBox.setCurrentIndex(id)
                except:
                    self.ui.comboBox.setCurrentIndex(0)

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
    def send_to_personal_info(self):
        from Settings_Personal_info_implementation import personal_info
        self.settings_3=personal_info()
        self.settings_3.show()
        self.closing()
    def closing(self):
        Which_AI=''
        Voice=self.ui.comboBox.currentIndex()
        if self.ui.radioButton_4.isChecked():
            Which_AI='Zera' 
        elif self.ui.radioButton_3.isChecked():
            Which_AI='Jarvis'
        # with open("C:\\PRogramData\\ZeraAI\\AI_Settings.txt",'w') as f:
        #     f.write(f"{Which_AI}\n{Voice}")
        self.ai_info.setValue("ai_name",Which_AI)
        self.ai_info.setValue("ai_voice",str(Voice))
        self.close()
              
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

    
if __name__=='__main__':
    app=QApplication(sys.argv)
    settings_3=ai_info()
    settings_3.show()
    exit(app.exec_())