from googletrans import Translator


def translate_text(text, to_lang):
    # Create an instance of the Translator
    translator = Translator(service_urls=['translate.google.com'])

    # Translate each name and store the translations in a new array
    translations = []
    for name in text:
        translation = translator.translate(name, dest=to_lang).text
        translations.append(translation)

    # Return the translated names
    return translations


# Define the array of names to be translated
names = ['Firepaw', 'Fireheart', 'Firestar']

# Call the translate_text function with the names and target language
translated_names = translate_text(names, 'uk')

# Print the translated names
print(translated_names)
