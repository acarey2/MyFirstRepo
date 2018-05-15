import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb
import speech_recognition as sr

speak= wincl.Dispatch("SAPI.SpVoice")

r= sr.Recognizer()
with sr.Microphone() as source:
    speak.Speak(" hello I am anne e shopping bot 2000. what store do you want to shop at")
    print("Listening...")
    audio = r.listen(source)
    print("Thinking...")


try:
    words = r.recognize_google(audio)
    speak.Speak("Ok Annie,let's look for " + r.recognize_google (audio))
    wb.open("https://www.google.com/search?q=" + words)

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.UnknownValueError:
    print ("AnnieBot2000 could not understand audio")
except sr.RequestError as e:
    print("Could not request results from ANN E BOT 2000; {0}".format(e))



















"""
speak = wincl. Dispatch ("SAPI.SPVoice")
speak.Speak ("Who is your favorite person?")
answer= pg.prompt ("Enter you favorite color.")

if answer== "annie":
    speak.Speak ("WOW, she is the best")
    wb.open ("https://www.google.com/search?rlz=1C1GCEA_enUS752US761&biw=1240&bih=561&tbm=isch&sa=1&ei=lKrxWq4n7e_mAv_uqtAP&q=kentucky+derby+winner+circle+2018+cnbc&oq=kentucky+derby+winner+circle+2018+cnbc&gs_l=img.3...96151.97215.0.97390.5.5.0.0.0.0.119.309.4j1.5.0....0...1c.1.64.img..0.0.0....0.N6letyRCr5M#imgrc=dzpkcFKlBclFJM:")

else:
    speak.Speak("never heard of them, must be a loser LOL ")
    
"""
