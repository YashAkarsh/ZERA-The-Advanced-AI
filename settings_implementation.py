from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Settings import Ui_MainWindow
import sys
import pyttsx3
import speech_recognition as sr
import sounddevice as sd


class settings_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        #----------------- GENREAL PAGE---------------------

        line_edit_focus=False
        self.setWindowFlag(QtCore.Qt.Tool)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()
        # making settings class
        self.storage_folder=QSettings("Yash Akarsh","ZERA-The Advanced AI")
        self.settings=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Settings")
        
        # buttons
        
        #general page menu buttons 
        self.ui.back.clicked.connect(self.closing)
        self.ui.personal_info_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.ai_info_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.history_button.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))

        # info page menu buttons
        self.ui.back_2.clicked.connect(self.closing)
        self.ui.general_button_2.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.ai_info_button_2.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.ui.history_button_2.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))

        # ai_info page menu buttons
        self.ui.back_3.clicked.connect(self.closing)
        self.ui.general_button_3.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.personal_info_button_3.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.history_button_3.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))

        # history page menu buttons
        self.ui.back_4.clicked.connect(self.closing)
        self.ui.general_button_4.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.personal_info_button_4.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.ui.ai_info_button_4.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))

        # Main General Page Functions
        microphone_list=sr.Microphone.list_microphone_names()
        self.ui.combobox_microphone.addItems(microphone_list)
        self.ui.volume_control.setTickInterval(1)
        self.ui.volume_control.setMaximum(100)
        self.ui.vooice_speed_control.setMaximum(300)
        self.ui.vooice_speed_control.setMinimum(1)
        self.ui.vooice_speed_control.setTickInterval(5)
        self.ui.vooice_speed_control.valueChanged.connect(self.voice_speed_changed)
        self.ui.toolButton.clicked.connect(self.music_directory_select)
        music_folder_path=self.settings.value('music_directory_path')
        self.ui.music_directory.setText(music_folder_path)
        audio_list=sd.query_devices()
        for i in audio_list:
            self.ui.combobox_audio.addItem(str(i['name']))

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

        self.ui.sleep_hotkey.setText(str(sleep_detector).capitalize())
        self.ui.wakeup_hotkey.setText(str(wake_detector).capitalize())
        
        # with open('C:\\ProgramData\\ZeraAI\\Settings.txt') as f:
        #     a=f.readline().strip()
        #     b=f.readline().strip()
        #     c=f.readline().strip()

        try:
            current_microphone=self.settings.value('microphone')
            self.ui.combobox_microphone.setCurrentIndex(current_microphone)
        except:
            self.ui.combobox_microphone.setCurrentIndex(0)

        try:
            current_audio_device=self.settings.value('audio')
            self.ui.combobox_audio.setCurrentIndex(current_audio_device)
        except:
            self.ui.combobox_audio.setCurrentIndex(0)
        
        try:
            current_volume=self.settings.value('volume')
            self.ui.volume_control.setValue(int(float(current_volume)*100))
        except Exception as e:
            print(e)
            self.ui.volume_control.setValue(100)
        
        try:
            current_voice_speed=self.settings.value('voice_speed')
            self.ui.label_14.setText(current_voice_speed)
            self.ui.vooice_speed_control.setValue(int(current_voice_speed))
        except:
            self.ui.vooice_speed_control.setValue(170)
        a=self.settings.value("wake_greeting")
        b=self.settings.value("goodbye_greeting")
        c=self.settings.value("exit_dialog_box")

        power_allow=self.settings.value('power_permission')
        locked_at_launch=self.settings.value('locked_at_launch')
        bool1=False #Boolean for power_permission
        bool2=True  #boolean for locked_at_launch
        try:
            if 'true' in power_allow:
                bool1=True
            if locked_at_launch=='false':
                bool2=False
        except:
            bool1=False

        self.ui.power_permission.setChecked(bool1)
        self.ui.locked_at_launch.setChecked(bool2)
        if a=="true" or a=='True ~~':
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
    
    #----------------- info PAGE---------------------

        self.user_info=QSettings("Yash Akarsh\\ZERA-The Advanced AI","user_info")
        user_name=self.user_info.value("name")
        user_dob=str(self.user_info.value("birth_date")).split(',')
        print(user_dob)
        user_age=self.user_info.value("user_age")
        user_gender=self.user_info.value("gender")
        user_email=self.user_info.value("email")

        if user_gender=='sir':
            self.ui.male_radioButton.setChecked(True)
        else:
            self.ui.female_radioButton.setChecked(True)

        self.ui.username_area.setText(user_name)
        self.ui.birth_date_area.setDate(QDate(int(user_dob[0]),int(user_dob[1]),int(user_dob[2])))
        self.ui.email_area.setText(user_email)
        self.ui.age_area.setValue(int(user_age))


        # button
        self.ui.back_2.clicked.connect(self.closing)

        #----------------- ai_info PAGE---------------------

        # buttons
        self.ui.back_3.clicked.connect(self.closing)
        self.center()

        self.ai_info=QSettings("Yash Akarsh\\ZERA-The Advanced AI","AI_Settings")

        # extras
        # with open("C:\\ProgramData\\ZeraAI\\AI_settings.txt",'r') as f:
        name=self.ai_info.value("ai_name")
        voice_idx=self.ai_info.value("ai_voice")

        
        # self.ui.label_16.setText(name.strip())
        if name.strip()=='Jarvis':
            self.ui.label_16.setText('Current AI :- Jarvis')
            self.ui.jarvis_radioButton.setChecked(True)
    
        # voice management
        engine=pyttsx3.init()
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
        self.ui.voice_selector_comboBox.addItems(v_names)
        
        try:
            self.ui.voice_selector_comboBox.setCurrentIndex(int(voice_idx))
        except Exception as e:
            print(e)
            if name.lower()=="zera":
                try:
                    id=v_names.index("Cortana")
                    self.ui.voice_selector_comboBox.setCurrentIndex(id)
                except:
                    self.ui.voice_selector_comboBox.setCurrentIndex(0)
            else:
                id=v_names.index("Mark")
                try:
                    self.ui.voice_selector_comboBox.setCurrentIndex(id)
                except:
                    self.ui.voice_selector_comboBox.setCurrentIndex(0)

        #----------------- History PAGE---------------------
        # timer=QTimer()
        # timer.timeout.connect(self.update_history)
        chat_history=str(self.settings.value('history'))
        self.ui.textEdit.setReadOnly(True)
        if chat_history!='':
            chat_history=chat_history.split(',')
            chat_history="\n".join(chat_history)
            self.ui.textEdit.setText(chat_history)
        else:
            self.ui.textEdit.setPlaceholderText('Currently No History To Show')

        self.ui.clear_button.clicked.connect(self.clear_history)

    def clear_history(self):
        from Main_AI import history_list
        self.ui.textEdit.clear()
        self.settings.setValue('history','')
        history_list=[]
    def voice_speed_changed(self):
        from Main_AI import speak
        crnt_speed=self.ui.vooice_speed_control.value()
        # if crnt_speed==170:
        #     self.ui.label_6.setText('Default Voice Speed')
        # else:
        #     self.ui.label_6.setText('Voice Speed')
        if crnt_speed==170:
            self.ui.label_14.setText(f'{crnt_speed}-Default')
        else:
            self.ui.label_14.setText(f'{crnt_speed}')

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
            settings_win.close()
         
        except Exception as e:
            print(e)
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

    def music_directory_select(self):
        folder=QFileDialog.getExistingDirectory(self, str("Open Directory"),
                                             "/home",
                                             QFileDialog.ShowDirsOnly
                                             | QFileDialog.DontResolveSymlinks)
        self.ui.music_directory.setText(str(folder))

    def closing(self):
        sleeping_hotword=self.ui.sleep_hotkey.text()
        waking_hotword=self.ui.wakeup_hotkey.text()
        wake_greeting=self.ui.checkBox.isChecked()
        goodbye_greeting=self.ui.checkBox_2.isChecked()
        exit_dialog_box=self.ui.checkBox_3.isChecked()
        microphone=self.ui.combobox_microphone.currentIndex()
        audio_device=self.ui.combobox_audio.currentIndex()
        volume=str((self.ui.volume_control.value())/100)
        voice_speed=str(self.ui.vooice_speed_control.value())
        music_folder=self.ui.music_directory.text()
        power_allow=self.ui.power_permission.isChecked()
        locked_at_launch=self.ui.locked_at_launch.isChecked()

        Which_AI=''
        Voice=self.ui.voice_selector_comboBox.currentIndex()
        if self.ui.zera_radioButton.isChecked():
            Which_AI='Zera' 
        elif self.ui.jarvis_radioButton.isChecked():
            Which_AI='Jarvis'
        # with open("C:\\PRogramData\\ZeraAI\\AI_Settings.txt",'w') as f:
        #     f.write(f"{Which_AI}\n{Voice}")
        self.ai_info.setValue("ai_name",Which_AI)
        self.ai_info.setValue("ai_voice",str(Voice))

        get_name=self.ui.username_area.text().split()
        get_dob=self.ui.birth_date_area.date()
        dob=f"{get_dob.year()},{get_dob.month()},{get_dob.day()}"
        get_email=self.ui.email_area.text().strip()
        get_age=self.ui.age_area.value()
        gender=''
        if self.ui.male_radioButton.isChecked():
            gender='sir'
        else:
            gender='maam'
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
        self.user_info.setValue("birth_date",dob)
        self.user_info.setValue("email",get_email)
        self.user_info.setValue('user_age',str(get_age))
        self.user_info.setValue('gender',gender)

        # try:
        #     os.remove('C:\\ProgramData\\ZeraAI\\hotkeys.txt')
        # except Exception:
        #     pass
        # with open('C:\\ProgramData\\ZeraAI\\hotkeys.txt','w') as f:
        #     f.write(f'{waking_hotword}\n{sleeping_hotword}')

        self.settings.setValue("waking_hotkey",waking_hotword)
        self.settings.setValue('sleeping_hotkey',sleeping_hotword)
        self.settings.setValue('microphone',microphone)
        self.settings.setValue('audio',audio_device)
        self.settings.setValue('volume',volume)
        self.settings.setValue('voice_speed',voice_speed)
        self.settings.setValue('music_directory_path',music_folder)

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
        self.settings.setValue('power_permission',power_allow)
        self.settings.setValue('locked_at_launch',locked_at_launch)
        # settings_win.close()
        self.close()
        # print(True)

if "__main__"==__name__:
    # if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    #     print('highDpi')
    #     QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, False)
    #     print('highDpi-2')
    # if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    #         QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    # QWidget.setAttribute(Qt.AA_DisableHighDpiScaling)
    # QApplication.setAttribute(Qt.AA_DisableHighDpiScaling)
    
    app=QApplication(sys.argv)
    settings_win=settings_window()
    settings_win.show()
    settings_win.setAttribute(QtCore.Qt.WA_QuitOnClose)
    exit(app.exec_())

    