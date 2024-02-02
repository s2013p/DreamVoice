import speech_recognition as sr
from translator import *


def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Mów teraz")
        audio=r.listen(source,timeout=3)

        return audio


def stt(listen,language="pl"):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        audio = listen

        try:
            text = r.recognize_google(audio, language=language)
            return text
        except sr.UnknownValueError:
            return auto_translate("Nie zrozumiałem",language)
        except sr.RequestError as e:
            return str(e)

