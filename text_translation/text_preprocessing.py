import re


def split_text(text, max_length):
    # Split the text into sentences
    # TODO: include in pattern cases like !" or ?" or ". ` as well
    # sentence_split_pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)(?<!\w\.")\s'
    # sentence_split_pattern = r'\.\s|\.|"\n|!"|\?|"\. '
    sentence_split_pattern = r'\n'
    sentences = re.split(sentence_split_pattern, text)
    # for sentence in sentences:
    #     print(sentence, "\n")

    # Split sentences into chunks of maximum length
    chunks = []
    current_chunk = ''
    for sentence in sentences:
        if len(current_chunk + sentence) < max_length:
            current_chunk += '\n' + sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence.strip()

    return chunks


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


# Specify the file path of the text file
file_path = 'texts/text.txt'

# Read the text from the file with the correct encoding (e.g., UTF-8)
with open(file_path, 'r', encoding='utf-8') as file:
    text_en = file.read()

print(f'ORIGINAL ENGLISH TEXT:\n{text_en}\n\n\n')

paragraphs = split_text(text_en, 500)
for i, chunk in enumerate(paragraphs):
    print(f'Chunk #{i}:\n{chunk}\n\n')

print("all chunks are printed")
