#Requirments: pyttsx3 , gTTS , pygame, SpeechRecognition, pyautogui, bs4, requests, langdetect, pyaudio, translate
from os import system
system("pip install pyttsx3 gTTS pygame SpeechRecognition pyautogui bs4 requests langdetect pyaudio translate")
from stt import *
from tts import *
from translator import *
from wikipedia import *


"""system("C:/windows/system32/shutdown.exe -s")
            say("Dziekuje że wybrałeś asystenta dream. Mam nadzieję że spełnił twoje oczekiwania. Komputer wyloguje cię za około minutę. Mam nadzieję że polecisz mnie znajomym oraz rodzinie. Jeśli wystąpiły jakieś błędy najmocniej za nie przepraszam. Nasz zespół już nad nimi pracuje.")
            exit()"""


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
                print("Przeczytać to?")
                say("Przeczytać to?")
       
                if "tak" in stt(listen()).lower():
                    print(f"Skrót: {details['snippet']}")
                    say(f"Skrót: {details['snippet']}")
                    print(f"pageid: {details['pageid']}")
                    print("\n")
                    print("Czy czytać dalej?")
                    say("Czy czytać dalej?")
                    if "tak" in stt(listen()).lower():
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
    elif "komputer" in n.lower():
        print("Co chcesz zrobić z komputerem?")
        say("Co chcesz zrobić z komputerem?")
        n=stt(listen())
        from pyautogui import typewrite as typee
        from pyautogui import press
        press("win")
        typee("cmd")
        press("enter")
        from time import sleep
        sleep(1)
        
        
        if "wyłącz" in n.lower():
            typee("cd C:/windows/system32")
            press("enter")
            typee("shutdown /s /f /t 60 /c \"The computer will shut down in 1 minute. Save your work!\"")
            press("enter")
            typee("exit")
            press("enter")
            say("Dziekuje że wybrałeś asystenta dream. Mam nadzieję że spełnił twoje oczekiwania. Komputer wyłączy się za około minutę. Mam nadzieję że polecisz mnie znajomym oraz rodzinie. Jeśli wystąpiły jakieś błędy najmocniej za nie przepraszam. Nasz zespół już nad nimi pracuje.")
            exit()
        elif "ponownie" in n.lower():
            typee("cd C:/windows/system32")
            press("enter")
            typee("shutdown /r /f /t 60 /c \"The computer will shut down in 1 minute. Save your work!\"")
            press("enter")
            typee("exit")
            press("enter")
            say("Dziekuje że wybrałeś asystenta dream. Mam nadzieję że spełnił twoje oczekiwania. Komputer uruchomi ponownie się za około minutę. Mam nadzieję że polecisz mnie znajomym oraz rodzinie. Jeśli wystąpiły jakieś błędy najmocniej za nie przepraszam. Nasz zespół już nad nimi pracuje.")
            exit()
        elif "wyloguj" in n.lower():
            typee("cd C:/windows/system32")
            press("enter")
            typee("shutdown /l")
            press("enter")
            typee("exit")
            press("enter")
            say("Dziekuje że wybrałeś asystenta dream. Mam nadzieję że spełnił twoje oczekiwania. Komputer wyloguje cię za około minutę. Mam nadzieję że polecisz mnie znajomym oraz rodzinie. Jeśli wystąpiły jakieś błędy najmocniej za nie przepraszam. Nasz zespół już nad nimi pracuje.")
            exit()
        
            
    elif "pa" in n.lower() or "widzenia" in n.lower() or "wyjdź" in n.lower():
        exit()

    else:
        print("Nie obsługuję tej aplikacji")
        say("nie obsługuję tej aplikacji")
