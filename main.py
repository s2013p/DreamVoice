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
    if search_query!="Nie zrozumiałem":
        search_results = search_wikipedia(search_query)
        if "error" in search_results:
            print(search_results["error"])
        else:
            print(f"Wyniki wyszukiwania dla '{search_query}':\n")
            say(f"Wyniki wyszukiwania dla '{search_query}'")
            for title, details in search_results.items():
                print(f"Tytuł: {title}")
                say(f"Tytuł: {title}")
                print("Czytać to? Kliknij enter jeśli tak jeśli nie wpisz COKOLWIEK i wciśnij enter.")
                say("Czytać to?. Kliknij enter jeśli tak jeśli nie wpisz COKOLWIEK i wciśnij enter.")
                if input()=="":
                    print(f"Skrót: {details['snippet']}")
                    say(f"Skrót: {details['snippet']}")
                    print(f"pageid: {details['pageid']}")
                    print("\n")
                    print("Czy czytać dalej? Wciśnij enter aby czytać. wpisz COKOLWIEK i kliknij enter aby nie czytać")
                    say("Czy czytać dalej? Wciśnij enter aby czytać. wpisz COKOLWIEK i kliknij enter aby nie czytać")
                    if input()=="":
                        pass
                    else:
                        break
                
                

print("Witaj. Jestem Dream-twój asystent marzeń")
say("Witaj. Jestem Dream.twój asystent marzeń")
while True:
    done=False
    print("Jakiej aplikacji chcesz teraz użyć?")
    say("Jakiej aplikacji chcesz teraz użyć?")
    n = stt(listen())
    n = str(n)
    print(n)
    if "wikipedia" in n.lower():
        wikipedia()
    elif "tłumacz" in n.lower():
        say("Co chcesz przetłumaczyć?")
        nn=str(stt(listen()))
        print(nn)
        j=auto_translate(nn, "en")
        print(j)
        say(j,"en")
    elif "bingo" in n.lower():
        bingo()
    elif "pa" in n.lower() or "widzenia" in n.lower() or "wyjdź" in n.lower():
        exit()

    else:
        print("Nie obsługuję tej aplikacji")
        say("nie obsługuję tej aplikacji")
