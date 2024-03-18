# -*- coding: utf-8 -*-

import requests

URL = "https://www.perplexity.ai/discover"

response = requests.get(URL)

print(response.html)

