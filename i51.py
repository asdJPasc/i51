from playwright.sync_api import Playwright, sync_playwright
import time
import os
from datetime import date
from datetime import datetime

urls = ['https://www.google.com', 'https://www.facebook.com', 'https://www.twitter.com']

folders = ['./google_screenshots', './facebook_screenshots', './twitter_screenshots']

# Define the interval between capturing each screenshot (in seconds)s
interval = 60

with sync_playwright() as playwright:

    counter = 10
    browser = playwright.firefox.launch(headless=True)

    while True:
        try:
            for i, url in enumerate(urls):
                folder = folders[i]
                os.makedirs(folder, exist_ok=True)
                count = len(os.listdir(folder))
                filename = f"{date.today().strftime('%m-%d')}-3rd_i51-{count+1}.png"
                page = browser.new_page()
                page.goto(url)
                page.wait_for_load_state()
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                page.evaluate(f"""
                    const timestamp = new Date().toLocaleString();
                    const url = document.URL;
                    const div = document.createElement('div');
                    div.style.position = 'absolute';
                    div.style.top = '0';
                    div.style.left = '0';
                    div.style.backgroundColor = 'white';
                    div.style.padding = '5px';
                    div.style.zIndex = '9999';
                    div.textContent = `{timestamp} - {url}`;
                    document.body.appendChild(div);
                """)
                page.screenshot(path=f"{folder}/{filename}", full_page=True)
                
            time.sleep(interval)

        except KeyboardInterrupt:
            break
