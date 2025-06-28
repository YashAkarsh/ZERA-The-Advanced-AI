from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
from loading_screeen import Ui_MainWindow
import os



# checking admin
import ctypes, sys
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
# ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
class Loading_window(QMainWindow):
    def __init__(self):
        self.counter=0
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.Tool)
        self.timer= QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(35)
        self.center()

        # self.spacerItem = QtWidgets.QSpacerItem(435, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        # self.ui.gridLayout_2.addItem(self.spacerItem, 1, 2, 1, 1)
        if not os.path.exists('C:\\ProgramData\\ZeraAI'):
            os.mkdir('C:\\ProgramData\\ZeraAI')
    def progress(self):
        self.counter+=10
        settings=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Settings")

        self.ui.frame_2.setMaximumSize(QtCore.QSize(self.counter, 50))
        if self.counter==1000:
            if os.path.exists('C:\\ProgramData\\ZeraAI'):
                if settings.value("waking_hotkey")!=None:
                    try:
                                # with open('C:\\ProgramData\\ZeraAI\\user_occurence.txt','r') as f:
                                #         data=f.read()
                                # if data!='new':
                                #         print('printing')
                                #         os.startfile('Loading_responsive.exe')
                                #         sys.exit()
                                
                                import Main_AI

                                if settings.value("sleeping_hotkey")!=None:
                                    settings=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Settings")            
                                    Zera=Main_AI.Main()
                                    Zera.show()
                                    Main_AI.speak('')
                                    W_greetings=settings.value("wake_greeting")
                                    if W_greetings=='true':
                                            Main_AI.greet_switch=True
                                            Zera.run_task()
                                    data_other=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Other")
                                    d=data_other.value("user_occurence")
                                    if d=='new_2':
                                            Zera.run_task()  
                                    self.hide()
                    except:
                        pass
                else:
                    from setup_implementation import setup_window
                    self.setup_win=setup_window()
                    self.setup_win.show()
                    self.hide()
                    # self.close()

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
if __name__=='__main__':
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
                QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
            QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    app=QApplication(sys.argv)
    settings=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Settings")
    load_win=Loading_window()
    load_win.show()
    load_win.setAttribute(QtCore.Qt.WA_QuitOnClose)
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

