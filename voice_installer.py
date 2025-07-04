def install_voices():
  import os
  if os.path.exists('C:\\ProgramData\\ZeraAI\\voices\\zera_voice.reg'):
    pass
  else:
    with open('C:\\ProgramData\\ZeraAI\\voices\\zera_voice.reg','w') as f:
        f.write('''Windows Registry Editor Version 5.00

    [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens]

    [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_Cortana]
    @="Cortana"
    "409"="Cortana - English (United States)"
    "CLSID"="{179F3D56-1B0B-42B2-A962-59B7EF59FE1B}"
    "LangDataPath"=hex(2):25,00,77,00,69,00,6e,00,64,00,69,00,72,00,25,00,5c,00,53,\
      00,70,00,65,00,65,00,63,00,68,00,5f,00,4f,00,6e,00,65,00,43,00,6f,00,72,00,\
      65,00,5c,00,45,00,6e,00,67,00,69,00,6e,00,65,00,73,00,5c,00,54,00,54,00,53,\
      00,5c,00,65,00,6e,00,2d,00,55,00,53,00,5c,00,4d,00,53,00,54,00,54,00,53,00,\
      4c,00,6f,00,63,00,65,00,6e,00,55,00,53,00,2e,00,64,00,61,00,74,00,00,00
    "VoicePath"=hex(2):25,00,77,00,69,00,6e,00,64,00,69,00,72,00,25,00,5c,00,53,00,\
      70,00,65,00,65,00,63,00,68,00,5f,00,4f,00,6e,00,65,00,43,00,6f,00,72,00,65,\
      00,5c,00,45,00,6e,00,67,00,69,00,6e,00,65,00,73,00,5c,00,54,00,54,00,53,00,\
      5c,00,65,00,6e,00,2d,00,55,00,53,00,5c,00,4d,00,31,00,30,00,33,00,33,00,45,\
      00,76,00,61,00,00,00

    [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_Cortana\Attributes]
    "Age"="Adult"
    "DataVersion"="11.0.2013.1022"
    "Gender"="Female"
    "Language"="409"
    "Name"="Cortana"
    "SharedPronunciation"=""
    "Vendor"="Microsoft"
    "Version"="11.0"

    ''')
  if os.path.exists("C:\\ProgramData\\ZeraAI\\voices\\jarvis_voice.reg"):
    pass
  else:

    with open("C:\\ProgramData\\ZeraAI\\voices\\jarvis_voice.reg",'w') as f:
      f.write('''Windows Registry Editor Version 5.00

  [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_MarkM]
  @="Microsoft Mark - English (United States)"
  "409"="Microsoft Mark - English (United States)"
  "CLSID"="{179F3D56-1B0B-42B2-A962-59B7EF59FE1B}"
  "LangDataPath"=hex(2):25,00,77,00,69,00,6e,00,64,00,69,00,72,00,25,00,5c,00,53,\
    00,70,00,65,00,65,00,63,00,68,00,5f,00,4f,00,6e,00,65,00,43,00,6f,00,72,00,\
    65,00,5c,00,45,00,6e,00,67,00,69,00,6e,00,65,00,73,00,5c,00,54,00,54,00,53,\
    00,5c,00,65,00,6e,00,2d,00,55,00,53,00,5c,00,4d,00,53,00,54,00,54,00,53,00,\
    4c,00,6f,00,63,00,65,00,6e,00,55,00,53,00,2e,00,64,00,61,00,74,00,00,00
  "VoicePath"=hex(2):25,00,77,00,69,00,6e,00,64,00,69,00,72,00,25,00,5c,00,53,00,\
    70,00,65,00,65,00,63,00,68,00,5f,00,4f,00,6e,00,65,00,43,00,6f,00,72,00,65,\
    00,5c,00,45,00,6e,00,67,00,69,00,6e,00,65,00,73,00,5c,00,54,00,54,00,53,00,\
    5c,00,65,00,6e,00,2d,00,55,00,53,00,5c,00,4d,00,31,00,30,00,33,00,33,00,4d,\
    00,61,00,72,00,6b,00,00,00

  [HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_MarkM\Attributes]
  "Age"="Adult"
  "DataVersion"="11.0.2013.1022"
  "Gender"="Male"
  "Language"="409"
  "Name"="Microsoft Mark"
  "SayAsSupport"="spell=NativeSupported; cardinal=GlobalSupported; ordinal=NativeSupported; date=GlobalSupported; time=GlobalSupported; telephone=NativeSupported; currency=NativeSupported; net=NativeSupported; url=NativeSupported; address=NativeSupported; alphanumeric=NativeSupported; Name=NativeSupported; media=NativeSupported; message=NativeSupported; companyName=NativeSupported; computer=NativeSupported; math=NativeSupported; duration=NativeSupported"
  "SharedPronunciation"=""
  "Vendor"="Microsoft"
  "Version"="11.0"
  
  ''')

if __name__=="__main__":
  install_voices()