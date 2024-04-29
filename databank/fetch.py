# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.artificialintelligence-news.com/artificial-intelligence-news"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(URL)
html_content = response.text

# logging
print(html_content)

# debugging
with open('ai-news.html', 'w', encoding="utf-8") as file:
    file.write(html_content)

soup = BeautifulSoup(html_content, 'html.parser')
articles = soup.find_all('a', class_='term-page--news-article--item--title--link')

news = []
for article in articles:
    title = article.text.strip() 
    link = article['href']
    news.append({'title': title, 'link': link})

# logging
print(news)

with open('news.json', 'w', encoding='utf-8') as file:
    json.dump(news, file, ensure_ascii=False, indent=4)

