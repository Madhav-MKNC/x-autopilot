# -*- coding: utf-8 -*-

import utils
import requests
from bs4 import BeautifulSoup
import json
from uuid import uuid4


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
        self.__process_html()
        self.__get_articles()
    
    def __process_html(self) -> None:
        response = requests.get(url=self.url, headers=self.headers)
        response.raise_for_status()
        html_content = response.text
        self.soup = BeautifulSoup(html_content, 'html.parser')
        
    
    def __get_articles(self) -> None:
        self.news_items = self.soup.find_all('article')
    
    def __save(self) -> None:
        utils.add_to_databank(self.news_data)

    def fetch(self) -> list:
        self.news_data = []
        for item in self.news_items:
            title_element = item.find('a', title=True)
            description_element = item.find('p')
            if title_element and description_element:
                title = title_element['title']
                link = title_element['href']
                description = description_element.text.strip()
                news_item = {
                    'title': title,
                    'link': link,
                    'description': description
                }
                if news_item not in self.news_data:
                    self.news_data.append(news_item)
        self.__save()
        return self.news_data
    
    def save_this(self, filename: str = "") -> None:
        if not filename.strip():
            # filename = f'databank/{str(uuid4())}.json'
            filename = f"databank/{url.split('.')[1]}.json"
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.news_data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    
    for url in URLS:
        scraper = Scraper(url)
        scraper.fetch()
        # scraper.save_this()

    