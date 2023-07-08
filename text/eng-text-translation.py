from pygoogletranslation import Translator


# Function to read text from a file
def read_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


# Function to translate text from English to Ukrainian
def translate_to_ukrainian(text):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src='en', dest='uk')
    return translation.text


# File path of the input text file
file_path = 'eng-text.txt'

# Read text from the file
english_text = read_text_from_file(file_path)

# print(english_text)

# Translate the text to Ukrainian
ukrainian_text = translate_to_ukrainian(english_text)

# Print the translated text
print(ukrainian_text)
