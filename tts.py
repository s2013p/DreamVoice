from gtts import gTTS
from pygame import mixer
import os
import tempfile

def say(text, lang='pl'):
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
