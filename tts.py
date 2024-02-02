from gtts import gTTS
from pygame import mixer
import os
import tempfile

def say(text, lang='pl'):
    try:
        # Tworzenie obiektu gTTS
        tts = gTTS(text=text, lang=lang)
        
        # Zapisanie pliku dźwiękowego w tymczasowym pliku
        with tempfile.NamedTemporaryFile(delete=True) as fp:
            temp_filename = f'{fp.name}.mp3'
            tts.save(temp_filename)
            
            # Odtwarzanie pliku dźwiękowego
            mixer.init()
            mixer.music.load(temp_filename)
            mixer.music.play()
            
            # Czekanie na zakończenie odtwarzania
            while mixer.music.get_busy():
                continue

            # Zatrzymanie odtwarzania i zwolnienie zasobów mixer'a
            mixer.music.stop()
            mixer.quit()
            
            # Usunięcie tymczasowego pliku
            os.remove(temp_filename)
        except:
            import pyttsx3

            def say(text, lang='pl'):
                engine = pyttsx3.init()

                # Ustaw język, pyttsx3 może wymagać dodatkowej konfiguracji dla różnych języków
                voices = engine.getProperty('voices')
                for voice in voices:
                    # Sprawdź dostępne języki w głosie (uwaga: 'languages' może zwracać listę kodów języków)
                    if lang in voice.languages:
                        engine.setProperty('voice', voice.id)
                        break


                # Odtwarzanie tekstu
                engine.say(text)
                engine.runAndWait()

