# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

import os
from dotenv import load_dotenv
load_dotenv()


# for headless browser
options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

chrome_driver_path = "selenium/chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)


def login_to_twitter():
    driver.get('https://twitter.com/login')
    time.sleep(10)
    
    username = os.environ['TWITTER_USERNAME']
    password = os.environ['TWITTER_PASSWORD']
    
    username_field = driver.find_element(By.XPATH, '//input[@name="text"]')
    username_field.send_keys(username)
    username_field.send_keys(Keys.RETURN)
    time.sleep(5)
    
    password_field = driver.find_element(By.XPATH, '//input[@name="password"]')
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    time.sleep(10)


# def post_tweet(tweet_text):
#     driver.get('https://twitter.com/home')
#     time.sleep(5)

#     # Find the tweet text area and enter the tweet
#     tweet_box = driver.find_element(
#         By.XPATH, '//div[@aria-label="Tweet text"]')
#     tweet_box.send_keys(tweet_text)
#     time.sleep(2)
    
#     tweet_button = driver.find_element(
#         By.XPATH, '//div[@data-testid="tweetButtonInline"]')
#     tweet_button.click()
#     time.sleep(2)


# def post_tweet(tweet_text):
#     driver.get('https://twitter.com/home')
#     time.sleep(5)

#     try:
#         compose_box = driver.find_element(By.XPATH, "//div[@data-testid='tweetTextarea_0' and contains(@class,'public-DraftEditor-content')]")
#         compose_box.click()
#         time.sleep(2)
#     except Exception as e:
#         print("Error finding compose tweet box:", e)
#         return

#     try:
#         compose_box.send_keys(tweet_text)
#         time.sleep(2)
#         tweet_button = driver.find_element(By.XPATH, "//div[@data-testid='tweetButtonInline']")
#         tweet_button.click()
#         time.sleep(5)
#     except Exception as e:
#         print("Error Tweeting", e)
#         return



def post_tweet(tweet_text):
    driver.get('https://twitter.com/home')
    time.sleep(5)  # Allow time for the page to fully load

    # Activate the tweet box
    try:
        compose_box = driver.find_element(By.XPATH, "//div[@data-testid='tweetTextarea_0' and contains(@class,'public-DraftEditor-content')]")
        driver.execute_script("arguments[0].click();", compose_box)
        time.sleep(2)
    except Exception as e:
        print("Error activating tweet box:", e)
        return

    # Set the tweet text using JavaScript
    try:
        driver.execute_script("arguments[0].textContent = arguments[1];", compose_box, tweet_text)
        time.sleep(2)
    except Exception as e:
        print("Error setting tweet text via JavaScript:", e)
        return

    # Find and click the tweet button
    try:
        tweet_button = driver.find_element(By.XPATH, "//div[@data-testid='tweetButtonInline']")
        tweet_button.click()
        time.sleep(5)
    except Exception as e:
        print("Error clicking tweet button:", e)
        return



def main():
    try:
        print("Logging in...")
        login_to_twitter()
        print("Logged in")
    except Exception as e:
        print(str(e))
        exit()
    
    from databank import utils
    from databank.generate import synthesize_post
    
    content = utils.pop_from_databank()
    print('content:', content)
    print("Synthesizing post...")
    tweet_text = synthesize_post(context=content)
    print("post:", tweet_text)
    
    try:
        print("Posting...")
        post_tweet(tweet_text)
        print("Tweet posted successfully")
    except Exception as e:
        print(str(e))
    
    driver.quit()


if __name__ == "__main__":
    main()