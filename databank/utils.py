# -*- coding: utf-8 -*-
# This script manages the databank

import json
import os
from datetime import datetime


current_month = datetime.now().month
databank_filename = f"databank/databank-{current_month}.json"
if not os.path.exists(databank_filename):
    with open(databank_filename, 'w', encoding='utf-8') as file:
        file.write("[]")
        
posts_filename = "posts.json"
if not os.path.exists(posts_filename):
    with open(posts_filename, 'w', encoding='utf-8') as file:
        file.write("[]")


def read_databank() -> list:
    with open(databank_filename, 'r') as file:
        databank = json.load(file)
    return databank

def write_databank(x: list) -> None:
    with open(databank_filename, 'w', encoding='utf-8') as file:
        json.dump(x, file, indent=4)

def add_to_databank(x: list):
    databank = read_databank()
    # databank.extend(x)
    for i in x:
        if i not in databank:
            databank.append(i)
    write_databank(databank)

def pop_from_databank():
    databank = read_databank()
    content = databank.pop()
    write_databank(databank)
    return content


def read_posts() -> list:
    with open(posts_filename, 'r') as file:
        posts = json.load(file)
    return posts

def write_posts(x: list) -> None:
    with open(posts_filename, 'w', encoding='utf-8') as file:
        json.dump(x, file, indent=4)

def add_to_posts(x: list):
    posts = read_posts()
    # posts.extend(x)
    for i in x:
        if i not in posts:
            posts.append(i)
    write_posts(posts)

def pop_from_posts():
    posts = read_posts()
    content = posts.pop()
    write_posts(posts)
    return content

