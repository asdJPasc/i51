from playwright.sync_api import Playwright, sync_playwright
import time
import os
import subprocess
from datetime import date
from datetime import datetime
from colorama import init, Fore, Style
init()


subprocess.call('mode con: cols=100 lines=10', shell=True)
os.system('color 0A')

#list all web links separated with comma
urls = ['https://www.congress.gov/search?searchResultViewType=expanded&pageSort=latestAction:desc&q={%22source%22:%22legislation%22,%22type%22:%22bills%22,%22bill-status%22:%22law%22}&pageSize=25', 
        'https://www.cftc.gov/LawRegulation/CFTCStaffLetters/letters.htm?title=&field_csl_letter_year_value=2023'
       ]

#list all simplified names
names = ['Row id: 191',
         'Row id: 198'
        ]

#list all folder name
folders = ['191_screenshots', 
           '198_screenshots'
          ]

# Define the interval between capturing each screenshot (in seconds)s.
# Set 3600 sec equivalent to 1 hour.
interval = 3600

print(r"""

\n
 ______   ______     _                                         __      
/\__  _\ /\  ___\  /' \                             __        /\ \__   
\/_/\ \/ \ \ \__/ /\_, \        ____    ___   _ __ /\_\  _____\ \ ,_\  
   \ \ \  \ \___``\/_/\ \      /',__\  /'___\/\`'__\/\ \/\ '__`\ \ \/  
    \_\ \__\/\ \L\ \ \ \ \    /\__, `\/\ \__/\ \ \/ \ \ \ \ \L\ \ \ \_ 
    /\_____\\ \____/  \ \_\   \/\____/\ \____\\ \_\  \ \_\ \ ,__/\ \__\
    \/_____/ \/___/    \/_/    \/___/  \/____/ \/_/   \/_/\ \ \/  \/__/
                                                           \ \_\       
                                                            \/_/       
""")
time.sleep(4)

def accept_cookies(page):
    try:
        accept_button = page.locator('.btn-accept')
        if accept_button.is_visible():
            accept_button.click()
    except Exception as e:
        print(e)

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
                print(f"Capturing screenshot of {names[i]}...")
                page.goto(url)
                page.wait_for_load_state()
                accept_cookies(page)  # accept cookies
                time.sleep(8)
                timestamp = datetime.now().strftime("Date: %m-%d-%Y || Time: %I:%M:%S %p")
                consoleTimestamp = datetime.now().strftime("%I:%M:%S %p")
                page.evaluate(f"""
                    const timestamp = new Date().toLocaleString('en-US', {{ hour12: true }});
                    const url = document.URL;
                    const div = document.createElement('div');
                    div.style.position = 'fixed';
                    div.style.top = '0';
                    div.style.left = '0';
                    div.style.backgroundColor = 'blue';
                    div.style.padding = '5px';
                    div.style.width = '100%';
                    div.style.color = 'white';
                    div.style.fontWeight = 'bold';
                    div.style.height = 'auto';
                    div.style.zIndex = '9999999';
                    div.textContent = `{timestamp} || {names[i]}`;
                    document.body.appendChild(div);
                """)
                page.screenshot(path=f"{folder}/{filename}", full_page=True)
                print(f"Done capturing screenshot of {names[i]} at {consoleTimestamp}.\n")
            time.sleep(interval)
            
        except KeyboardInterrupt:
            break
