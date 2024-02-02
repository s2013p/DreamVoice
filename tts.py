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
