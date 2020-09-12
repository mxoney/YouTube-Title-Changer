import os
import time

import requests
from selenium import webdriver, common

os.system('cls && title [YouTube Title Changer]')
VIDEO_ID = input('[>] YouTube Video ID: https://www.youtube.com/watch?v=')
VIDEO_TITLE_FIELD = (
    '/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-metadata-e'
    'ditor-section/ytcp-video-metadata-editor-old/div/ytcp-animatable/ytcp-video-metadata-basics-ol'
    'd/div/div[1]/div[1]/ytcp-mention-textbox/ytcp-form-input-container/div[1]/div[2]/ytcp-mention-'
    'input/div'
)

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Disables logging
driver = webdriver.Chrome(options=options)
driver.set_window_size(800, 900)
driver.get('https://accounts.google.com/signin')

print('[!] Please log in...')
logged_in = False

while not logged_in:
    try:
        driver.find_element_by_xpath(
            '/html/body/c-wiz/div/div[2]/c-wiz/c-wiz/div/div[1]/div[3]/c-wiz/nav/ul/li[2]/a/div[2]'
        )
    except common.exceptions.NoSuchElementException:
        continue
    driver.set_window_position(-10000, 0)
    print('[!] Successfully logged in.\n')
    logged_in = True

while True:
    views = requests.get(
        f'https://www.youtube.com/watch?v={VIDEO_ID}'
    ).text.split(r'viewCount\":\"')[1].split(r'\"')[0]
    driver.get(f'https://studio.youtube.com/video/{VIDEO_ID}/edit/basic')

    # Clears the video title field
    driver.find_element_by_xpath(VIDEO_TITLE_FIELD).clear()

    # Edits the video title
    driver.find_element_by_xpath(VIDEO_TITLE_FIELD).send_keys(f'This video has {views} views')

    # Updates video settings
    driver.find_element_by_xpath(
        '/html/body/ytcp-app/ytcp-entity-page/div/div/main/div/ytcp-animatable[9]/ytcp-video-metada'
        'ta-editor-section/ytcp-video-metadata-editor-old/div/ytcp-sticky-header/ytcp-primary-actio'
        'n-bar/div/div[2]/ytcp-button[2]'
    ).click()
    print(f'[!] Updated YouTube Video title | Views: {views}')

    # For rate limit purposes waiting
    seconds = 30
    while seconds > 0:
        os.system(f'title [YouTube Title Changer] - Seconds remaining: {seconds}')
        seconds -= 1
        time.sleep(1)
    os.system('title [YouTube Title Changer] - Updating...')
