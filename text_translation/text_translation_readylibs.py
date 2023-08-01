from translate import Translator as TranslateTranslator
from googletrans import Translator as GoogleTranslator
from text_preprocessing import split_text


def translate_text(text, to_lang, translation_library='googletrans'):
    """
    Translate the given text to the specified language using the chosen translation library.

    :param text: The text to be translated.
    :param to_lang: The target language code for translation (e.g., 'en', 'fr', 'es').
    :param translation_library: The preferred translation library, either 'googletrans' or 'translate'.
                                Defaults to 'googletrans'.
    :return: The translated text.
    """
    if translation_library == 'googletrans':
        translator = GoogleTranslator()
    elif translation_library == 'translate':
        translator = TranslateTranslator(to_lang=to_lang)
    else:
        raise ValueError("Invalid translation library. Please choose 'googletrans' or 'translate'.")

    chunks = split_text(text, 500)
    translations = []

    for i, chunk in enumerate(chunks):
        try:
            translation = translator.translate(chunk, dest=to_lang)
            translations.append(translation.text)
        except Exception as e:
            print(f"Error occurred: {e}")
            translations.extend([chunk] + chunks[i + 1:])
            break

    translated_text = '. '.join(translations)
    return translated_text
