import requests
from bs4 import BeautifulSoup

url = "https://znews.vn/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
for i in range(1, 6):
    element = soup.select_one(f"#section-latest > section > div > article:nth-child({i}) > header > p.article-title > a")
    print(element.text)
    tempoUrl = element.get("href")
    tempoResponse = requests.get(tempoUrl)
    tempoSoup = BeautifulSoup(tempoResponse.content, "html.parser")
    date = tempoSoup.select_one("li.the-article-publish")
    print(date.text)
