from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from custom_commands import Ui_MainWindow
import json
import sys

class custom_commands_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.center()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlag(QtCore.Qt.Tool)

        self.settings=QSettings("Yash Akarsh\\ZERA-The Advanced AI",'Settings')

        # setting line edits
        self.l1=[self.ui.q1,self.ui.q2,self.ui.q3,self.ui.q4,self.ui.q5,self.ui.q6,self.ui.q7,self.ui.q8]
        self.l2=[self.ui.r1,self.ui.r2,self.ui.r3,self.ui.r4,self.ui.r5,self.ui.r6,self.ui.r7,self.ui.r8]

        custom_commands=self.settings.value('custom_commands')
        # custom_commands=json.loads('custom_commands')
        command_dict=custom_commands
        try:
            reply_list=list(command_dict.values())
            query_list=list(command_dict.keys())
            for i in range(0,len(self.l1)):
                try:
                    self.l1[i].setText(query_list[i])
                    self.l2[i].setText(reply_list[i])
                except:
                    break
        except:
            pass
        self.ui.q1.returnPressed.connect(lambda:self.focus_shifter('q1'))
        self.ui.q2.returnPressed.connect(lambda:self.focus_shifter('q2'))
        self.ui.q3.returnPressed.connect(lambda:self.focus_shifter('q3'))
        self.ui.q4.returnPressed.connect(lambda:self.focus_shifter('q4'))
        self.ui.q5.returnPressed.connect(lambda:self.focus_shifter('q5'))
        self.ui.q6.returnPressed.connect(lambda:self.focus_shifter('q6'))
        self.ui.q7.returnPressed.connect(lambda:self.focus_shifter('q7'))
        self.ui.q8.returnPressed.connect(lambda:self.focus_shifter('q8'))

        self.ui.r1.returnPressed.connect(lambda:self.focus_shifter_replies('r1'))
        self.ui.r2.returnPressed.connect(lambda:self.focus_shifter_replies('r2'))
        self.ui.r3.returnPressed.connect(lambda:self.focus_shifter_replies('r3'))
        self.ui.r4.returnPressed.connect(lambda:self.focus_shifter_replies('r4'))
        self.ui.r5.returnPressed.connect(lambda:self.focus_shifter_replies('r5'))
        self.ui.r6.returnPressed.connect(lambda:self.focus_shifter_replies('r6'))
        self.ui.r7.returnPressed.connect(lambda:self.focus_shifter_replies('r7'))
        self.ui.r8.returnPressed.connect(lambda:self.focus_shifter_replies('r8'))
        
        

        # joining buttons
        self.ui.back.clicked.connect(self.closing)

    def focus_shifter(self,element):
        # if element=='q1':
        #     self.ui.q2.setFocus()
        # if element=='q1':
        #     self.ui.q2.setFocus()
        for i in range(9):
            if element==f'q{i}':
                if i<8:
                    self.l1[i].setFocus()
                else:
                    i=0
                    self.l1[i].setFocus()
    
    def focus_shifter_replies(self,element):
        for i in range(9):
            if element==f'r{i}':
                if i<8:
                    self.l2[i].setFocus()
                else:
                    i=0
                    self.l2[i].setFocus()

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
    
    def center(self):
            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
    
    def closing(self):
        commands_dict={}
        for i in range(0,len(self.l1)):
            if len(self.l1[i].text())!=0:
                commands_dict.update({(self.l1[i].text()).lower():(self.l2[i].text()).lower()})
            else:
                continue
        self.settings.setValue('custom_commands',commands_dict)
        print(commands_dict)

        self.close()


if __name__=='__main__':
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
                QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
            QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    QApplication.setAttribute(Qt.AA_DisableHighDpiScaling)
    
    app=QApplication(sys.argv)
    custom_commands_win=custom_commands_window()
    custom_commands_win.show()
    custom_commands_win.setAttribute(QtCore.Qt.WA_QuitOnClose)
    exit(app.exec_())
