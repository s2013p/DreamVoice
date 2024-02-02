from googletrans import Translator, LANGUAGES


def auto_translate(text, target_lang):
    # Utwórz obiekt tłumacza
    translator = Translator()

    # Wykryj język źródłowy i przetłumacz na język docelowy
    translated = translator.translate(text, dest=target_lang)

    # Zbuduj słownik z wynikami
    result = {
        'original_text': text,
        'source_language': LANGUAGES.get(translated.src, "Unknown"),
        'target_language': LANGUAGES.get(target_lang, "Unknown"),
        'translated_text': translated.text
    }

    return result
