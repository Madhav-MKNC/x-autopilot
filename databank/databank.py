# -*- coding: utf-8 -*-
# This script manages the databank i.e, pops the content from posts.json

import json
import os
from datetime import datetime


current_month = datetime.now().month
databank_filename = f"databank/databank-{current_month}.json"

if not os.path.exists(databank_filename):
    with open(databank_filename, 'w', encoding='utf-8') as file:
        file.write("[]")

databank = []


def add(x: list):
    with open(databank_filename, 'r') as file:
        databank = json.load(file)
    databank.extend(x)
    with open(databank_filename, 'w', encoding='utf-8') as file:
        json.dump(databank, databank_filename)
    

def pop(item: dict):
    with open(databank_filename, 'r') as file:
        databank = json.load(file)
    content = databank.pop()
    with open(databank_filename, 'w', encoding='utf-8') as file:
        json.dump(databank, databank_filename)
    return content


# with open('news.json', 'w', encoding='utf-8') as file:
#     json.dump(news, file, ensure_ascii=False, indent=4)
