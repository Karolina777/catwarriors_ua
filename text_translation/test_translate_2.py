from googletrans import Translator


def translate_text(text, to_lang):
    # Create an instance of the Translator
    translator = Translator()

    # Translate each name and store the translations in a new array
    translations = []
    for name in text:
        print(name)
        translation = translator.translate(name, dest=to_lang).text
        translations.append(translation)

    # Return the translated names
    return translations


# Define the array of names to be translated
names = [
    '''
    A paw clipping against her ear woke Dovepaw; keeping her eyes closed, she batted irritably at it. “Get off, Ivypaw! I need to sleep.” Nearly a moon
had passed since the apprentice ceremony, and the day before, their mentors had given them their first assessment, on the far side of the territory.
    '''
   ]



# Call the translate_text function with the names and target language
translated_names = translate_text(names, 'uk')

# Print the translated names
print(translated_names)
