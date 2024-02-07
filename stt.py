import speech_recognition as sr
from translator import *

r = sr.Recognizer()
def listen():
    

    with sr.Microphone() as source:
        print("Mów teraz")
        audio=r.listen(source)

        return audio


def stt(listen,language="pl"):
    with sr.Microphone() as source:
        audio = listen

        try:
            text = r.recognize_google(audio, language=language)
            return text
        except sr.UnknownValueError:
            print(auto_translate("Nie zrozumiałem",language))
            stt(r)
            
        except sr.RequestError as e:
            return str(e)

