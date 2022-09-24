from tkinter import*
import speed_recognition as sr
import webbrowser
import pyttsx3
from datetime import datwtime
import subprocess

root =Tk()
root.geometry("500x500")
root.configure(bg="Light Blue")

label=Label(root,text="Welcome To Your Personal Desktop Assistant",
label.place(relx=0.5,rely=0.1,anchor=CENTER)

text_to_speech=pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
    
def r_audio():
    speech_recognisor= sr.Recognizer()
    speak("How can i help you..")
    with sr.Microphone() as source:
        audio= speech recognizer.listen(source)
        voice_data=''
        
    try:
        voice_data = speech_recognisor.recognize_google(audio,)
    except sr.UnknownValueError:
        print('PLease repeat i did not get that')
        print('PLease repeat i did not get that')
        r_audio()
        respond(voice_data)
        