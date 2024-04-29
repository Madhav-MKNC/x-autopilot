# -*- coding: utf-8 -*-

import databank
import requests
from bs4 import BeautifulSoup
import json


URLS = [
    "https://www.artificialintelligence-news.com",
    "https://www.blockchaintechnology-news.com",
    "https://www.cloudcomputing-news.net",
    "https://www.developer-tech.com"
]


class Scraper:
    def __init__(self, url: str) -> None:
        self.url = url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        self.soup = BeautifulSoup(self.__get_html(), 'html.parser')
    
    def __get_html(self):
        response = requests.get(url=self.url, headers=self.headers)
        response.raise_for_status()
        html = response.text
        return html
    
    def __get_articles(self):
        news_items = self.soup.find_all('article')
        return news_items
    
    def __save(self):
        databank.add(self.news_data)

    def fetch(self):
        self.news_data = []
        for item in self.__get_articles():
            title_element = item.find('a', title=True)
            description_element = item.find('p')

            if title_element and description_element:
                title = title_element['title']
                link = title_element['href']
                description = description_element.text.strip()

                self.news_data.append({
                    'title': title,
                    'link': link,
                    'description': description
                })
        self.__save()


if __name__ == "__main__":
    URL = "https://www.artificialintelligence-news.com"
    
    news = Scraper(url=URL).fetch()
    with open('databank/news.json', 'w', encoding='utf-8') as file:
        json.dump(news, file, ensure_ascii=False, indent=4)
