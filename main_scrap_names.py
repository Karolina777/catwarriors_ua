import requests
import pandas as pd
import re
from bs4 import BeautifulSoup


def extract_links_with_prefix(url, prefix, exclude_pages):
    response = requests.get(url)  # Send a GET request to the URL
    soup = BeautifulSoup(response.content, "html.parser")    # Parse the HTML content using BeautifulSoup

    # Find all <a> tags that have an href attribute starting with the specified prefix
    links = [a["href"] for a in soup.find_all("a", href=lambda href: href and href.startswith(prefix))]

    # Exclude the specific page or link
    links = [link for link in links if link not in exclude_pages]

    return links


def extract_names_from_webpage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    text_elements = soup.find_all('p')  # Find the desired text content
    text_data = [element.get_text() for element in text_elements]   # Extract the text from the elements
    all_text = ' '.join(text_data)        # Join the text data into a single string

    # Find the  Ukrainian names  between "Ланцюг імен" and "Англійський ланцюг імен" using regex
    pattern_ua = r"Ланцюг імен(.*?)Англійський ланцюг імен"
    matches = re.findall(pattern_ua, all_text, re.DOTALL)
    filtered_text_data = [match.strip() for match in matches]   # Remove leading/trailing whitespace from each match

    # Finding English names
    pattern_uk = r"Англійський ланцюг імен(.*?)Дослівний переклад імені"
    matches = re.findall(pattern_uk, all_text, re.DOTALL)

    if matches == []:
        return None

    filtered_text_data.append([match.strip() for match in matches][0])

    #TODO make the element flexible to number of names
    # (i.e. if only a cat has 2 names or 4 names, the structure of the element (row) is the same: link_to_webpage, ua_names. uk_names)

    # Create a DataFrame to store the names
    df_to_add = pd.DataFrame(columns=['kitten_ua', 'apprentice_ua', 'warrior_ua',
                                      'kitten_uk', 'apprentice_uk', 'warrior_uk'])

    # Iterate over the list elements and split the values
    split_data = filtered_text_data[0].split(' → ')
    second_element_split = filtered_text_data[1].split(' → ')
    for i in range(len(second_element_split)):
        split_data.append(second_element_split[i])

    # Create a dictionary with the split values and add it to the DataFrame
    row = {col: split_data[i] if i < len(split_data) else '' for i, col in enumerate(df_to_add.columns)}
    df_to_add = df_to_add._append(row, ignore_index=True)

    return df_to_add

# Example usage
url = "https://uawarriors.fandom.com/uk/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D1%96%D1%8F:%D0%93%D1%80%D0%BE%D0%BC%D0%BE%D0%B2%D0%B8%D0%B9_%D0%9A%D0%BB%D0%B0%D0%BD"
prefix = "https://uawarriors.fandom.com/uk/wiki/"
exclude_pages = \
    ["https://uawarriors.fandom.com/uk/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0",
     "https://uawarriors.fandom.com/uk/wiki/%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0:AllPages",
     "https://uawarriors.fandom.com/uk/wiki/%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0:Community",
     "https://uawarriors.fandom.com/uk/wiki/%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0:AllMaps",
     "https://uawarriors.fandom.com/uk/wiki/%D0%A6%D0%B8%D0%BA%D0%BB%D0%B8"]

http_links = extract_links_with_prefix(url, prefix, exclude_pages)

filename = "scraped_names_data_full.csv"
# df_existing = pd.read_csv(filename)
df_existing = pd.DataFrame()

# Print the list of HTTP links
for link in http_links:
    print(link)
    df_names = extract_names_from_webpage(link)
    print(df_names)
    df_existing = df_existing._append(df_names, ignore_index=True)


df_existing.to_csv(filename, index=False)
