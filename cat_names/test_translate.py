import pandas as pd
from translate import Translator
import spacy
from spacy.cli import download
import re


def replace_newline_with_space(text):
    # Use regular expressions to find occurrences of a character at the end of a line
    pattern = re.compile(r'([a-zA-Z])(\n|, |\. |; |: )')
    # Replace newline characters with space if the previous line ends with a specific character
    result = re.sub(pattern, r'\1\2', text)

    pattern = re.compile(r'([a-zA-Z])([.,:;\-!?])\s*([a-zA-Z])')
    # Replace occurrences of letter + "."/","/":" + letter with letter + ". "/", "/": " + letter
    result = re.sub(pattern, r'\1\2 \3', result)

    pattern = re.compile(r'([a-zA-Z])\n([a-zA-Z])')
    result = re.sub(pattern, r'\1 \2', result)

    return result


def split_text(text, max_length):
    # Split the text into sentences
    sentences = text.split('. ')

    # Split sentences into chunks of maximum length
    chunks = []
    current_chunk = ''
    for sentence in sentences:
        if len(current_chunk + sentence) <= max_length:
            current_chunk += sentence + '. '
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + '. '

    # Add the last chunk to the list if it's not empty
    if current_chunk:
        chunks.append(current_chunk.strip())

    # Return the list of chunks
    return chunks


def get_named_entities(text):
    # Check if the 'en_core_web_sm' model is installed, and if not, download and install it
    if not spacy.util.is_package('en_core_web_sm'):
        download('en_core_web_sm')

    # Load the spaCy English model
    nlp = spacy.load('en_core_web_sm')

    # Process the text with spaCy
    doc = nlp(text)

    # Extract named entities from the document
    named_entities = set()
    for entity in doc.ents:
        if entity.label_ not in ['TIME', 'CARDINAL']:
            if ',' or "'" not in entity.text:
                named_entities.add(entity.text)

    # Return the set of named entities
    return named_entities


def translate_text_Translator(text, to_lang):
    # Create an instance of the Translator
    translator = Translator(to_lang=to_lang)

    # Split the text into chunks
    chunks = split_text(text, 500)

    # Translate each chunk and store the translations in a new array
    translations = []
    # for chunk in chunks:
    #     translation = translator.translate(chunk)
    #     translations.append(translation)
    # # TODO add the check that if the text exceeds max length,
    # #  then the rest is not translated and added in english the the output
    # #  (namely, after the 1st chunk everything goes in english)
    # #  OR simply if error appeares - everything else in english

    for i, chunk in enumerate(chunks):
        try:
            translation = translator.translate(chunk)
        except Exception as e:
            print(f"Error occurred: {e}")
            # If an error occurs during translation, add the remaining text in English
            translations.extend([chunk] + chunks[i+1:])
            break
        else:
            translations.append(translation)

    # Join the translated chunks into a single string
    translated_text = '. '.join(translations)

    # Return the translated text
    return translated_text


# Specify the file path of the text file
file_path = 'Chapter 6-12.txt'

# Read the text from the file with the correct encoding (e.g., UTF-8)
with open(file_path, 'r', encoding='utf-8') as file:
    text_en = file.read()

text_en = replace_newline_with_space(text_en)
# print(text_en)

# # Open the file in write mode with the 'utf-8' encoding
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(text_en)

# Get the set of named entities from the original text
named_entities = get_named_entities(text_en)

named_entities = pd.DataFrame(named_entities)
named_entities.to_csv('Names-in-text-en.csv', index=False)
# print(named_entities)

# Call the translate_text function with the input text and target language
translated_text = translate_text_Translator(text_en, 'uk')
#
# Print the translated text
print(translated_text)
#
#
# Open the file in write mode with the 'utf-8' encoding
with open(file_path.replace(".txt", "-ua.txt"), 'w', encoding='utf-8') as file:
    file.write(translated_text)

print("Text has been written to the file.")
