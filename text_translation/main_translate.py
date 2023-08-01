import pandas as pd

from spacy.cli import download
from text_preprocessing import split_text, replace_newline_with_space
from text_NER import get_named_entities



# Read the text from the file with the correct encoding (e.g., UTF-8)
file_path = 'texts/text.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    text_en = file.read()

# text_en = replace_newline_with_space(text_en)
print(f'ORIGINAL ENGLISH TEXT:\n{text_en}\n\n\n')

paragraphs = split_text(text_en, 500)
for i, chunk in enumerate(paragraphs):
    print(f'Chunk #{i}:\n{chunk}\n\n')
print("all chunks are printed")


# # Open the file in write mode with the 'utf-8' encoding
# with open(file_path, 'w', encoding='utf-8') as file:
#     file.write(text_en)

# # Get the set of named entities from the original text
# named_entities_en = get_named_entities(text_en)
# # print(type(named_entities))
#
# named_entities_ua = list()
#
# for name in named_entities_en:
#     if name.endswith("'s"):
#         name = name[:-2]
#     translated_name = translate_text(name, 'uk', 'googletrans')
#     if translated_name.endswith('.'):
#         translated_name = translated_name[:-1]
#     named_entities_ua.append(translated_name)
#
# df_named_entities = pd.DataFrame({'names english': named_entities_en, 'names ukrainian': named_entities_ua})
#
# df_named_entities.to_csv('Names-in-text-en-ua.csv', index=False, encoding='utf-8')
# print(df_named_entities)

# # Call the translate_text function with the input text and target language
# translated_text_google = translate_text(text_en, 'uk', 'googletrans')
# print(translated_text_google)
# translated_text_translate = translate_text(text_en, 'uk', 'translate')
# print(f'\n\n{"non-google translation".upper()}\n{translated_text_translate}')
#
# # Print the translated text
# # print(translated_text)
#
#
# # Open the file in write mode with the 'utf-8' encoding
# with open(file_path.replace(".txt", "-ua.txt"), 'w', encoding='utf-8') as file:
#     file.write('Google translator:\n')
#     file.write(translated_text_google)
#     file.write('\n\n\nOther translator:\n')
#     file.write(translated_text_translate)

# print("Text has been written to the file.")
