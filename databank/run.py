# -*- coding: utf-8 -*-

from web import Scraper, URLS_1
from generate import generate_posts
from utils import read_databank


for url in URLS_1:
    print("* Scraping", url)
    Scraper(url=url, source=1).fetch()


databank = read_databank()

print(f"\nTotal no. of articles in the databank: {len(databank)}")
try:
    input("\nPress enter to view or CTRL+C to exit...")
except KeyboardInterrupt:
    exit()
for i, article in enumerate(databank):
    print(f"[{i+1}] {article['title']}")


try:
    input("\nGenerate posts with OpenAI? Press Enter to continue or else CTRL+C...")
except KeyboardInterrupt:
    exit()
generate_posts(databank)

