from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib

def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')
#listen for commands

def myCommand():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('I am ready for your next command')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print('You said'+ command + '/n')
        
    #loop back to continue to listen for commands
    except sr.UnknownValueError:
        assistant(myCommand())

    return command

#if statements for executing commands
def assistant(command):

    if 'open youtube' in command:
        chrome_path = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        url = "https://www.youtube.com"
        webbrowser.get(chrome_path).open(url)
talkToMe("I am ready for your next command")

while True:
    assistant(myCommand())
