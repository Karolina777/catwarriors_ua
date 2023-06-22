import requests
from bs4 import BeautifulSoup

# URL of the web page
url = "https://uawarriors.fandom.com/uk/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D1%96%D1%8F:%D0%93%D1%80%D0%BE%D0%BC%D0%BE%D0%B2%D0%B8%D0%B9_%D0%9A%D0%BB%D0%B0%D0%BD"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all <a> tags that have an href attribute starting with "https://uawarriors.fandom.com/uk/wiki/"
http_links = [a["href"] for a in soup.find_all("a", href=lambda href: href and href.startswith("https://uawarriors.fandom.com/uk/wiki/"))]

# Print the list of HTTP links
for link in http_links:
    print(link)
