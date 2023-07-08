import requests
import pandas as pd
import re
from bs4 import BeautifulSoup


def extract_links_with_prefix(url, prefix, exclude_pages = []):
    response = requests.get(url)  # Send a GET request to the URL
    soup = BeautifulSoup(response.content, "html.parser")    # Parse the HTML content using BeautifulSoup

    # Find all <a> tags that have an href attribute starting with the specified prefix
    links = [a["href"] for a in soup.find_all("a", href=lambda href: href and href.startswith(prefix))]

    # TODO check if this causes duplicates in links Exclude the specific page or link
    links = [link for link in links if link not in exclude_pages]

    return links


def extract_names_from_webpage(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    text_elements = soup.find_all('p')  # Find the desired text content
    text_data = [element.get_text() for element in text_elements]   # Extract the text from the elements
    all_text = ' '.join(text_data)        # Join the text data into a single string

    # patterns to find ukrainian and english names - the text between "Ланцюг імен" and "Англійський ланцюг імен" using regex
    pattern_ua = r"Ланцюг імен(.*?)Англійський ланцюг імен"
    pattern_uk = r"Англійський ланцюг імен(.*?)Дослівний переклад імені"

    try:
        matches = str(re.findall(pattern_ua, all_text, re.DOTALL)[0]).lower()
        ua_names = re.findall(r'\b\w+\b', matches.replace('\n', '').replace('невідомо', '').title())
        # print(ua_names)
        matches = str(re.findall(pattern_uk, all_text, re.DOTALL)[0])
        uk_names = re.findall(r'\b\w+\b', matches.replace('\n', ''))
        # print(uk_names)
    except IndexError:
        return print(f'--- Not the page with the cat name {url}')

    if len(ua_names) == len(uk_names):
        data = {"link": url, "ua_names": ua_names, "uk_names": uk_names}
        print(f'return dataframe {data["ua_names"][0]}')

    elif uk_names[0] == 'Heatherkit':
        ua_names.append(ua_names[len(ua_names)-1])

        for i in range(2, len(uk_names)-1):
            ua_names[len(uk_names)-i-1] = ua_names[len(uk_names)-i-2]

        ua_names[0] = 'Вереска'
        data = {"link": url, "ua_names": ua_names, "uk_names": uk_names}
        print(f'++++++ solved ---------- {url}\n--------{ua_names}---{uk_names}')

    elif uk_names[0] == 'Featherkit':
        ua_names_with_apostrof = [ua_names[0]+"'"+ua_names[1].lower()]

        for i in range(1, len(uk_names)):
            ua_names_with_apostrof.append(ua_names[i+1])

        data = {"link": url, "ua_names": ua_names_with_apostrof, "uk_names": uk_names}
        print(f'++++++ solved ---------- {url}\n--------{ua_names_with_apostrof}---{uk_names}')

    else:
        print(f'new case with error on the link {url}')
        data = {"link": url, "ua_names": "---error", "uk_names": "---error"}


    df = pd.DataFrame(data)
    # TODO drop duplicates - but I have a link in the 1st row of the Cat
    #  df = df.drop_duplicates()
    #  OR i need to find why the links go for the 2nd cycle


    return df

# Example usage
url = "https://uawarriors.fandom.com/uk/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D1%96%D1%8F:%D0%93%D1%80%D0%BE%D0%BC%D0%BE%D0%B2%D0%B8%D0%B9_%D0%9A%D0%BB%D0%B0%D0%BD"
prefix = "https://uawarriors.fandom.com/uk/wiki/"
# exclude_pages = []
    # ["https://uawarriors.fandom.com/uk/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0",
    #  "https://uawarriors.fandom.com/uk/wiki/%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0:AllPages",
    #  "https://uawarriors.fandom.com/uk/wiki/%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0:Community",
    #  "https://uawarriors.fandom.com/uk/wiki/%D0%A1%D0%BF%D0%B5%D1%86%D1%96%D0%B0%D0%BB%D1%8C%D0%BD%D0%B0:AllMaps",
    #  "https://uawarriors.fandom.com/uk/wiki/%D0%A6%D0%B8%D0%BA%D0%BB%D0%B8"
    # ]

http_links = extract_links_with_prefix(url, prefix)

print('links are exctracted')

filename = "scraped_names_data_full.csv"
# df_existing = pd.read_csv(filename)
df_name = pd.DataFrame()
df_all_names = pd.DataFrame()

# Print the list of HTTP links
for link in http_links:
    df_name = extract_names_from_webpage(link)
    if df_name is not None:
        # print(df_name)
        df_all_names = df_all_names._append(df_name, ignore_index=True)


df_all_names.to_csv(filename, index=False)
