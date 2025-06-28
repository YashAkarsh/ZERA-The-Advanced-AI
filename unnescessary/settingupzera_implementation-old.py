from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
from settingupzera import Ui_MainWindow
import random

# with open('C:\\ProgramData\\ZeraAI\\user_occurence.txt','w') as f:
#     f.write('new_2')

class settingupzera(QMainWindow):
    def __init__(self):
        global other
        self.counter=0
        other_change=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Other")
        other_change.setValue("user_occurence","new_2")
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint)
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap(":/bgImage/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ui.centralwidget.setWindowIcon(self.icon)
        self.setWindowFlag(QtCore.Qt.Tool)

        # main functions
        self.timer= QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)
        self.center()
    # centering the window
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

    def progress(self):
        from female_voice_confirmer_implementation import voice_confirmer_1
        # global counter
        increment=random.randint(int(0.5),1)
        import keyboard
        if keyboard.is_pressed('esc'):
            self.close()
        else:
            pass
        self.counter+=increment
        self.ui.LoadingBAr.setValue(self.counter)
        if self.counter == 100:
            import os
            import Main_AI
            from Main_AI import Main

            settings_0=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Settings")
            check_value=settings_0.value("sleeping_hotkey")
            if check_value==None:
                    print("recreating")
                    settings_0.setValue("exit_dialog_box",False)
                    # settings_0.setValue("wake_greeting",True)
                    settings_0.setValue("goodbye_greeting",True)
                    settings_0.setValue("waking_hotkey","tab")
                    settings_0.setValue("sleeping_hotkey","home")
            self.other_data=QSettings('Yash Akarsh\\ZERA-The Advanced AI',"Other")
            # other.setValue("condition",'')
            self.Zera=Main()
            self.Zera.show()
            Main_AI.speak('')
            d=self.other_data.value("user_occurence").strip()
            if d=='new_2':
                    self.Zera.run_task()
            self.timer.stop()
            self.close()
if __name__=="__main__":
    app=QApplication(sys.argv)
    settingup=settingupzera()
    settingup.show()
    sys.exit(app.exec_())

