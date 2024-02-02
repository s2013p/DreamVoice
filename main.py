#Requirments: pyttsx3 , gTTS , pygame, SpeechRecognition, pyautogui, bs4, requests, langdetect, pyaudio, translate
from os import system
system("pip install pyttsx3 gTTS pygame SpeechRecognition pyautogui bs4 requests langdetect pyaudio translate")
from stt import *
from tts import *
from translator import *
from wikipedia import *
from bingo import *


def wikipedia():
    print("Wypowiedz zapytanie do wikipedi: ")
    say("Wypowiedz zapytanie do wikipedi")
    search_query = stt(listen())
    print(search_query)
    search_results = search_wikipedia(search_query)
    if "error" in search_results:
        print(search_results["error"])
    else:
        print(f"Wyniki wyszukiwania dla '{search_query}':\n")
        say(f"Wyniki wyszukiwania dla '{search_query}'")
        for title, details in search_results.items():
            print(f"Tytuł: {title}")
            say(f"Tytuł: {title}")
            print(f"Skrót: {details['snippet']}")
            say(f"Skrót: {details['snippet']}")
            print(f"pageid: {details['pageid']}")
            print("\n")


while True:
    print("Jakiej aplikacji chcesz teraz użyć?")
    say("Jakiej aplikacji chcesz teraz użyć?")
    n = stt(listen())
    n = str(n)
    print(n)
    if "wikipedia" in n.lower():
        wikipedia()
    elif "tłumacz" in n.lower():
        say("Co chcesz przetłumaczyć?")
        j=auto_translate(str(stt(listen())), "en")
        print(j)
        say(j,"en")
    elif "bingo" in n.lower():
        bingo()

    else:
        print("Nie obsługuję tej aplikacji")
        say("nie obsługuję tej aplikacji")
