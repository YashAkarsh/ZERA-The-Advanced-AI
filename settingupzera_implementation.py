from typing import Counter
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
import random,os

class settingupzera(QMainWindow):
    def __init__(self):
        super().__init__()
        self.counter=0
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        other_change=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Other")
        other_change.setValue("user_occurence","new_2")
        self.setWindowFlag(QtCore.Qt.Tool)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()
    
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.initialize)
        self.timer.start(300)

    def initialize(self):
        self.counter+=1
        self.ui.label.setText(str(self.counter)+"%")
        if self.counter==50:
            try:
                os.system('regedit /s C:\\ProgramData\\ZeraAI\\voices\\zera_voice.reg')
            except Exception:
                print('unable to install zera voice')
        elif self.counter==70:
            try:
                os.system("regedit /s C:\\ProgramData\\ZeraAI\\voices\\jarvis_voice.reg")
            except Exception as e:
                print('Unable to install jarvis voice')
        elif self.counter==100:
            import Main_AI

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
            self.Zera=Main_AI.Main()
            self.Zera.show()
            Main_AI.speak('')
            try:
                d=self.other_data.value("user_occurence").strip()
            except:
                pass
            if d=='new_2':
                    self.Zera.run_task()
            # self.timer.stop()
            self.hide()
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
if __name__=='__main__':
    QApplication.setAttribute(Qt.AA_DisableHighDpiScaling)
    app=QApplication(sys.argv)
    settingupzera_win=settingupzera()
    settingupzera_win.show()
    settingupzera_win.setAttribute(QtCore.Qt.WA_QuitOnClose)
    tray=QSystemTrayIcon(parent=app)
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/icon/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    tray.setIcon(icon)
    # tray.setVisible(True)
    tray.setToolTip("ZERA-The Advanced AI")
    tray.show()

    menu=QMenu()
    option1=menu.addAction('EXIT')
    option1.triggered.connect(app.quit)
    menu.addAction(option1)

    tray.setContextMenu(menu)
    sys.exit(app.exec_())