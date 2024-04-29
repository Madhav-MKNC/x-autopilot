# -*- coding: utf-8 -*-
# Generate posts using an LLM with prompt and the news articles as context.

from openai import OpenAI, OpenAIError

from utils import add_to_posts

import os
from dotenv import load_dotenv
load_dotenv()

# Initialize OpenAI
openai_client = OpenAI(api_key=os.environ["OPENAI_API_KEY"],)
openai_model = "gpt-4-turbo"


def synthesize_post(context="") -> str:
    prompt = [
        {
            'role': 'system',
            'content': "You are a well known expert tech influencer on twitter. You will be given some text. You have to write a tweet about it without changing much but only enhancing some little certain parts. You will then generate the tweet and only return it in plain text without any noise. If you understood the job say YES."
        },
        {
            'role': 'assistant',
            'content': "YES."
        },
        {
            'role': 'user',
            'content': f"Please create a simple short tweet out of the following text without deleting anything and keeping the whole tweet under 250 characters. Tweet should not contain any emojis or other special characters. Content: {context}"
        }
    ]
    try:
        response = openai_client.chat.completions.create(
            messages=prompt,
            model=openai_model
        )
        output = response.choices[0].message.content
        return output
    except OpenAIError as e:
        print('\033[31m*** get_gpt_response():', str(e), "\033[m")
        return ""


def generate_posts(databank: list) -> list:
    posts = []
    try:
        for i, article in enumerate(databank):
            title = article['title']
            content = article['content']
            print(f"\n[{i+1}] Generating for- {title}")
            post = synthesize_post(context=content)
            posts.append(post)
            print(post)
    except KeyboardInterrupt:
        print("Done.")
    
    add_to_posts(posts)
    return posts

