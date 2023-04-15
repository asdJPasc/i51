from playwright.sync_api import Playwright, sync_playwright
import time
import os
from datetime import date
from datetime import datetime

#list all web links separated with comma
urls = ['https://www.federalregister.gov/documents/current', 
        'https://www.consumerfinance.gov/enforcement/actions/?title=&statuses=post-order-post-judgment&from_date=2023-01-01&to_date=2023-12-31', 
        'https://www.cftc.gov/LawRegulation/CFTCStaffLetters/letters.htm?title=&field_csl_letter_year_value=2023']

#list all folder name
folders = ['./192_screenshots', 
           './195_screenshots', 
           './198_screenshots']

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
                timestamp = datetime.now().strftime("Date: %m-%d-%Y || Time: %I:%M:%S %p")
                page.evaluate(f"""
                    const timestamp = new Date().toLocaleString('en-US', {{ hour12: true }});
                    const url = document.URL;
                    const div = document.createElement('div');
                    div.style.position = 'absolute';
                    div.style.top = '0';
                    div.style.left = '0';
                    div.style.backgroundColor = 'white';
                    div.style.padding = '5px';
                    div.style.width = '100%';
                    div.style.fontWeight = 'bold';
                    div.style.height = 'auto';
                    div.style.zIndex = '9999';
                    div.textContent = `{timestamp} || {url}`;
                    document.body.appendChild(div);
                """)
                page.screenshot(path=f"{folder}/{filename}", full_page=True)
                
            time.sleep(interval)

        except KeyboardInterrupt:
            break
