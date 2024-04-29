# -*- coding: utf-8 -*-

from web import Scraper, URLS
from generate import synthesize_post
from utils import read_databank


for url in URLS:
    print("* Scraping", url)
    Scraper(url).fetch()


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
posts = []
try:
    for i, article in enumerate(databank):
        title = article['title']
        content = article['description']
        print(f"[{i+1}] Generating post with {title}")
        post = synthesize_post(context=content)
        posts.append(post)
except KeyboardInterrupt:
    print("Done.")
import json
with open('databank/posts.json', 'w', encoding='utf-8') as file:
    json.dump(posts, file, indent=4)
