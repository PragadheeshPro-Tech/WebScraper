import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")
headlines = soup.find_all("h2")
headline_list = [headline.get_text(strip=True) for headline in headlines if headline.get_text(strip=True)]

with open("headlines.txt", "w", encoding="utf-8") as file:
    for h in headline_list:
        file.write(h + "\n")
