from translate import Translator
from langdetect import detect

def auto_translate(text, to_lang="en"):
    # Wykrywanie języka źródłowego tekstu
    source_language = detect(text)

    # Określ język źródłowy i docelowy na podstawie wykrytego języka
    translator = Translator(from_lang=source_language, to_lang=to_lang)

    # Przetłumacz tekst
    translation = translator.translate(text)

    return translation