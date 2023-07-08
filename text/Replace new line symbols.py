import re

def replace_newline_with_space(text):
    # Use regular expressions to find occurrences of a character at the end of a line
    pattern = re.compile(r'([a-zA-Z,;:-])\n')
    # Replace newline characters with space if the previous line ends with a specific character
    result = re.sub(pattern, r'\1 ', text)
    return result

# Example usage
input_text = '''Hello,
this is a sample text.
The previous line ends with a letter t
and the newline symbol should be replaced with a space.
'''

output_text = replace_newline_with_space(input_text)
print(output_text)
