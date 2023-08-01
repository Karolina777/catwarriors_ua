from translate import Translator

# Function to read text from a file
def read_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def write_text_to_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        text = file.write(text)
    return print('file with translation is written')

# Function to translate text from English to Ukrainian
def translate_to_ukrainian(text):
    translator = Translator(to_lang="uk")
    translation = translator.translate(text)
    return translation

# File path of the input text file
file_path = 'eng-text.txt'

# Read text from the file
english_text = read_text_from_file(file_path)

# Translate the text to Ukrainian
ukrainian_text = translate_to_ukrainian(english_text)

# Print the translated text
print(ukrainian_text)

file_path_ukr = 'ukr-text.txt'
write_text_to_file(file_path_ukr, ukrainian_text)