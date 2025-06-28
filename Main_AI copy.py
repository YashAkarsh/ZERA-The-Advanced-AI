import ctypes
import sys
import pyttsx3
import speech_recognition as sr
try:
        import pywhatkit
except:
        pass
import os
import random 
import webbrowser
import time
import datetime
import pyautogui
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from ZeraGUI import Ui_MainWindow
import sys
import keyboard
import wolframalpha
import wikipedia
from PyQt5.QtCore import pyqtSignal as SIGNAL
import sounddevice as sd
# import playsound
# import winsound
from pygame import mixer
import asyncio
import io
from pydub import AudioSegment
from pydub.playback import play
import edge_tts

mixer.init()

# switch
switch=False
greet_switch=False
switch_activator=True
sleep=False
listen_switch=True
sleep_countdown=0 # to automatically sleep when not in use for a long time
exit_switch=False
bar_activator=False
main_active=True
settings_hovered_switch=False
main_switch=False # True- Wake, False- Sleep
application_close_switch=False
music_switch=False
pause=False


current_song=0
AI_State='Zera'
textbox=''
history_list=[]
age='22'
wishing_words='good morning','good evening','good night','good afternoon'
appreciate_words='good','nice','god','cool','wow','ya','why not'
yes_words='yes','why not','sure','okay','of course'
no_words='nope','no','no way','nah','nahi','na'
words_to_text=''
numbers='1','2','3','4','5','6','7','8','9','0'
message=''


# wolframalpha
api=wolframalpha.Client('KGQWTR-73Q5WR5JGY')

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

try:

        ai_settings=QSettings("Yash Akarsh\\ZERA-The Advanced AI","AI_Settings")
        name=ai_settings.value("ai_name")
        voice=ai_settings.value("ai_voice")
        try:
                engine.setProperty('voice',voices[int(voice)].id)
        except Exception:
                engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_Cortana')

        engine.setProperty('rate',170)
except Exception:
        pass
try:
        user_info=QSettings("Yash Akarsh\\ZERA-The Advanced AI",'user_info')
        username=user_info.value("name")
        dob=user_info.value("birth_date")
        age=user_info.value("user_age")
        gender=user_info.value("gender")

        if len(gender)==0:
                username=username.split()
                names='',username[0]
                gender=random.choice(names)
except Exception:
        pass

miccel_settings=QSettings('Yash Akarsh\\ZERA-The Advanced AI','Settings')
voice_volume=miccel_settings.value('volume')
voice_speed=miccel_settings.value('voice_speed')
audio_device=miccel_settings.value('audio')
try:
        try:
                mic_index=miccel_settings.value('microphone')
        except:
                mic_index=0
        sd.default.device=[mic_index,audio_device]
        print('successful')
except Exception as e:
        print(e)
try:
        current_song_volume=float(voice_volume)
except:
        current_song_volume=1
try:
        engine.setProperty('rate',int(voice_speed))
except:
        engine.setProperty('rate',170)
try:
        engine.setProperty('volume',float(voice_volume))
except:
        engine.setProperty('volume',1)
def command2():
        recognize=sr.Recognizer()
        with sr.Microphone() as source:
                try:
                        listener=recognize.listen(source,timeout=3)
                        recognize.adjust_for_ambient_noise(source, duration=1) 
                except Exception:
                        pass
        try:
                recognizer=recognize.recognize_google(listener,language='en-in')

        except Exception:
                return ''
        return recognizer
def command3():
        global words_to_text
        recognize=sr.Recognizer()
        with sr.Microphone() as source:
                try:
                        listener=recognize.listen(source,timeout=3)
                        recognize.adjust_for_ambient_noise(source,duration=1)
                except Exception:
                        pass
        try:
                recognizer=recognize.recognize_google(listener,language='en-in')
                words_to_text=recognizer
        except Exception:
                return ''
        return recognizer

# def speak(audio):
#         global textbox
#         engine.say(audio)
#         try:
#                 engine.runAndWait()
#         except:
#                 if engine._inLoop:
#                         engine.endLoop()

# def speak(text, voice="en-IN-NeerjaNeural"):
#         if len(text)==0:
#                 print('herer')
#                 return
#         voices =edge_tts.list_voices()
#         voice_names = [v['ShortName'] for v in voices if v['Locale'].startswith("en")]

#         communicate = edge_tts.Communicate(text=text, voice=voice)

#         buffer = io.BytesIO()

#         for chunk in communicate.stream():
#                 if chunk["type"] == "audio":
#                         buffer.write(chunk["data"])

#         buffer.seek(0)
#         audio = AudioSegment.from_file(buffer, format="mp3")
#         play(audio)  # Uses ffplay or pyaudio if installed


def speak(text: str, voice="en-US-JennyNeural"):
    if not text.strip():
        return

    async def speak_async():
        communicate = edge_tts.Communicate(text=text, voice=voice)
        mp3_bytes = b""

        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                mp3_bytes += chunk["data"]

        buffer = io.BytesIO(mp3_bytes)
        audio = AudioSegment.from_file(buffer, format="mp3")
        play(audio)

    asyncio.run(speak_async())

def open_Chrome():
        try:
                os.startfile("chrome.exe")
        except:
                speak("Sorry; no such file")
def open_notepad():
        os.startfile('notepad.exe')
def open_cmd():
        os.startfile('cmd.exe')
def open_other_files(software):
        # print(software)
        try:
                # program_locations=os.listdir("C:\\ProgramData\\ZeraAI\\Programs")
                # program_locations=str(program_locations)
                open_programs=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Programs")
                try:
                        # program_locations2=program_locations.replace('.txt','')
                        program_names=open_programs.value("program_names")
                        program_names=program_names.split(",")
                        if software.strip() in program_names:
                                # with open(f'C:\\ProgramData\\ZeraAI\\Programs\\{software.strip()}.txt','r') as f:
                                #         data=f.read()
                                data=open_programs.value(software)
                                os.startfile(data)
                        else:
                                pyautogui.press('win')
                                time.sleep(1)
                                pyautogui.typewrite(software)
                                time.sleep(1)
                                pyautogui.press('enter')
                # print(program_locations2)
                except:
                        speak('Sorry no such files')
        except:
                pass
def search_google(search_what):
        pywhatkit.search(search_what)
def search_youtube(search_what_on_youtube):
        pywhatkit.playonyt(search_what_on_youtube)
def temperature(pl):
        speak('getting the temperature')
        resp=api.query(pl)
        try:
                speak(f'The temperature outside is {next(resp.results).text}')
        except Exception:
                speak('sorry; no internet connection')
def calc(calculatewhat):
        resp=api.query(calculatewhat)
        try:
                speak(f"your answer is; {next(resp.results).text}")
        except Exception:
                speak('Sorry; no internet connection')

class Temp_background_listener(QThread):
        def __init__(self):
                super(Temp_background_listener,self).__init__()
        def run(self):
                self.brain_2()
        def temporary_listen(self):
                global words_to_text
                recognize=sr.Recognizer()
                with sr.Microphone() as source:
                        # speak('listening...')
                        try:
                                print('listening...(background)')
                                listener=recognize.listen(source,timeout=3)
                                recognize.adjust_for_ambient_noise(source)
                        except Exception:
                                # print('Error!')
                                pass
                try:
                        print('recognizing..(background)')
                        recognizer=recognize.recognize_google(listener,language='en-in')
                        print(recognizer)
                        
                except Exception:
                        # print('sorry; Please say it again!')
                        return ''
                return recognizer
        def brain_2(self):
                self.user_2=self.temporary_listen()
                if 'stop' in self.user_2:
                        print('okay')

class Activator_thread(QThread):
        def __init__(self):
                super(Activator_thread,self).__init__()
        
        def run(self):
                global exit_switch,main_switch,music_switch,current_song,pause,switch,current_song_volume
                while True:
                        if switch_activator:
                                self.settings=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Settings")
                                self.other_0=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Other")
                                
                                # with open('C:\\ProgramData\\ZeraAI\\hotkeys.txt','r') as f:
                                #         wake_key=f.readline().lower()
                                #         sleep_key=f.readline().lower()
                                wake_key=self.settings.value("waking_hotkey")
                                sleep_key=self.settings.value("sleeping_hotkey")
                                key_times=0

                                if switch_activator:
                                        key_reader=keyboard.read_key()
                                        try:
                                                if main_active:      
                                                        if key_reader==(wake_key).lower():
                                                                # with open('C:\\ProgramData\\ZeraAI\\condition.txt','w') as f:
                                                                #         f.write('wakeup')
                                                                self.other_0.setValue('condition','wakeup')
                                                                main_switch=True
                                                        elif key_reader==(sleep_key).lower():
                                                                # with open("C:\\ProgramData\\ZeraAI\\condition.txt",'w') as f:
                                                                #         f.write('sleep')
                                                                self.other_0.setValue('condition',"sleep")
                                                                main_switch=False
                                                        
                                                        # Music Controls
                                                        if keyboard.is_pressed('esc'):
                                                                mixer.music.stop()
                                                                music_switch=False
                                                        elif keyboard.is_pressed('space'):
                                                                if pause:
                                                                        print('resume')
                                                                        mixer.music.unpause()
                                                                        pause=False
                                                                else:
                                                                        print('pause')
                                                                        mixer.music.pause()
                                                                        pause=True
                                                        elif keyboard.is_pressed('right'):
                                                                if music_switch:
                                                                        try:
                                                                                self.song_dir_path=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Settings")
                                                                                music_folder=self.song_dir_path.value('music_directory_path')
                                                                                songs_list=os.listdir(music_folder)
                                                                                if current_song<len(songs_list):
                                                                                        current_song+=1     
                                                                                        mixer.music.load(f"{music_folder}\\{songs_list[current_song]}")
                                                                                        mixer.music.play()
                                                                                else:
                                                                                        current_song=0
                                                                                        mixer.music.load(f"{music_folder}\\{songs_list[current_song]}")
                                                                                        mixer.music.play()
                                                                        except:
                                                                                speak('sorry I am facing issues playing songs from your music directory; try changing the file path in settings')
                                                                                
                                                        elif keyboard.is_pressed('left'):
                                                                if music_switch:
                                                                        try:
                                                                                self.song_dir_path=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Settings")
                                                                                music_folder=self.song_dir_path.value('music_directory_path')
                                                                                songs_list=os.listdir(music_folder)
                                                                                if current_song<len(songs_list):
                                                                                        current_song-=1     
                                                                                        mixer.music.load(f"{music_folder}\\{songs_list[current_song]}")
                                                                                        mixer.music.play()
                                                                                else:
                                                                                        current_song=0
                                                                                        mixer.music.load(f"{music_folder}\\{songs_list[current_song]}")
                                                                                        mixer.music.play()
                                                                        except:
                                                                                speak('sorry I am facing issues playing songs from your music directory; try changing the file path in settings')
                                                        elif keyboard.is_pressed('up'):
                                                                current_song_volume+=0.1
                                                                mixer.music.set_volume(current_song_volume)
                                                        elif keyboard.is_pressed('down'):
                                                                current_song_volume-=0.1
                                                                mixer.music.set_volume(current_song_volume)
                                                else:
                                                        pass
                                                
                                        except Exception as e:
                                                print(e)
                                                # pass
                                else:
                                        # if exit_switch:
                                        sys.exit()
                        else:
                                # if exit_switch:
                                self.exit()

class music_player(QThread):
        def __init__(self):
                super(music_player,self).__init__()
        
        def run(self):
                global music_switch,current_song,current_song_volume
                self.song_dir_path=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Settings")
                music_folder=self.song_dir_path.value('music_directory_path')
                if music_folder=='' or music_folder==None:
                        speak('Please enter the path of your music directory in settings; to play songs')
                else:                
                        try:
                                songs_list=os.listdir(music_folder)     
                                print(songs_list)

                                # for i in range(len(songs_list)-1):              
                                if music_switch:
                                        speak('Okay playing songs from your music folder')
                                        speak('if you want to learn how to control the music just say; music controls')           

                                        if current_song<len(songs_list):
                                                        print(f'playing {songs_list[current_song]}')
                                                        mixer.music.set_volume(current_song_volume)
                                                        mixer.music.load(f"{music_folder}\\{songs_list[current_song]}")
                                                        if mixer.music.get_busy():
                                                                pass
                                                        else:
                                                                print('done')
                                                                current_song+=1
                                                        mixer.music.play()
                                                        mixer.music.queue(f"{music_folder}\\{songs_list[current_song]}")
                        except:
                                speak('sorry I am facing issues playing songs from your music directory; try changing the file path in settings')

                
        
class MainThread(QThread):  
        def __init__(self):
                super(MainThread,self).__init__()  
        def run(self):
                global switch
                while True:
                        try:
                                self.other_1=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Other")
                                # with open('C:\\ProgramData\\ZeraAI\\condition.txt','r') as f:
                                #         value=f.read()
                                value=self.other_1.value("condition")
                                if value=='reset':
                                        self.exit()
                                if value=='wakeup':
                                        # self.ui.Ai_state.setText('Listening...')
                                        switch=True
                                        self.brain()
                                        break
                                # elif value=='sleep':
                                #         switch=False
                                #         break
                                # app.processEvents()
                        except:
                                pass
                self.brain()
        
        def command(self):
                global textbox,AI_State,listen_switch,sleep_countdown,bar_activator,main_switch
                recognize=sr.Recognizer()
                self.other_2=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Other")

                try:
                        try:
                                mic_index=self.settings.value('microphone')
                        except:
                                mic_index=0
                        with sr.Microphone(device_index=mic_index) as source:
                                bar_activator=True
                                try:
                                        # if not internet:
                                        # with open('C:\\ProgramData\\ZeraAI\\condition.txt','r') as f:
                                        #         data=f.read().strip()
                                        data=self.other_2.value("condition")
                                        if data=='sleep':
                                                # if not internet:
                                                sleep_messages="Okay; going to sleep!","Alright! going to sleep"
                                                # sleep_messages=["No internet connection. please connect to a stable network"]
                                                speak(random.choice(sleep_messages))
                                                # AI_State='Sleeping...'
                                                AI_State=name
                                                switch=False
                                                sleep=True
                                                sleep_countdown=0
                                                listen_switch=True
                                                self.sleep_mode()

                                        if listen_switch:
                                                speak('listening')
                                        # recognize.pause_threshold=0.5 
                                        # bar_activator=False
                                        listener=recognize.listen(source,timeout=3)
                                        recognize.adjust_for_ambient_noise(source, duration=1)

                                        # recognize.adjust_for_ambient_noise(source)
                                        # with open('C:\\ProgramData\\ZeraAI\\condition.txt','r') as f:
                                        #         data=f.read().strip()
                                        data=self.other_2.value("condition")
                                        if data=='sleep':
                                                sleep_messages="Okay; going to sleep!","Alright! going to sleep"
                                                speak(random.choice(sleep_messages))
                                                AI_State='Sleeping...'
                                                AI_State=name
                                                switch=False    
                                                sleep=True
                                                sleep_countdown=0
                                                listen_switch=True
                                                main_switch=False
                                                self.sleep_mode()
                                                                           
                                
                                # recognize.energy_threshold=200
                                except sr.WaitTimeoutError:
                                        print("❗ No speech detected (timeout).")
                                except sr.UnknownValueError:
                                        print("❗ Could not understand audio.")
                                except sr.RequestError as e:
                                        print(f"❗ Could not request results; {e}")
                                # except Exception as e:
                                #         print(f"❗ Other error: {e}")
                                except Exception as e:
                                        print("Error:",e)
                                        if 'listening timed out while waiting for phrase to start' in str(e).strip():
                                                speak('sorry; am facing some issues with your microphone')
                                        elif "name 'other' is not defined" in str(e).strip():
                                               print("passing") 
                                        else:
                                                speak('Sorry I am unable to detect a microphone; please attach a microphone to your device and try again.')
                                                # with open("C:\\ProgramData\\ZeraAI\\condition.txt",'w') as f:
                                                #         f.write('sleep')
                                                self.other_2.setValue("condition",'sleep')
                                                # with open('C:\\ProgramData\\ZeraAI\\condition.txt','r') as f:
                                                #         data=f.read().strip()
                                                data=self.other_2.value("condition")
                                                if data=='sleep':
                                                        # sleep_messages="Okay; going to sleep!","Alright! going to sleep"
                                                        # speak(random.choice(sleep_messages))
                                                        # AI_State='Sleeping...'
                                                        AI_State=name
                                                        switch=False
                                                        sleep=True
                                                        sleep_countdown=0
                                                        listen_switch=True
                                                        self.sleep_mode()
                except Exception:
                        pass
                # if internet:
                try:
                        # other_entries=QSettings("Yash Akarsh\\ZERA-The Advanced AI",'Other')
                        # print('recognizing..')
                        recognizer=recognize.recognize_google(listener,language='en-us')
                        recognize.adjust_for_ambient_noise(source, duration=1)
                        # recognizer=recognize.recognize_sphinx(source,language='en-in')
                        textbox=f"You: {recognizer}"
                        # history_list.append(textbox)
                        listen_switch=True
                        sleep_countdown=0
                except Exception as e:
                        
                        # print(f"{name.strip()}: {e}")
                        # textbox=f"{name.strip()}: Sorry; please say that again!"
                        # textbox=f"{name.strip()}: {e}"

                        exc=str(e)
                        exc=(exc.strip()).split()
                        # print(f'{exc}')                        
                        if exc=="recognition connection failed: [Errno 11001] getaddrinfo failed".split():
                                self.other_2=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Other")

                                speak('No internet connection. Please connect to a stable network.\ngoing to sleep mode')
                                # AI_State='Sleeping...'
                                AI_State=name
                                # with open("C:\\ProgramData\\ZeraAI\\condition.txt",'w') as f:
                                #         f.write('sleep')
                                self.other_2.setValue("condition","sleep")
                                # with open('C:\\ProgramData\\ZeraAI\\condition.txt','r') as f:
                                #         data=f.read().strip()
                                data=self.other_2.value("condition")
                                if data=='sleep':
                                        # sleep_messages="Okay; going to sleep!","Alright! going to sleep"
                                        # speak(random.choice(sleep_messages))
                                        # AI_State='Sleeping...'
                                        AI_State=name
                                        switch=False
                                        sleep=True
                                        sleep_countdown=0
                                        listen_switch=True
                                        self.sleep_mode()

                        listen_switch=False
                        sleep_countdown+=1
                        return 'None'
                return recognizer


        def sleep_mode(self):
                global switch,bar_activator
                # print('now in sleep')
                # self.record=command2().lower()
                self.other_3=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Other")

                while True:
                        bar_activator=False
                        # Zera.ui.movie.stop()
                        # with open('C:\\ProgramData\\ZeraAI\\condition.txt') as f:
                        #         data=f.read()
                        data=self.other_3.value("condition")
                        if data=='wakeup':
                                switch=True
                                self.brain()
                                break
                        else:
                                pass

        def brain(self):
                global switch,sleep,numbers,AI_State,sleep_countdown,message,switch_activator,main_switch,greet_switch,music_switch
                # print(sleep_countdown)
                # print(switch2)
                self.settings=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Settings")
                self.other_4=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Other")

                # with open('C:\\ProgramData\\ZeraAI\\condition.txt','w') as f:
                #         f.write('')
                self.other_4.setValue("condition","")

                while switch:
                        # with open('C:\\ProgramData\\ZeraAI\\condition.txt','r') as f:
                        #                 data=f.read().strip()
                        data=self.other_4.value("condition")
                        if data=='sleep':
                                sleep_messages="Okay; going to sleep!","Alright! going to sleep"
                                speak(random.choice(sleep_messages))
                                # AI_State='Sleeping...'
                                AI_State=name
                                switch=False
                                sleep=True
                                listen_switch=True
                                sleep_countdown=0      
                                self.sleep_mode()
                                break
                        # with open('C:\\ProgramData\\ZeraAI\\Settings.txt','r') as f:
                        wake_greet=self.settings.value("wake_greeting")
                        sleep_greet=self.settings.value("goodbye_greeting")
                        exit_box=self.settings.value("exit_dialog_box")
                        if greet_switch:
                                if wake_greet=='true' and self.other_4.value("user_occurence")=='old':
                                        greeting_time=int(datetime.datetime.now().hour)
                                        current_time=datetime.datetime.now()
                                        current_time=current_time.strftime('%I:%M')
                                        if int(greeting_time)>=12 and greeting_time<=16:
                                                ans=f'good afternoon {gender}; Its {current_time} pm'
                                        elif int(greeting_time)>16:
                                                ans=f'good evening {gender}; Its {current_time} pm'
                                        elif int(greeting_time)<12 and greeting_time>=4:
                                                ans=f'good evening {gender}; Its {current_time} am'
                                        elif int(greeting_time)>=0 and greeting_time<=3:
                                                ans=f'good evening {gender}; Its {current_time} am'
                                        greetings_welcome=ans,f'Welcome back {gender}!'
                                        speak(random.choice(greetings_welcome))
                                        # print(f'welcome back {gender}')
                                        # with open('C:\\ProgramData\\ZeraAI\\Settings.txt','w') as f:
                                        #         f.write(f'wakeup_greeting ~~\n{sleep_greet}\n{exit_box}')
                                        self.settings.setValue("wake_greeting","True ~~")
                                        # AI_State='Sleeping...'
                                        AI_State=name
                                        switch=False
                                        main_switch=False
                                        greet_switch=False
                                        # sleep=True
                                        self.sleep_mode()
                                        sleep_countdown=0
                                        break

                        neworold=self.other_4.value("user_occurence")
                        if neworold=='new_2':
                                global main_active
                                print("Test 2 complete")
                                AI_State='Speaking...'
                                act_execution=Activator_thread()
                                speak(f'Hello.. I am {name}.. your personal Assistant.. I can help you with your daily work, on this PC; just click at the center and say What are your features to get all the features')
                                # with open('C:\\PRogramData\\ZeraAI\\condition.txt','w') as f:
                                #         f.write('sleep')
                                if not switch_activator:
                                        switch_activator=True
                                if not main_active:
                                        main_active=True
                                self.other_4.setValue("condition",'sleep')
                                self.other_4.setValue("user_occurence","old")
                                # AI_State='Sleeping...'
                                AI_State=name
                                switch=False
                                main_switch=False
                                self.sleep_mode()
                                break
                        # if sleep_countdown==500:
                        #         pass
                        else:  
                                AI_State='Listening...' 
                                self.user=self.command().lower()
                                custom_chat_bool=False
                                try:
                                        custom_chat=self.settings.value('custom_commands')
                                        query_list=list(custom_chat.keys())
                                        custom_chat_bool=True
                                except:
                                        query_list=[]
                                        custom_chat_bool=False
                                
                                # chatbot
                                if self.user in query_list and custom_chat_bool==True:
                                        speak(custom_chat[self.user])
                                else:
                                        # exception
                                        if 'say' in self.user and 'to' in self.user:
                                                self.user=self.user.replace('say','')
                                                self.user=self.user.replace('to','')
                                                speak(self.user)
                                        elif 'say' in self.user:
                                                self.user=self.user.replace('say','')
                                                speak(self.user)
                                        elif 'music' in self.user and 'controls' in self.user:
                                                speak('Press escape button on your keyboard to stop the music;; Press space button to pause or resume;; Use right and left buttons to scorll through your playlist;; up and down arrow keys are used to control the volume')
                                        elif 'play' in self.user or 'song' in self.user or 'music' in self.user:
                                                music_player_instance=music_player()
                                                music_player_instance.start()
                                                music_switch=True
                                                self.other_4.setValue("condition",'sleep')
                                                self.other_4.setValue("user_occurence","old")
                                                # AI_State='Sleeping...'
                                                AI_State=name
                                                switch=False
                                                main_switch=False
                                                self.sleep_mode()
                                                break
                                        elif 'on youtube' in self.user or 'in youtube' in self.user or 'play' in self.user:
                                                try:
                                                        self.user=self.user.replace('search',"")
                                                        self.user=self.user.replace('on youtube',"")
                                                except:
                                                        self.user=self.user.replace('search',"")
                                                        self.user=self.user.replace('in youtube',"")
                                                if 'play' in self.user:
                                                        self.user=self.user.replace('play','')
                                                speak(f'playing {self.user} on youtube')
                                                search_youtube(self.user)       
                                        elif 'search' in self.user:
                                                self.user=self.user.split()
                                                id=self.user.index('search')
                                                what_to_search=self.user[id+1:]
                                                self.user=" ".join(what_to_search)
                                                self.user=str(self.user)
                                                # self.user=self.user.replace('search','')
                                                if 'on google' in self.user:
                                                        self.user=self.user.replace('on google','')
                                                elif 'on chrome' in self.user:
                                                        self.user=self.user.replace('on chrome','')
                                                elif 'on google' in self.user and 'on chrome' in self.user:
                                                        self.user=self.user.replace('on google','')
                                                        self.user=self.user.replace('on chrome','')
                                                elif 'in google' in self.user:
                                                        self.user=self.user.replace('in google','')
                                                elif 'in chrome' in self.user:
                                                        self.user=self.user.replace('in chrome','')
                                                elif 'in google' in self.user and 'in chrome' in self.user:
                                                        self.user=self.user.replace('in google','')
                                                        self.user=self.user.replace('in chrome','')
                                                elif 'google' in self.user:
                                                        self.user=self.user.replace('google','')
                                                elif 'chrome' in self.user:
                                                        self.user=self.user.replace('chrome','')
                                                elif 'google' in self.user and 'chrome' in self.user:
                                                        self.user=self.user.replace('google','')
                                                        self.user=self.user.replace('chrome','')
                                                else:
                                                        pass
                                                speak(f'searching {self.user} on google')
                                                search_google(self.user)
                                        elif self.user.startswith('hello') or self.user.startswith('hi') or self.user.startswith('hai'):
                                                a1=f'Hello {gender}!',f'Hi {gender}!',"Hello there!",'Hi there!'
                                                speak(random.choice(a1))
                                        elif 'what' in self.user and 'your name' in self.user:
                                                a2=f'I am {name}',f'My name is {name}',f'Hello! I am {name}'
                                                speak(random.choice(a2))
                                        elif 'thank you' in self.user or 'thanks' in self.user:
                                                a3='Your most welcome',f'Your welcome {gender};'
                                                speak(random.choice(a3))
                                        elif 'who' in self.user and 'are you' in self.user:
                                                a4=f'I am {name}; nice to meet you!',f'Hello; I am {name}; your personal assistant!',f'Hello; I am {name}; nice to meet you!'
                                                speak(random.choice(a4)) 
                                        elif 'how are' in self.user and 'you' in self.user:
                                                a5='I am fine; Thankyou for asking','I am absolutely fine!','I am fine!'
                                                speak(random.choice(a5))
                                        elif 'f***' in self.user or 'hell' in self.user:
                                                a6='AAAh!; I cannot hear that',"Please dont say it again!","I cannot tolerate that"
                                                speak(random.choice(a6))
                                        
                                        elif 'love' in self.user:
                                                a7='I can be your best friend',"I am just a machine","I am an artifitial intelligence and not a human so i cannot love",'I am afraid I cannot'
                                                speak(random.choice(a7))
                                        elif 'who' in self.user and 'your developer' in self.user or 'who' in self.user and 'is your creator' in self.user or 'who' in self.user and 'created you' in self.user or 'who' in self.user and 'made you' in self.user:
                                                a11='I was developed by Yash Akarsh','I was made by Yash Akarsh','My developer is Yash Akarsh','Yash Akarsh is my developer'
                                                speak(random.choice(a11))
                                        elif '**' in self.user:
                                                speak('moving on!')

                                        elif self.user in wishing_words:
                                                if 'good morning' in self.user:
                                                        speak(f'Good Morning {gender}!')
                                                elif 'good afternoon' in self.user:
                                                        speak(f'Good afternoon {gender}!')
                                                elif 'good evening' in self.user:
                                                        speak(f'Good evening {gender}!')
                                                elif 'good night' in self.user:
                                                        speak(f'Good night {gender}')
                                        elif self.user in appreciate_words:
                                                variate5='Thanks!',''
                                                speak(random.choice(variate5))
                                        elif 'good' in self.user:
                                                speak("thanks")
                                        elif 'what' in self.user and 'my name' in self.user:
                                                speak(f'Your name is {username}')
                                        elif 'what are your features' in self.user:
                                                speak('My features are;; I can talk to you like a real person;; I can open programs for you;; I can play youtube videos;; I can type for you in a text file;; I can search anything for you on google;; I can give you information about anything;; I can create text files for you;;')
                                        elif 'what' in self.user and 'are you' in self.user:
                                                speak('I am an Artificial Intelligence')
                                        elif 'why' in self.user and 'are you' in self.user:
                                                a12=f'to help you {gender}','because of you'
                                                speak(random.choice(a12))
                                        elif 'friends with me' in self.user:
                                                a13='why not','sure','ofcource','we are friends already'
                                                speak(random.choice(a13))
                                        elif 'I hate you' in self.user or 'you are' in self.user and 'bad' in self.user or 'disgusting' in self.user:
                                                a14='I am sorry for everything I did wrong','Please give me another chance!'
                                                speak(random.choice(a14))
                                        elif 'do you know' in self.user and 'alexa' in self.user:
                                                speak('of cource I do, she is my best friend')
                                        elif 'do you know' in self.user and 'google assistant' in self.user:
                                                speak('Yes we both are friends')
                                        elif 'can you speak' in self.user and 'hindi' in self.user:
                                                a15='Sorry I cannot','I am afraid I cannot','No;I cannot speak in hindi'
                                                speak(random.choice(a15))
                                        elif 'shut up' in self.user or 'shut' in self.user and 'up' in self.user:
                                                # with open('C:\\ProgramData\\ZeraAI\\condition.txt','w') as f:
                                                #         f.write('sleep')
                                                self.other_4.setValue("condition","sleep")
                                        elif 'how' in self.user and 'you doing' in self.user:
                                                speak('I am fine')
                                        elif 'who' in self.user and 'am I' in self.user:
                                                speak('You are my boss!')
                                        elif 'what' in self.user and 'you doing' in self.user:
                                                speak(f'Always at your service {gender}!')
                                        elif 'laugh' in self.user:
                                                speak('hahahahahhaha')
                                        elif 'when' in self.user and 'is my birthday' in self.user:
                                                speak(f'Your date of birth is {dob}')
                                        elif 'when' in self.user and 'is your birthday' in self.user:#11th june 2021
                                                a16='its 11th of June because mine development was started on that day','its 11th of June'
                                                speak(random.choice(a16))
                                        elif 'what' in self.user and 'your age' in self.user:
                                                a17=f'I am 22; I think my developer is crazy',f'My age is 22 given by my developer'
                                                speak(random.choice(a17))
                                        elif "happy" in self.user:
                                                self.user=self.user.split()
                                                id_01=self.user.index("happy")
                                                prefixes=self.user[:id_01]
                                                if len(prefixes)!=0:
                                                        if "I am" in prefixes:
                                                                a18="Great!", "Glad to hear that your are happy"
                                                                speak(random.choice(a18))
                                                        elif "you" in prefixes:
                                                                speak("Yes I am very happy")
                                                else:
                                                        pass
                                                suffixes=self.user[id_01+1:]
                                                if len(suffixes)!=0:
                                                        print(suffixes)
                                                        # festival=self.user.replace("happy","")
                                                        speak(f"Happy {suffixes} {gender}!")
                                                else:
                                                        pass    
                                        elif "today is my birthday" in self.user:

                                                speak(f"Happy birthday {gender}!")
                                                search_google("Best Birthday Songs")
                                        # tasks
                                        elif 'what is' in self.user and 'time' in self.user or 'time' in self.user:
                                                speak(f"The time is; {datetime.datetime.now().strftime('%I:%M')}")
                                        elif 'what is' in self.user and 'date' in self.user or 'date' in self.user:
                                                speak(f"today's date is {datetime.date.today()}")

                                        elif 'close' in self.user:
                                                # self.user=self.user.replace('close','')
                                                self.user=self.user.split()
                                                id=self.user.index('close')
                                                what_to_close=self.user[id+1:]
                                                self.user=" ".join(what_to_close)
                                                self.user=str(self.user)
                                                speak(f'okay; closing {self.user}')
                                                try:
                                                        os.system(f'taskkill /f /im {self.user}.exe')
                                                except:
                                                        speak('Sorry cannot close the application you wanted to')
                                        elif 'open' in self.user and 'chrome' in self.user or 'open' in self.user and  'google' in self.user:
                                                speak('opening Chrome')
                                                open_Chrome()
                                        elif 'open' in self.user and 'notepad' in self.user or 'open' in self.user and 'text file' in self.user:
                                                speak('opening notepad')
                                                open_notepad()
                                        elif 'open' in self.user and 'command prompt' in self.user or 'open' in self.user and 'cmd' in self.user:
                                                speak('opening command prompt')
                                                open_cmd()
                                        elif 'open youtube' in self.user:
                                                speak('opening youtube')
                                                webbrowser.open('https://www.youtube.com/')
                                        elif 'open wikipedia' in self.user:
                                                speak('opening Wikipedia')
                                                webbrowser.open('https://en.wikipedia.org/wiki/Main_Page')
                                        elif 'open whatsapp' in self.user:
                                                webbrowser.open('https://web.whatsapp.com/')
                                        elif 'open' in self.user:
                                                # self.user=self.user.replace('open','')41
                                                self.user=self.user.split()
                                                id=self.user.index('open')
                                                which_file=self.user[id+1:]
                                                self.user=" ".join(which_file)
                                                self.user=str(self.user)
                                                speak(f'opening {self.user}')
                                                open_other_files(self.user)
                                        elif 'mute' in self.user:
                                                speak('Okay')
                                                pyautogui.press('volumemute')
                                        elif 'unmute' in self.user:
                                                speak('okay')
                                                pyautogui.press('volumeunmute')
                                        elif 'volume up' in self.user or 'voluemeup' in self.user:
                                                speak('Okay')
                                                pyautogui.press('volumeup')
                                        elif 'volume down' in self.user:
                                                speak('Okay')
                                                pyautogui.press('volumedown')
                                        elif 'temperature' in self.user:
                                                temperature(self.user)
                                        # elif 'calculate' in self.user or 'calculation' in self.user:
                                        #         if 'calculate' in self.user:
                                        #                 self.user=self.user.replace('calculate', '')
                                        #         elif 'calculation' in self.user:
                                        #                 self.user=self.user.replace('calculation','')
                                        #         elif 'into' in user:
                                        #                 self.user=self.user.replace('into','x')
                                        #                 calc(self.user)
                                        elif 'how to' in self.user:
                                                try:
                                                        self.user=self.user.replace('search','')
                                                except Exception:
                                                        pass
                                                search_google(self.user)
                                        elif 'shutdown' in self.user and 'in' in self.user or  'shutdown' in self.user and 'after' in self.user  or 'shut down' in self.user and 'in' in self.user or 'shut down' in self.user and 'after' in self.user:
                                                try:
                                                        permission=self.settings.value('power_permission')
                                                        if permission=='true':
                                                                permission=True
                                                        else:
                                                                permission=False
                                                except:
                                                        permission=False
                                                if permission:
                                                        self.user=self.user.split()
                                                        id=''
                                                        try:
                                                                id=self.user.index('in')
                                                        except:
                                                                id=self.user.index('after')
                                                        print("Test 1 passed")
                                                        what_time=self.user[id+1:id+2]
                                                        what_time_2=self.user[id+1:id+2]
                                                        sec_or_min=self.user[id+2:]
                                                        sec_or_min="".join(sec_or_min)
                                                        if 'one' in what_time:
                                                                what_time=1
                                                        else:
                                                                pass
                                                        if str(sec_or_min)=='minutes':
                                                                what_time="".join(what_time)
                                                                what_time=int(str(what_time))*60
                                                                print(what_time)
                                                        else:
                                                                pass
                                                        # what_time="".join(what_time)
                                                        # what_time=str(what_time)
                                                        print("Test 2 passed")
                                                        try:
                                                                speak(f'okay; shutting down this pc in {what_time_2}{sec_or_min}')
                                                                os.system(f'shutdown /s /t {int(what_time)}')
                                                        except Exception:
                                                                speak("Sorry I am unable to shutdown this pc right now")
                                                else:
                                                        speak('Sorry; you first need to allow me to turn your computer on or off in settings')
                                        elif 'restart' in self.user and 'in' in self.user or 'restart' in self.user and 'after' in self.user or 're start' in self.user and 'in' in self.user or 're start' in self.user and 'after' in self.user:
                                                try:
                                                        permission=self.settings.value('power_permission')
                                                        if permission=='true':
                                                                permission=True
                                                        else:
                                                                permission=False
                                                except:
                                                        permission=False                                                        
                                                if permission:
                                                        self.user=self.user.split()
                                                        try:
                                                                id=self.user.index('in')
                                                        except:
                                                                id=self.user.index('after')
                                                        what_time=self.user[id+1:id+2]
                                                        what_time_2=self.user[id+1:id+2]
                                                        sec_or_min=self.user[id+2:]
                                                        sec_or_min="".join(sec_or_min)
                                                        if 'one' in what_time:
                                                                what_time=1
                                                        else:
                                                                pass
                                                        if str(sec_or_min)=='minutes':
                                                                what_time="".join(what_time)
                                                                what_time=int(str(what_time))*60
                                                                print(what_time)
                                                        else:
                                                                pass
                                                        what_time="".join(what_time)
                                                        what_time=str(what_time)
                                                        try:
                                                                speak(f'okay;restarting this pc in {what_time_2}{sec_or_min}')
                                                                os.system(f'shutdown /r /t {int(what_time)}')
                                                        except Exception as e:
                                                                print(e)
                                                                speak("Sorry I am unable to restart this pc right now")
                                                else:
                                                        speak('Sorry; you first need to allow me to turn your computer on or off in settings')
                                        elif 'shutdown' in self.user or 'shut down' in self.user:
                                                try:
                                                        permission=self.settings.value('power_permission')
                                                
                                                        if permission=='true':
                                                                permission=True
                                                        else:
                                                                permission=False
                                                except:
                                                        permission=False
                                                if permission:
                                                        speak('Okay shutting down this pc in a minute.')
                                                        os.system('shutdown /s /t 1')
                                                else:
                                                        speak('Sorry; you first need to allow me to turn your computer on or off in settings')

                                        elif 'restart' in self.user or 're start' in self.user:
                                                try:
                                                        permission=self.settings.value('power_permission')
                                                        if permission=='true':
                                                                permission=True
                                                        else:
                                                                permission=False
                                                except:
                                                        permission=False
                                                if permission:
                                                        speak('Okay restarting this PC.')
                                                        os.system('shutdown /r /t 1')
                                                else:
                                                        speak('Sorry; you first need to allow me to turn your computer on or off in settings')

                                        elif 'create' in self.user and 'text' in self.user:
                                                a8='alright; creating and opening a text file.','okay; creating a text file.'
                                                speak(random.choice(a8))
                                                open_notepad()
                                                a9='should I turn on the speech to text mode for you?','Should I type for you?'
                                                speak(random.choice(a9))
                                                def start_tts():
                                                        speak('Okay; Switching on speech to text mode; Now I will type whatever you speak;Make sure to click once in the empty space before starting, once done say DEACTIVATE;;;;;started.')
                                                        while True:
                                                                # global words_to_text
                                                                self.typewriter=command3()
                                                                pyautogui.typewrite(f"{self.typewriter} ")
                                                                if 'deactivate' in words_to_text or 'de activate' in words_to_text:
                                                                        speak('Deactivating speech to text mode')
                                                                        break
                                                                elif 'backspace' in words_to_text:
                                                                        pyautogui.press('backspace')
                                                                elif 'enter' in words_to_text or 'next line' in words_to_text:
                                                                        pyautogui.press('enter')
                                                                if 'full stop' in words_to_text:
                                                                        pyautogui.typewrite('.')
                                                while True:
                                                        self.yesorno=command2()
                                                        if 'yes' in self.yesorno or 'ok' in self.yesorno or 'yup' in self.yesorno or 'alright' in self.yesorno or 'why not' in self.yesorno or 'fine' in self.yesorno or 'done' in self.yesorno or 'of course' in self.yesorno:
                                                                start_tts()
                                                                break
                                                        elif 'no' in self.yesorno or 'nope' in self.yesorno or 'nah' in self.yesorno or 'neh' in self.yesorno or 'no need' in self.yesorno or 'nep' in self.yesorno or 'let it be' in self.yesorno or 'nahi' in self.yesorno or 'no way' in self.yesorno:
                                                                a10='okay','alright'
                                                                speak(random.choice(a10))
                                                                break
                                                        else:
                                                                speak('say it again please')

                                                                
                                                        
                                        # sleeping
                                        elif 'sleep' in self.user:
                                                # global sleep
                                                # # speak('alright; going to sleep')
                                                # sleep=True
                                                # with open('C:\\PRogramData\\ZeraAI\\condition.txt','w') as f:
                                                #         f.write('sleep')
                                                self.other_4.setValue("condition","sleep")
                                                main_switch=False
                                        # leaving statements
                                        elif 'bye' in self.user:
                                                exit_switch
                                                speak(f'Bye {gender}; have a nice day')
                                                # with open('C:\\ProgramData\\ZeraAI\\condition.txt','w') as f:
                                                #         f.write('')
                                                self.other_4.setValue("condition","")
                                                switch=False
                                                switch_activator=False
                                                # import sys
                                                # if exit_switch:
                                                Zera.close()
                                                sys.exit()
                                        # exception-2
                                        elif 'what is' in self.user or 'calculate' in self.user:
                                                if 'into' in self.user:
                                                        self.user=self.user.replace('into',' * ')
                                                elif 'x' in self.user:
                                                        self.user=self.user.replace('x','*')
                                                if 'calculate' in self.user:
                                                        self.user=self.user.replace('calculate','')
                                                elif 'what is' in self.user:
                                                        self.user=self.user.replace('what','')
                                                        self.user=self.user.replace('is','')
                                                elif 'calculate' in self.user and 'what is' in self.user:
                                                        self.user=self.user.replace('calculate','')
                                                        self.user=self.user.replace('what','')
                                                        self.user=self.user.replace('is','')
                                                try:
                                                        calc(self.user)
                                                except Exception:
                                                        speak("sorry couldn't find out")
                                        elif 'who is' in self.user or 'who' in self.user:
                                                self.user=self.user.replace('who','')
                                                try:
                                                        self.user=self.user.replace('is','')
                                                except Exception:
                                                        pass
                                                # speak(f'searching {self.user} on google')
                                                try:
                                                        answer=wikipedia.summary(self.user,sentences=2)
                                                        bg_listener=Temp_background_listener()
                                                        try:
                                                                bg_listener.start()
                                                        except:
                                                                pass
                                                        speak(f'according to wikipedia {answer}')
                                                        # print('came here')
                                                        self.other_4.setValue("condition","sleep")
                                                        
                                                except Exception:
                                                        # answer=search_google(self.user)
                                                        speak(f'searching {self.user} on google')
                                                        search_google(self.user)

                                                # print(answer) 
                                        elif 'type' in self.user:
                                                self.user=self.user.split()
                                                id=self.user.index('type')
                                                what_to_type=self.user[id+1:]
                                                if len(what_to_type)!=0:
                                                        self.user=" ".join(what_to_type)
                                                        self.user=str(self.user)
                                                        speak('Okay')
                                                        pyautogui.typewrite(self.user)
                                                elif len(what_to_type)==0:
                                                        speak('Okay switching on speech to text mode say stop to stop typing')
                                                        while True:
                                                                stt=command2()
                                                                if 'full stop' in stt:
                                                                        pyautogui.typewrite('.')
                                                                elif 'stop' in stt:
                                                                        break
                                                                elif 'backspace' in stt:
                                                                        pyautogui.press('backspace')
                                                                elif 'enter' in stt or 'next line' in stt:
                                                                        pyautogui.press('enter')
                                                                else:
                                                                        try:
                                                                                pyautogui.typewrite(f"{stt} ")
                                                                        except:
                                                                                speak("sorry couldn't write right now")
                                                                
                                        else:
                                                # print(len(self.user))
                                                if len(self.user)!=4:
                                                        f_variation="Sorry; I didn't understand!","Pardon; I couldn't understand",f'Sorry; no information'
                                                        speak(random.choice(f_variation))
                                                else:
                                                        continue
execution=MainThread()
execution_2=Activator_thread()


class Main(QMainWindow):
        def __init__(self):
                global switch,name,locked
                global AI_State

                self.other_5=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Other")
                self.settings=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Settings")
                # AI_State='Sleeping...'
                AI_State=name
                # with open('C:\\ProgramData\\ZeraAI\\condition.txt','r') as f:
                #         d=f.read().strip()
                d=self.other_5.value('condition')
                if d=='wakeup':
                        # with open('C:\ProgramData\\ZeraAI\\condition.txt','w') as f:
                        #         f.write('')
                        self.other_5.setValue("condition","")
                        
                super().__init__()
                self.ui=Ui_MainWindow()
                self.ui.setupUi(self)
                self.setWindowFlags(QtCore.Qt.Widget | QtCore.Qt.FramelessWindowHint)

                self.setWindowFlag(QtCore.Qt.Tool)
                # self.center()

                # main functions
                # self.ui.movie=QtGui.QMovie(":/bgImage/main circle.gif")
                self.ui.Ai_state.setText(name.strip())
                execution.start()
                execution_2.start()
                self.center_win()

                # deactivating hover effects
                self.opacity_effect_settings=QGraphicsOpacityEffect()
                self.opacity_effect_settings.setOpacity(0)
                self.opacity_effect_lock=QGraphicsOpacityEffect()
                self.opacity_effect_lock.setOpacity(0)
                self.opacity_effect_exit=QGraphicsOpacityEffect()
                self.opacity_effect_exit.setOpacity(0)
                self.opacity_effect_custom_commands=QGraphicsOpacityEffect()
                self.opacity_effect_custom_commands.setOpacity(0)
                self.opacity_effect_ai_info=QGraphicsOpacityEffect()
                self.opacity_effect_ai_info.setOpacity(0)
                self.opacity_effect_programs=QGraphicsOpacityEffect()
                self.opacity_effect_programs.setOpacity(0)
                self.opacity_effect_info=QGraphicsOpacityEffect()
                self.opacity_effect_info.setOpacity(0)
                self.ui.settings_hovered_label.setGraphicsEffect(self.opacity_effect_settings)
                self.ui.lock_hovered_button.setGraphicsEffect(self.opacity_effect_lock)
                self.ui.exit_hovered_button.setGraphicsEffect(self.opacity_effect_exit)
                self.ui.label.setGraphicsEffect(self.opacity_effect_custom_commands)
                self.ui.label_2.setGraphicsEffect(self.opacity_effect_programs)
                self.ui.label_3.setGraphicsEffect(self.opacity_effect_ai_info)
                self.ui.label_4.setGraphicsEffect(self.opacity_effect_info)

                
                # activating hover effect
                self.ui.settings_button.entered.connect(self.settings_hovered)
                self.ui.settings_button.leaved.connect(self.settings_hovered_false)
                
                self.ui.lock_button.entered.connect(self.lock_hovered)
                self.ui.lock_button.leaved.connect(self.lock_hovered_false)

                self.ui.exit_button.entered.connect(self.exit_hovered)
                self.ui.exit_button.leaved.connect(self.exit_hovered_false)
                
                self.ui.custom_command_button.entered.connect(self.custom_commands_hovered)
                self.ui.custom_command_button.leaved.connect(self.custom_commands_hovered_false)

                self.ui.personal_info_button.entered.connect(self.personal_info_hovered)
                self.ui.personal_info_button.leaved.connect(self.personal_info_hovered_false)

                self.ui.Ai_info_button.entered.connect(self.ai_info_hovered)
                self.ui.Ai_info_button.leaved.connect(self.ai_info_hovered_false)
                
                self.ui.programs_button.entered.connect(self.programs_hovered)
                self.ui.programs_button.leaved.connect(self.programs_hovered_false)

                locked_at_launch=self.settings.value('locked_at_launch')

                if locked_at_launch=='false':
                        locked=False
                else:
                        locked=True
                if locked:
                        self.opacity_effect_lock.setOpacity(1)
                        self.ui.lock_hovered_button.setGraphicsEffect(self.opacity_effect_lock)

                # joining buttons
                # self.ui.Wakeup_button.clicked.connect(self.run_task)
                # self.ui.cross.clicked.connect(self.closing)
                # self.ui.exit_button.clicked.connect(self.closing)
                # self.ui.Sleep_button.clicked.connect(self.send_to_sleep)
                # self.ui.minimize_button.clicked.connect(self.minimize)
                # self.ui.settingsButton.clicked.connect(self.send_to_general)

                from settings_implementation import settings_window
                self.settings_win=settings_window()

                self.ui.exit_button.clicked.connect(self.closing)
                self.ui.exit_button.setFocusPolicy(Qt.NoFocus)

                self.ui.switch_button.clicked.connect(self.run_task)
                self.ui.switch_button.setFocusPolicy(Qt.NoFocus)

                self.ui.settings_button.clicked.connect(self.send_to_settings)
                self.ui.settings_button.setFocusPolicy(Qt.NoFocus)

                self.ui.lock_button.clicked.connect(self.change_lock_state)
                self.ui.lock_button.setFocusPolicy(Qt.NoFocus)

                self.ui.Ai_info_button.clicked.connect(lambda:self.open_respective_page(self.settings_win.ui.page_3))
                self.ui.Ai_info_button.setFocusPolicy(Qt.NoFocus)

                self.ui.personal_info_button.clicked.connect(lambda:self.open_respective_page(self.settings_win.ui.page_2))
                self.ui.personal_info_button.setFocusPolicy(Qt.NoFocus)

                self.ui.programs_button.clicked.connect(self.send_to_programs)
                self.ui.programs_button.setFocusPolicy(Qt.NoFocus)

                self.ui.custom_command_button.clicked.connect(self.send_to_custom_commands)
                self.ui.custom_command_button.setFocusPolicy(Qt.NoFocus)
                
                #labels
                # timer = QTimer(self)
                # timer.timeout.connect(self.showTimeandDate)
                # timer.start(1000) # update every second
                # self.showTimeandDate()

                timer_2 = QTimer(self)
                timer_2.timeout.connect(self.update_state)
                timer_2.timeout.connect(self.exit_checker)
                timer_2.timeout.connect(self.update_history)
                timer_2.start(1000) # update every second

                # timer_3 = QTimer(self)
                # timer_3.timeout.connect(self.tips_update)
                # timer_3.start(10000) # update after every 10 seconds
                
                user_info=QSettings("Yash Akarsh\\ZERA-The Advanced AI","user_info")
                user_name=user_info.value("name")
                username_separated=user_name.replace(" ",",")
                username_splitted=username_separated.split(",")

                # if len(username_splitted[0])>10:
                #         self.ui.Username_text.setStyleSheet('''border-image:none;\nfont: 15pt \"Azonix\";''')
                # else:
                #         self.ui.Username_text.setStyleSheet('''border-image:none;\nfont: 20pt \"Azonix\";''')

                # # username="".join(username[0])
                # self.ui.Username_text.setText(username_splitted[0])

                # getting temperature
                # try:
                #         resp=api.query('temperature')
                #         temp=(next(resp.results).text).split()
                #         self.ui.Temp_text.setText(str(" ".join(temp[0:2])))
                # except:
                #         self.ui.Temp_text.setText('Error')
                # internet connectivity
                # import requests
                # import pyttsx3

                # internet=True
                # url = "http://www.kite.com"
                # timeout = 5
                # try:
                #         request = requests.get(url, timeout=timeout)
                #         # print("Connected to the Internet")
                #         self.ui.internet_text.setText('Connected')
                #         self.ui.internet_text.setStyleSheet("border-image:none;\nfont: 19pt \"Azonix\";")
                #         self.ui.internet_text.setGeometry(QtCore.QRect(70, 580, 221, 41))
                # except (requests.ConnectionError, requests.Timeout) as Exception:
                #         internet=False
                #         self.ui.internet_text.setText('Disconnected')
        
        def change_lock_state(self):
                global locked
                if locked==False:
                        locked=True
                else:
                        locked=False
        
        def send_to_custom_commands(self):
                from custom_commands_implementation import custom_commands_window
                self.custom_win=custom_commands_window()
                self.custom_win.show()

        def send_to_programs(self):
                from file_location_implementation import file_location_window
                self.file_location_win=file_location_window()
                self.file_location_win.show()
                # file_location_win.setAttribute(QtCore.Qt.WA_QuitOnClose)

        def settings_hovered(self):
                self.opacity_effect_settings.setOpacity(1.0)
                self.ui.settings_hovered_label.setGraphicsEffect(self.opacity_effect_settings)
        
        def settings_hovered_false(self):
                self.opacity_effect_settings.setOpacity(0)
                self.ui.settings_hovered_label.setGraphicsEffect(self.opacity_effect_settings)
        
        def lock_hovered(self):
                self.opacity_effect_lock.setOpacity(1.0)
                self.ui.lock_hovered_button.setGraphicsEffect(self.opacity_effect_lock)
        
        def lock_hovered_false(self):
                if not locked:
                        self.opacity_effect_lock.setOpacity(0)
                        self.ui.lock_hovered_button.setGraphicsEffect(self.opacity_effect_lock)
        
        def exit_hovered(self):
                self.opacity_effect_exit.setOpacity(1.0)
                self.ui.exit_hovered_button.setGraphicsEffect(self.opacity_effect_exit)
        
        def exit_hovered_false(self):
                self.opacity_effect_exit.setOpacity(0)
                self.ui.exit_hovered_button.setGraphicsEffect(self.opacity_effect_exit)
        
        def custom_commands_hovered(self):
                self.opacity_effect_custom_commands.setOpacity(1.0)
                self.ui.label.setGraphicsEffect(self.opacity_effect_custom_commands)
        
        def custom_commands_hovered_false(self):
                self.opacity_effect_custom_commands.setOpacity(0)
                self.ui.label.setGraphicsEffect(self.opacity_effect_custom_commands)
        
        def ai_info_hovered(self):
                self.opacity_effect_ai_info.setOpacity(1.0)
                self.ui.label_3.setGraphicsEffect(self.opacity_effect_ai_info)
        
        def ai_info_hovered_false(self):
                self.opacity_effect_ai_info.setOpacity(0)
                self.ui.label_3.setGraphicsEffect(self.opacity_effect_ai_info)
        
        def personal_info_hovered(self):
                self.opacity_effect_info.setOpacity(1.0)
                self.ui.label_4.setGraphicsEffect(self.opacity_effect_info)

        def personal_info_hovered_false(self):
                self.opacity_effect_info.setOpacity(0)
                self.ui.label_4.setGraphicsEffect(self.opacity_effect_info)
        
        def programs_hovered(self):
                self.opacity_effect_programs.setOpacity(1.0)
                self.ui.label_2.setGraphicsEffect(self.opacity_effect_programs)
        
        def programs_hovered_false(self):
                self.opacity_effect_programs.setOpacity(0)
                self.ui.label_2.setGraphicsEffect(self.opacity_effect_programs)
        def send_to_settings(self):
                # from settings_general_implementation import general_window
                from settings_implementation import settings_window
                # self.app=QApplication(sys.argv)
                self.settings_1=settings_window()
                self.settings_1.show()
        
        def open_respective_page(self,page):
                self.settings_win.show()
                self.settings_win.ui.stackedWidget.setCurrentWidget(page)
        

        def send_to_sleep(self):
                # os.startfile('activation.py')
                # with open('C:\\ProgramData\\ZeraAI\\condition.txt','w') as f:
                #         f.write('sleep')
                self.other_5.setValue("condition","sleep")

        def send_to_reset(self):
                global main_active
                from Loading_implementation import Loading_window
                main_active=False
                self.load_win=Loading_window()
                self.load_win.show()
                # sys.exit()
                self.close()
        def showTimeandDate(self):
                global switch_activator
                currentTime = QTime.currentTime()
                currentDate=QDate.currentDate()
                LabelTime=currentTime.toString('hh:mm:ss')
                LabelDate=currentDate.toString(Qt.ISODate)
                # self.ui.Time_text.setText(LabelTime)
                # self.ui.date_text.setText(LabelDate)
                # with open('C:\\ProgramData\\ZeraAI\\condition.txt') as f:
                #         data=f.read().strip()
                data=self.other_5.value("condition")
                if data=='reset':
                        # with open('C:\\ProgramData\\ZeraAI\\condition.txt','w') as f:
                        #         f.write('')
                        self.other_5.setValue("condition","")
                        self.other_5.setValue("user_occurence","new_2")
                        settings_01=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Settings")
                        settings_01.setValue("wake_greeting",None)
                        switch_activator=False
                        self.send_to_reset()
                        self.close()
                        # sys.exit()
        def mousePressEvent(self, event):
                if event.button()==Qt.LeftButton:
                        self.m_flag=True
                        self.m_Position=event.globalPos()-self.pos() #Get the position of the mouse relative to the window
                        event.accept()
                        # self.setCursor(QCursor(Qt.OpenHandCursor))  #Change mouse icon

        def mouseMoveEvent(self, QMouseEvent):
                if not locked:
                        try:
                                if Qt.LeftButton and self.m_flag:  
                                        self.move(QMouseEvent.globalPos()-self.m_Position)#Change window position
                                        QMouseEvent.accept()
                        except:
                                pass
            
        def mouseReleaseEvent(self, QMouseEvent):
                self.m_flag=False
                self.setCursor(QCursor(Qt.ArrowCursor))
        def run_task(self):
                global switch,AI_State,message,main_switch
                if main_switch==False:
                        # self.ui.Ai_state.setText("active")
                        print('test 3 complete')
                        # with open('C:\\ProgramData\\ZeraAI\\condition.txt','w') as f:
                        #         f.write('wakeup')
                        print("Test 0 passed")
                        self.other_5.setValue("condition","wakeup")
                        AI_State='Listening...'
                        try:
                                execution.start()
                        except:
                                print("not able to")
                        message='hello'
                        main_switch=True
                else:
                        self.send_to_sleep()
                        main_switch=False
        def minimize(self):
                self.showMinimized()

        def closing(self):
                global exit_switch,switch_activator,application_close_switch
                exit_switch=True
                # with open("C:\\ProgramData\\ZeraAI\\Settings.txt",'r') as f:
                #         d_1=f.readline().strip()
                #         d_1=f.readline().strip()
                #         ex_read=f.readline().strip()
                d_1=self.settings.value("wake_greeting")
                d_2=self.settings.value("goodbye_greeting")
                ex_read=self.settings.value("exit_dialog_box")
                if ex_read=="true":
                        ex_read=True
                else:
                        ex_read=False
                if ex_read:
                        from exit_confirmer_implementation import exit_window
                        self.exit_window=exit_window()
                        self.exit_window.show()
                if not ex_read:
                        # with open("C:\\ProgramData\\ZeraAI\\condition.txt",'w') as f:
                        #                 f.write('')
                        self.other_5.setValue("condition","")

                        
                        switch=False
                        # with open('C:\\ProgramData\\ZeraAI\\condition.txt','w') as f:
                        #         f.write('')
                        self.other_5.setValue("condition","")
                        # with open('C:\\ProgramData\\ZeraAI\\Settings.txt','r') as f:
                        #         W_greetings=f.readline().strip()
                        #         S_greetings=f.readline().strip()
                        W_greetings=self.settings.value("wake_greeting")
                        S_greetings=self.settings.value("goodbye_greeting")
                        if S_greetings=='true':
                                try:
                                        speak(f'Goodbye {gender}!')
                                except:
                                        pass
                        switch_activator=False
                        # with open('C:\\ProgramData\\ZeraAI\\Settings.txt','r') as f:
                        #         data=f.read().strip()
                                # print(data)
                        # with open('C:\\ProgramData\\ZeraAI\\Settings.txt','r') as f:
                        #         data_1=f.readline().strip()
                        #         # data_2=f.readline().strip()
                        #         # data_3=f.readline().strip()
                        data_1=self.settings.value("wake_greeting")
                        data_2=self.settings.value("goodbye_greeting")
                        data_3=self.settings.value("exit_dialog_box")
                        if data_1=='True ~~':
                                data_1=True
                        self.settings.setValue("wake_greeting",data_1)
                        # with open(f"C:\\ProgramData\\ZeraAI\\Settings.txt",'w') as f:
                        #         f.write(f"{data_1}\n{data_2}\n{data_3}")
                        all_values_1=self.settings.value("wake_greeting")
                        all_values_2=self.settings.value("goodbye_greeting")
                        all_values_3=self.settings.value("exit_dialog_box")
                        if all_values_1=="true" or all_values_1=="True ~~":
                                all_values_1=True
                        elif all_values_1=="false":
                                all_values_1=False
                        if all_values_2=="true":
                                all_values_2=True
                        else:
                                all_values_2=False
                        if all_values_3=="true":
                                all_values_3=True
                        else:
                                all_values_3=False
                        # if all_values_1 and all_values_2 and all_values_3:

                        if data_1=='true' and data_2 =='true':
                                # g.write('wakeup_greetings\ngoodbye_greetings')
                                self.settings.setValue("wake_greeting",True)
                                self.settings.setValue("goodbye_greeting",True)
                        elif data_1=='false' and data_2=='true':
                                # g.write('\ngoodbye_greetings')
                                self.settings.setValue("goodbye_greeting",True)
                        elif data_1=='True ~~' and data_2=='true':
                                # g.write('wakeup_greetings\ngoodbye_greetings')
                                self.settings.setValue("wake_greeting",True)
                                self.settings.setValue("goodbye_greeting",True)
                        elif data_1=='True ~~' and data_2=='false':
                                # g.write('wakeup_greetings')
                                self.settings.setValue("wake_greeting",True)
                        elif data_1=='true' and data_2=="false":
                                # g.write('wakeup_greetings')
                                self.settings.setValue("wake_greeting",True)
                        
                        # closing all the other windows
                        from settings_implementation import settings_window
                        self.settings_1=settings_window()
                        self.settings_1.closing()
                        self.settings.setValue('history','')
                        application_close_switch=True
                        # app.quit()
                        sys.exit()
                        # self.close()
                        from Loading_implementation import Loading_window
                        self.loading_win=Loading_window()
                        self.loading_win.close()
        def closeEvent(self, event):
                global application_close_switch
                if application_close_switch:
                        from settings_implementation import settings_window
                        self.settings_1=settings_window()
                        self.settings_1.closing()
                        try:
                                # app.quit()
                                sys.exit()
                        except:
                                pass
                        event.accept()    
        def center_win(self):
            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
        def update_history(self):
                global textbox 
                # self.ui.textEdit.setReadOnly(True)
                previous=self.settings.value('history')
                if textbox=='':
                        pass
                else:
                        if previous!='':
                                # self.ui.textEdit.setText(f"{previous}\n{textbox}")
                                self.settings.setValue('history',f'{previous},{textbox}')
                        elif previous=='':
                                self.settings.setValue('history',f'{textbox}')

                textbox=''
        def update_state(self):
                global AI_State,sleep_countdown,listen_switch,bar_activator
                if sleep_countdown>=20:
                        # with open('C:\\ProgramData\\ZeraAI\\condition.txt','w') as f:
                        #                 f.write('sleep')
                        self.other_5.setValue("condition","sleep")

                elif sleep_countdown==0:
                        listen_switch=True
                # if bar_activator:
                #         self.ui.bar.setMovie(self.ui.movie)
                #         self.ui.movie.start()
                # elif bar_activator==False:
                #         self.ui.movie.stop()
                self.ui.Ai_state.setText(AI_State)
                if AI_State=='Listening...':
                        self.ui.Ai_state.setStyleSheet("font: 11pt \"Orbitron\";\n""color: rgb(0, 255, 182);")
                elif AI_State=='Speaking...':
                        self.ui.Ai_state.setStyleSheet("font: 11pt \"Orbitron\";\n""color: rgb(0, 255, 182);")
                else:
                        if name=='Zera':
                                self.ui.Ai_state.setStyleSheet("font: 20pt \"Perfect Dark (BRK)\";\n""color: rgb(0, 255, 182);")
                        else:
                                self.ui.Ai_state.setStyleSheet("font: 15pt \"Perfect Dark (BRK)\";\n""color: rgb(0, 255, 182);")
                user_info=QSettings("Yash Akarsh\\ZERA-The Advanced AI","user_info")
                try:
                        username2=user_info.value("name")
                        username_separated2=username2.replace(" ",",")
                        username_splitted2=username_separated2.split(",")
                        if len(username_splitted2[0])>10:
                                self.ui.Username_text.setStyleSheet('''border-image:none;\nfont: 15pt \"Azonix\";''')
                        else:
                                self.ui.Username_text.setStyleSheet('''border-image:none;\nfont: 20pt \"Azonix\";''')
                        self.ui.Username_text.setText(username_splitted2[0])
                        
                except:
                        pass
                current_volume=self.settings.value('volume')
                try:
                        engine.setProperty('volume',float(current_volume))
                except:
                        engine.setProperty('volume',1)
                current_voice_speed=self.settings.value('voice_speed')
                try:
                        engine.setProperty('rate',int(current_voice_speed))
                except:
                        engine.setProperty('rate',170)
                # history=",".join(history_list)
                # self.settings.setValue('history',history)
        def exit_checker(self):
                global exit_Switch,application_close_switch
                exit_switch=True
                # with open("C:\\ProgramData\\ZeraAI\\condition.txt",'r') as f:
                #         ex_or_not=f.read().strip()
                ex_or_not=self.other_5.value("condition")

                # with open("C:\\ProgramData\\ZeraAI\\Settings.txt",'r') as f:
                #         data_1=f.readline().strip()
                #         data_2=f.readline().strip()
                #         exit_box_read=f.readline().strip()

                data_1=self.settings.value("wake_greeting")
                data_2=self.settings.value('goodbye_greeting')
                exit_box_read=self.settings.value('exit_dialog_box')
                if exit_box_read=='true':
                        if ex_or_not=='exit':
                                print("EXIT")
                                # with open("C:\\ProgramData\\ZeraAI\\condition.txt",'w') as f:
                                #         f.write('')
                                self.other_5.setValue("condition","")

                                global switch_activator
                                switch=False
                                # with open('C:\\ProgramData\\ZeraAI\\condition.txt','w') as f:
                                #         f.write('')
                                self.other_5.setValue("condition","")

                                # with open('C:\\ProgramData\\ZeraAI\\Settings.txt','r') as f:
                                #         W_greetings=f.readline().strip()
                                #         S_greetings=f.readline().strip()
                                W_greetings=self.settings.value("wake_greeting").strip()
                                S_greetings=self.settings.value("goodbye_greeting").strip()
                                if S_greetings=='true':
                                        try:
                                                speak(f'Goodbye {gender}!')
                                        except:
                                                pass
                                switch_activator=False
                                # with open('C:\\ProgramData\\ZeraAI\\Settings.txt','r') as f:
                                #         data=f.read().strip()
                                        # print(data)
                                # with open('C:\\ProgramData\\ZeraAI\\Settings.txt','r') as f:
                                #         data_1=f.readline().strip()
                                #         data_2=f.readline().strip()
                                #         data_3=f.readline().strip()
                                data_1=self.settings.value("wake_greeting").strip()
                                if data_1=='True ~~':
                                        data_1=True
                                # with open(f"C:\\ProgramData\\ZeraAI\\Settings.txt",'w') as f:
                                #         f.write(f"{data_1}\n{data_2}\n{data_3}")
                                self.settings.setValue("wake_greeting",data_1)
                                all_values_1=self.settings.value("wake_greeting").strip()
                                all_values_2=self.settings.value("goodbye_greeting").strip()
                                all_values_3=self.settings.value("exit_dialog_box").strip()
                                if all_values_1=="true" or all_values_1=="true ~~":
                                        all_values_1=True
                                elif all_values_1=="false":
                                        all_values_1=False
                                if all_values_2=="true":
                                        all_values_2=True
                                else:
                                        all_values_2=False
                                if all_values_3=="true":
                                        all_values_3=True
                                else:
                                        all_values_3=False
                                # if all_values_1 and all_values_2 and all_values_3:
                                if data_1=='true' and data_2 =='true':
                                        # g.write('wakeup_greetings\ngoodbye_greetings')
                                        self.settings.setValue("wake_greeting",True)
                                        self.settings.setValue("goodbye_greeting",True)
                                elif data_1=='false' and data_2=='true':
                                        # g.write('\ngoodbye_greetings')
                                        self.settings.setValue("goodbye_greeting",True)
                                elif data_1=='True ~~' and data_2=='true':
                                        # g.write('wakeup_greetings\ngoodbye_greetings')
                                        self.settings.setValue("wake_greeting",True)
                                        self.settings.setValue("goodbye_greeting",True)
                                elif data_1=='True ~~' and data_2=='false':
                                        # g.write('wakeup_greetings')
                                        self.settings.setValue("wake_greeting",True)
                                elif data_1=='true' and data_2=="false":
                                        # g.write('wakeup_greetings')
                                        self.settings.setValue("wake_greeting",True)
                                # self.close()
                                self.settings.setValue('history','')
                                application_close_switch=True
                                sys.exit()
                                # app.quit()
        # def tips_update(self):
        #         initials='Try saying'
        #         messages=[f'{initials} "Open wikipedia"',f'{initials} "Open Chrome"',f'{initials} "Play songs on YouTube"',f'{initials} "type Good Morning"',f'{initials} "What is 27 + 34"',f'{initials} "What is the Temperature"',f''''{initials} "What is today's date"''',f'{initials} "tell me the time"',f'{initials} "Who is Sachin Tendulkar"',f'{initials} "search how to cook"',f'{initials} "shutdown this pc"',f'{initials} "restart this pc in 5 minutes"']
        #         self.ui.tips.setText(random.choice(messages))

if __name__=="__main__":
        if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
                QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
        if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
                QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
        settings=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Settings")
        other_6=QSettings("Yash Akarsh\\ZERA-The Advanced AI","Other")

        check_value=settings.value("waking_hotkey")
        if check_value==None:
                print("recreating")
                settings.setValue("exit_dialog_box",False)
                # settings.setValue("wake_greeting",True)
                settings.setValue("goodbye_greeting",True)
                settings.setValue("waking_hotkey","tab")
                settings.setValue("sleeping_hotkey","home")
                
                other_6.setValue("user_occurence",'new_2')
        # QApplication.setAttribute(Qt.AA_DisableHighDpiScaling)
        app=QApplication(sys.argv)
        # Handle high resolution displays:
        Zera=Main()
        Zera.show()
        Zera.setAttribute(QtCore.Qt.WA_QuitOnClose)
        speak('')
        # time.sleep(1)
        # with open('C:\\ProgramData\\ZeraAI\\user_occurence.txt','r') as f:
        d=other_6.value("user_occurence")
        if d=='new_2':
                Zera.run_task()

        # with open('C:\\ProgramData\\ZeraAI\\Settings.txt','r') as f:
        #         W_greetings=f.readline().strip()

        W_greetings=settings.value("wake_greeting")
        if W_greetings=='true':
                W_greetings=True
        elif W_greetings=="True ~~":
                print('Some problem here')
        else:
                W_greetings=False
        if W_greetings:
                greet_switch=True
                Zera.run_task()
        
        sys.exit(app.exec_())        