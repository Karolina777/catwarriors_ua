import requests
import pandas as pd
import re
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://uawarriors.fandom.com/uk/wiki/%D0%92%D0%BE%D0%B3%D0%BD%D0%B5%D0%B7%D1%96%D1%80"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

text_elements = soup.find_all('p')  # Find the desired text content
text_data = [element.get_text() for element in text_elements]   # Extract the text from the elements
all_text = ' '.join(text_data)  # Join the text data into a single string

# finding ukrainian names - the text between "Ланцюг імен" and "Англійський ланцюг імен" using regex
pattern_ua = r"Ланцюг імен(.*?)Англійський ланцюг імен"
matches = str(re.findall(pattern_ua, all_text, re.DOTALL)[0])
ua_names = re.findall(r'\b\w+\b', matches.replace('\n', ''))
print(ua_names)

# finding english names
pattern_uk = r"Англійський ланцюг імен(.*?)Дослівний переклад імені"
matches = str(re.findall(pattern_uk, all_text, re.DOTALL)[0])
uk_names = re.findall(r'\b\w+\b', matches.replace('\n', ''))
print(uk_names)

data = {"link": url, "ua_names": ua_names, "uk_names": uk_names}
df = pd.DataFrame(data)

print(data)

filename = "scraped_names_data.csv"
# df_existing = pd.read_csv(filename)
# df_existing = df_existing._append(df_to_add, ignore_index=True)
df.to_csv(filename, index=False)
