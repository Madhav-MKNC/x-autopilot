# Manually fetched content from whatever sources

Content will be manually fetched and stored in a bot-readable organised structure. 
The bot will post one tweet based on a new article from the databank everyday until all the articles in the databank are posted.

## Sources

- https://www.artificialintelligence-news.com
- https://www.blockchaintechnology-news.com
- https://www.cloudcomputing-news.net
- https://www.developer-tech.com

## Working

- <code>fetch.py</code> - News articles are fetched manually from sources and are stored in JSON format
- <code>generate.py</code> - Generate posts to tweet using an LLM and the news articles as context
- Generated posts are stored in <code>posts.json</code>
- <code>__init__.py</code> - This script manages the databank i.e, pops the content from posts.json

