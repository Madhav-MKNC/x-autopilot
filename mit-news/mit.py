# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

URL = "https://news.mit.edu/topic/machine-learning"

# headers for get request
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


response = requests.get(URL)

print(response.text)

with open('mit.html', 'w', encoding="utf-8") as file:
    file.write(response.text)

# get urls for the articles from the articles-base-url
def fetch_articles_perplexity_discover(url):

    print(f"[*] Fetching articles from {url}")
    
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = []

    article_elements = soup.find_all('article')
    if not article_elements:
        print("[-] No articles found")
        return

    try:
        this_articles = [{
            'link': article.a['href'],
            'title': article.text.strip()
        } for article in article_elements]
        articles.extend(this_articles)
    except Exception as err:
        print("\033[31m" + '[error]', url, str(err) + "\033[m")

    return articles

# scrape webpage


def scrape_content(url):
    print(f"|- Scraping content from URL: {url}")
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.find_all('p')
    content = ' '.join([p.text for p in paragraphs])
    # print(content) # remove this after testing
    return content



from bs4 import BeautifulSoup

# Example HTML content (truncated for clarity)
html_content = """
<div ...>
    <a href="/search/Chinas-astronaut-rail-W0e1IMUfTjqMbNYN3cNo1w">...</a>
    <div class="grow">...</div>
</div>
"""

# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the href link
# Assuming the first <a> tag within the main div contains the href
href_link = soup.find('a')['href']

# Extract the title
# Assuming the title is within a div with a specific data-testid attribute
title = soup.find('div', attrs={'data-testid': 'thread-title'}).text.strip()

# Extract the description
# Assuming the description is within a specific div structure following the title
description = soup.select_one('div.grow > a > div > div:nth-of-type(2)').text.strip()

print("Href Link:", href_link)
print("Title:", title)
print("Description:", description)
