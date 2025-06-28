from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
from file_location import Ui_file_location

button_id=''
close_switch=False
class file_location_window(QMainWindow):
    def __init__(self):
        global button_id
        super().__init__()
        self.ui=Ui_file_location()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()
        self.setWindowFlags(self.windowFlags()|Qt.Tool)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)


        self.programs=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Programs")
        # main functions
        self.ui.back.clicked.connect(self.closing)
        # self.ui.general.clicked.connect(self.send_to_general)
        # self.ui.Premium.clicked.connect(self.send_to_premium)
        # self.ui.personal_info.clicked.connect(self.send_to_personal_info)
        # self.ui.Ai_info.clicked.connect(self.send_to_ai_info)

        # file openers
        self.ui.t1.clicked.connect(self.file_opener_1)
        self.ui.t2.clicked.connect(self.file_opener_2)
        self.ui.t3.clicked.connect(self.file_opener_3)
        self.ui.t4.clicked.connect(self.file_opener_4)
        self.ui.t5.clicked.connect(self.file_opener_5)
        self.ui.t6.clicked.connect(self.file_opener_6)
        self.ui.t7.clicked.connect(self.file_opener_7)
        self.ui.t8.clicked.connect(self.file_opener_8)

        # other functions
        program_names=self.programs.value('program_names').split(',')
        print(program_names)
        try:
            self.ui.n1.setText(str(program_names[0]).capitalize())
            if len(program_names[0])!=0:
                self.ui.f1.setText(self.programs.value(program_names[0]))
        except:
            pass
        try:
            self.ui.n2.setText(str(program_names[1]).capitalize())
            if len(program_names[1])!=0:
                self.ui.f2.setText(self.programs.value(program_names[1]))
        except:
            pass
        try:
            self.ui.n3.setText(str(program_names[2]).capitalize())
            if len(program_names[2])!=0:
                self.ui.f3.setText(self.programs.value(program_names[2]))
        except:
            pass
        try:
            self.ui.n4.setText(str(program_names[3]).capitalize())
            if len(program_names[3])!=0:
                self.ui.f4.setText(self.programs.value(program_names[3]))
        except:
            pass
        try:
            self.ui.n5.setText(str(program_names[4]).capitalize())
            if len(program_names[4])!=0:
                self.ui.f5.setText(self.programs.value(program_names[4]))
        except:
            pass
        try:
            self.ui.n6.setText(str(program_names[5]).capitalize())
            if len(program_names[5])!=0:
                self.ui.f6.setText(self.programs.value(program_names[5]))
        except:
            pass
        try:
            self.ui.n7.setText(str(program_names[6]).capitalize())
            if len(program_names[7])!=0:
                self.ui.f7.setText(self.programs.value(program_names[6]))
        except:
            pass
        try:
            self.ui.n8.setText(str(program_names[7]).capitalize())
            if len(program_names[7])!=0:
                self.ui.f8.setText(self.programs.value(program_names[7]))
        except:
            pass

    # def send_to_premium(self):
    #     from Settings_premium_implementation import premium_window
    #     self.settings_4=premium_window()
    #     self.settings_4.show()
    #     self.close()
    # def send_to_personal_info(self):
    #     from Settings_Personal_info_implementation import personal_info
    #     self.settings_2=personal_info()
    #     self.settings_2.show()
    #     self.close()
    # def send_to_general(self):
    #     from settings_general_implementation import general_window
    #     # self.app=QApplication(sys.argv)
    #     self.settings_1=general_window()
    #     self.settings_1.show()
    #     self.close()
    # def send_to_ai_info(self):
    #     from Settings_AI_info_implementation import ai_info
    #     self.settings_3=ai_info()
    #     self.settings_3.show()
    #     self.close()

    def closeEvent(self,event):
        global close_switch
        if close_switch:
            import os,shutil
            # shutil.rmtree('C:\\ProgramData\\ZeraAI\\Programs')
            # os.mkdir('C:\\ProgramData\\ZeraAI\\Programs')
            self.programs.clear()
            f_location_1=self.ui.f1.text().strip()
            f_location_2=self.ui.f2.text().strip()
            f_location_3=self.ui.f3.text().strip()
            f_location_4=self.ui.f4.text().strip()
            f_location_5=self.ui.f5.text().strip()
            f_location_6=self.ui.f6.text().strip()
            f_location_7=self.ui.f7.text().strip()
            f_location_8=self.ui.f8.text().strip()

            n_name_1=self.ui.n1.text().lower()
            n_name_2=self.ui.n2.text().lower()
            n_name_3=self.ui.n3.text().lower()
            n_name_4=self.ui.n4.text().lower()
            n_name_5=self.ui.n5.text().lower()
            n_name_6=self.ui.n6.text().lower()
            n_name_7=self.ui.n7.text().lower()
            n_name_8=self.ui.n8.text().lower()
            
            names=f"{n_name_1},{n_name_2},{n_name_3},{n_name_4},{n_name_5},{n_name_6},{n_name_7},{n_name_8}"
            self.programs.setValue("program_names",names)
            if n_name_1!="":
                # with open(f"C:\\ProgramData\\ZeraAI\\Programs\\{n_name_1}.txt",'w') as f:
                #     f.write(f_location_1)
                self.programs.setValue(n_name_1,f_location_1)
                
            if n_name_2!="":
                # with open(f"C:\\ProgramData\\ZeraAI\\Programs\\{n_name_2}.txt",'w') as f:
                #     f.write(f_location_2)
                self.programs.setValue(n_name_2,f_location_2)
                
            if n_name_3!="":
                # with open(f"C:\\ProgramData\\ZeraAI\\Programs\\{n_name_3}.txt",'w') as f:
                #     f.write(f_location_3)
                self.programs.setValue(n_name_3,f_location_3)

            if n_name_4!="":
                # with open(f"C:\\ProgramData\\ZeraAI\\Programs\\{n_name_4}.txt",'w') as f:
                #     f.write(f_location_4)
                self.programs.setValue(n_name_4,f_location_4)

            if n_name_5!="":
                # with open(f"C:\\ProgramData\\ZeraAI\\Programs\\{n_name_5}.txt",'w') as f:
                #     f.write(f_location_5)
                self.programs.setValue(n_name_5,f_location_5)

            if n_name_6!="":
                # with open(f"C:\\ProgramData\\ZeraAI\\Programs\\{n_name_6}.txt",'w') as f:
                #     f.write(f_location_6)
                self.programs.setValue(n_name_6,f_location_6)

            if n_name_7!="":
                # with open(f"C:\\ProgramData\\ZeraAI\\Programs\\{n_name_7}.txt",'w') as f:
                #     f.write(f_location_7)
                self.programs.setValue(n_name_7,f_location_7)

            if n_name_8!="":
                # with open(f"C:\\ProgramData\\ZeraAI\\Programs\\{n_name_8}.txt",'w') as f:
                #     f.write(f_location_8)
                self.programs.setValue(n_name_8,f_location_8)
                event.accept()

    def closing(self):
        global close_switch
        close_switch=True
        self.close()
    
    def file_opener_1(self):
        global button_id
        filelocation=QFileDialog.getOpenFileName() 
        path=filelocation[0]
        self.ui.f1.setText(path)

    def file_opener_2(self):
        global button_id
        filelocation=QFileDialog.getOpenFileName()
        path=filelocation[0]
        self.ui.f2.setText(path)
    def file_opener_3(self):
        global button_id
        filelocation=QFileDialog.getOpenFileName()
        path=filelocation[0]
        self.ui.f3.setText(path)
    def file_opener_4(self):
        global button_id
        filelocation=QFileDialog.getOpenFileName()
        path=filelocation[0]
        self.ui.f4.setText(path)
    def file_opener_5(self):
        global button_id
        filelocation=QFileDialog.getOpenFileName()
        path=filelocation[0]
        self.ui.f5.setText(path)
    def file_opener_6(self):
        global button_id
        filelocation=QFileDialog.getOpenFileName()
        path=filelocation[0]
        self.ui.f6.setText(path)
    def file_opener_7(self):
        global button_id
        filelocation=QFileDialog.getOpenFileName()
        path=filelocation[0]
        self.ui.f7.setText(path)
    def file_opener_8(self):
        global button_id
        filelocation=QFileDialog.getOpenFileName()
        path=filelocation[0]
        self.ui.f8.setText(path)
        # movable window
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


if __name__=="__main__":
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
                QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
            QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    QApplication.setAttribute(Qt.AA_DisableHighDpiScaling)
    app=QApplication(sys.argv)
    settings_5=file_location_window()
    settings_5.show()
    settings_5.setAttribute(QtCore.Qt.WA_QuitOnClose)
    exit(app.exec_())