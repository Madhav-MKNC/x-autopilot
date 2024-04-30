# -*- coding: utf-8 -*-

import utils
import requests
from bs4 import BeautifulSoup
import json
from uuid import uuid4


URLS_1 = [
    "https://www.artificialintelligence-news.com",
    "https://www.blockchaintechnology-news.com",
    "https://www.cloudcomputing-news.net",
    "https://www.developer-tech.com"
]

URLS_2 = [
    "https://news.mit.edu/topic/machine-learning?page=0"
]


class Scraper:
    def __init__(self, url: str, source: int = 1) -> None:
        self.url = url
        self.source = source
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        self.__process_html()
    
    def __process_html(self) -> None:
        response = requests.get(url=self.url, headers=self.headers)
        response.raise_for_status()
        html_content = response.text
        self.soup = BeautifulSoup(html_content, 'html.parser')
     
    def fetch(self) -> list:
        if self.source == 1:
            return self.__fetch_1()
        elif self.source == 2:
            return self.__fetch_2()
    
    def __fetch_1(self) -> list:
        news_items = self.soup.find_all('article')
        self.news_data = []
        
        for item in news_items:
            title_element = item.find('a', title=True)
            description_element = item.find('p')
            
            if title_element and description_element:
                title = title_element['title']
                link = title_element['href']
                description = description_element.text.strip()
                news_item = {
                    'title': title,
                    'link': link,
                    'description': description,
                    'content': f"Title: {title}\n\n{description}"
                }

                if news_item not in self.news_data:
                    self.news_data.append(news_item)
        self.__save()
        return self.news_data
    
    def __fetch_2(self) -> list:
        news_items = self.soup.find_all("div", class_="term-page--news-article--item--descr")
        self.news_data = []
        
        for item in news_items:
            title_element = item.find(class_="term-page--news-article--item--title--link")
            description_element = item.find(class_="term-page--news-article--item--dek")

            if title_element and description_element:
                title = title_element.get_text(strip=True)
                link = title_element['href']
                description = description_element.get_text(strip=True)
                news_item = {
                    'title': title,
                    'link': link,
                    'description': description,
                    'content': f"Title: {title}\n\n{description}"
                }
                
                if news_item not in self.news_data:
                    self.news_data.append(news_item)
        self.__save()
        return self.news_data
    
    def __save(self) -> None:
        utils.add_to_databank(self.news_data)
    
    def save_this(self, filename: str = "") -> None:
        if not filename.strip():
            # filename = f'databank/{str(uuid4())}.json'
            filename = f"databank/{url.split('.')[1]}.json"
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(self.news_data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    
    for url in URLS_1:
        scraper = Scraper(url=url, source=1)
        scraper.fetch()
        # scraper.save_this()

    