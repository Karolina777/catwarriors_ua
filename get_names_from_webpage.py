import requests
import pandas as pd
import re
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://uawarriors.fandom.com/uk/wiki/%D0%91%D1%96%D0%BB%D0%BE%D0%BA%D1%80%D0%B8%D0%BB%D0%B0"

# Send a GET request to the webpage
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the desired text content
text_elements = soup.find_all('p')  # Adjust this according to your needs

# Extract the text from the elements
text_data = [element.get_text() for element in text_elements]

# Join the text data into a single string
all_text = ' '.join(text_data)

# finding ukrainian names
# Find the text between "Ланцюг імен" and "Англійський ланцюг імен" using regex
pattern_ua = r"Ланцюг імен(.*?)Англійський ланцюг імен"
matches = re.findall(pattern_ua, all_text, re.DOTALL)

# Remove leading/trailing whitespace from each match
filtered_text_data = [match.strip() for match in matches]

# finding english names
pattern_uk = r"Англійський ланцюг імен(.*?)Дослівний переклад імені"
matches = re.findall(pattern_uk, all_text, re.DOTALL)

filtered_text_data.append([match.strip() for match in matches][0])

print(filtered_text_data)


# write the set of UA and UK names into dataframe
df_to_add = pd.DataFrame(columns=['kitten_ua', 'apprentice_ua', 'warrior_ua', 'kitten_uk', 'apprentice_uk', 'warrior_uk'])

# Iterate over the list elements and split the values
split_data = filtered_text_data[0].split(' → ')
second_element_split = filtered_text_data[1].split(' → ')
for i in range(len(second_element_split)):
    split_data.append(second_element_split[i])


row = {col: split_data[i] if i < len(split_data) else '' for i, col in enumerate(df_to_add.columns)}
df_to_add = df_to_add._append(row, ignore_index=True)
print(df_to_add)

filename = "scraped_names_data.csv"
df_existing = pd.read_csv(filename)
df_existing = df_existing._append(df_to_add, ignore_index=True)
df_existing.to_csv(filename, index=False)


# Write the extracted text into a file
# filename = "scraped_text.txt"
# with open(filename, 'w', encoding='utf-8') as file:
#     for text in text_data:
#         file.write(text + '\n')
#
# print(f"Scraped text has been saved to {filename}.")
#
# # Print the extracted text
# for text in text_data:
#     print(text)
