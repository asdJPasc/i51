<<<<<<< HEAD
from playwright.sync_api import Playwright, sync_playwright
from playwright._impl._api_types import TimeoutError
import time
import os
import subprocess
import ctypes
from datetime import date
from datetime import datetime
from colorama import init, Fore, Style
import binascii
init()

winTitle = b'49353120536372697074'
decodeString = '446576656c6f7065642062793a204a50617363'
decoded_hex = binascii.unhexlify(winTitle)
decoded_string = decoded_hex.decode()
decoded_hex = binascii.unhexlify(decodeString)
decodedstring = decoded_hex.decode()
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleTitleW(decoded_string)
subprocess.call('mode con: cols=80 lines=10', shell=True)
os.system('color 09')

#Please be aware that using the script is at your own risk and 
# the creator of the script is not liable for any damages that may result from using it.

#list all url in ORDER separated with comma same with simplified and folder names. 
#BE CAREFUL WITH THE FORMAT TO AVOID ERRORS
urls = ['https://www.congress.gov/search?searchResultViewType=expanded&pageSort=latestAction:desc&q={%22source%22:%22legislation%22,%22type%22:%22bills%22,%22bill-status%22:%22law%22}&pageSize=25', 
        'https://www.federalregister.gov/documents/current', 
        'https://www.consumerfinance.gov/enforcement/actions/?title=&statuses=post-order-post-judgment&from_date=2023-01-01&to_date=2023-12-31',
        'https://www.cftc.gov/LawRegulation/CFTCStaffLetters/letters.htm?title=&field_csl_letter_year_value=2023',
        'http://dof.gob.mx',
        'https://www.bcb.gov.br/estabilidadefinanceira/buscanormas?dataInicioBusca=25%2F03%2F2023&dataFimBusca=31%2F12%2F2023&tipoDocumento=Resolu%C3%A7%C3%A3o%20BCB',
        'https://www.bcb.gov.br/estabilidadefinanceira/buscanormas?dataInicioBusca=25%2F03%2F2023&dataFimBusca=31%2F12%2F2023&tipoDocumento=Resolu%C3%A7%C3%A3o%20Conjunta',
        'http://www4.planalto.gov.br/legislacao/portal-legis/resenha-diaria/2023-resenha-diaria/marco-resenha-diaria',
        'https://www.bcb.gov.br/estabilidadefinanceira/buscanormas?dataInicioBusca=01%2F01%2F2023&dataFimBusca=31%2F12%2F2023&tipoDocumento=Resolu%C3%A7%C3%A3o%20CMN'
       ]

#Simplified name (will reflect to the screenshot timestamp)
names = ['Row id: 191',
         'Row id: 192',
         'Row id: 195',
         'Row id: 198',
         'Row id: 890',
         'Row id: 951 - BCB',
         'Row id: 951 - Conjunta',
         'Row id: 960',
         'Row id: 961 - CMN'
        ]

#Folder name
folders = ['191_screenshots', 
           '192_screenshots', 
           '195_screenshots',
           '198_screenshot',
           '890_screenshot',
           '951-bcb_screenshot',
           '951-conjunta_screenshot',
           '960_screenshot',
           '961_screenshot'
          ]

#To specify the output file name of the screenshot
shift = '3rd'
emp_id = 'i51'        

# Define the interval between capturing each screenshot (in seconds)s.
# Default interval is 1800 for 30mins 2 cycles per hour
interval = 1800

print(rf"""

 ______   ______     _                                         __      
/\__  _\ /\  ___\  /' \                             __        /\ \__   
\/_/\ \/ \ \ \__/ /\_, \        ____    ___   _ __ /\_\  _____\ \ ,_\  
   \ \ \  \ \___``\/_/\ \      /',__\  /'___\/\`'__\/\ \/\ '__`\ \ \/  
    \_\ \__\/\ \L\ \ \ \ \    /\__, `\/\ \__/\ \ \/ \ \ \ \ \L\ \ \ \_ 
    /\_____\\ \____/  \ \_\   \/\____/\ \____\\ \_\  \ \_\ \ ,__/\ \__\
    \/_____/ \/___/    \/_/    \/___/  \/____/ \/_/   \/_/\ \ \/  \/__/
                                 {decodedstring}       \ \_\       
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

log_file = open("log.txt", "a")        

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=True)

    while True:
        try:
            for i, url in enumerate(urls):
                folder = folders[i]
                os.makedirs(folder, exist_ok=True)
                count = len(os.listdir(folder))

                #To include another extension in the filename, you can copy one of the "elif" statements added above the "else" statement 
                if "BCB" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-BCB.png"
                elif "Conjunta" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Conjunta.png"
                elif "litreleases" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-LR.png"
                elif "de-recursos-de-terceiros" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Administração-de-Recursos.png"       
                elif "opinions" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Comm Opinion.png"
                elif "friactions" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-AA.png"  
                elif "admin" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-AP.png"    
                elif "codigo-de-etica" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Código-de-Ética.png"
                elif "atividades-conveniadas" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Atividades-Conveniadas.png"
                elif "servicos-qualificados" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Serviços-Qualificados.png"
                elif "certificacao" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-certificacao.png"
                elif "negociacao-de-instrumentos-financeiros" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Negociação-de-Instrumentos-Financeiros.png" 
                elif "ofertas-publicas" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Ofertas-Públicas.png"                                                       
                else:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}.png"

                page = browser.new_page()
                print(f"Capturing screenshot of {names[i]}...")
                retry = True
                while retry:
                    try:
                        page.goto(url)
                        page.wait_for_load_state()
                        accept_cookies(page)
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
                        print(f"Screenshot of {names[i]} taken at {consoleTimestamp} has been saved.\n")
                        log_file.write(f"Screenshot of {names[i]} taken at {consoleTimestamp} has been saved.\n")
                        retry = False
                
                    except TimeoutError:
                        print(f"Timeout occurred while loading the page: {url}. Retrying...")
                        log_file.write(f"Timeout occurred while loading the page: {url}. Retrying...\n")
                        continue     
                page.close()
            time.sleep(interval)    
        except KeyboardInterrupt:
            break
=======
from playwright.sync_api import Playwright, sync_playwright
from playwright._impl._api_types import TimeoutError
import time
import os
import subprocess
import ctypes
from datetime import date
from datetime import datetime
from colorama import init, Fore, Style
import binascii
init()

winTitle = b'49353120536372697074'
decodeString = '446576656c6f7065642062793a204a50617363'
decoded_hex = binascii.unhexlify(winTitle)
decoded_string = decoded_hex.decode()
decoded_hex = binascii.unhexlify(decodeString)
decodedstring = decoded_hex.decode()
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleTitleW(decoded_string)
subprocess.call('mode con: cols=80 lines=10', shell=True)
os.system('color 09')

#list all url in ORDER separated with comma same with simplified and folder names. 
#BE CAREFUL WITH THE FORMAT TO AVOID ERRORS
urls = ['https://www.congress.gov/search?searchResultViewType=expanded&pageSort=latestAction:desc&q={%22source%22:%22legislation%22,%22type%22:%22bills%22,%22bill-status%22:%22law%22}&pageSize=25', 
        'https://www.federalregister.gov/documents/current', 
        'https://www.consumerfinance.gov/enforcement/actions/?title=&statuses=post-order-post-judgment&from_date=2023-01-01&to_date=2023-12-31',
        'https://www.cftc.gov/LawRegulation/CFTCStaffLetters/letters.htm?title=&field_csl_letter_year_value=2023',
        'http://dof.gob.mx',
        'https://www.bcb.gov.br/estabilidadefinanceira/buscanormas?dataInicioBusca=25%2F03%2F2023&dataFimBusca=31%2F12%2F2023&tipoDocumento=Resolu%C3%A7%C3%A3o%20BCB',
        'https://www.bcb.gov.br/estabilidadefinanceira/buscanormas?dataInicioBusca=25%2F03%2F2023&dataFimBusca=31%2F12%2F2023&tipoDocumento=Resolu%C3%A7%C3%A3o%20Conjunta',
        'http://www4.planalto.gov.br/legislacao/portal-legis/resenha-diaria/2023-resenha-diaria/marco-resenha-diaria',
        'https://www.bcb.gov.br/estabilidadefinanceira/buscanormas?dataInicioBusca=01%2F01%2F2023&dataFimBusca=31%2F12%2F2023&tipoDocumento=Resolu%C3%A7%C3%A3o%20CMN'
       ]

#Simplified name (will reflect to the screenshot timestamp)
names = ['Row id: 191',
         'Row id: 192',
         'Row id: 195',
         'Row id: 198',
         'Row id: 890',
         'Row id: 951 - BCB',
         'Row id: 951 - Conjunta',
         'Row id: 960',
         'Row id: 961 - CMN'
        ]

#Folder name
folders = ['191_screenshots', 
           '192_screenshots', 
           '195_screenshots',
           '198_screenshot',
           '890_screenshot',
           '951-bcb_screenshot',
           '951-conjunta_screenshot',
           '960_screenshot',
           '961_screenshot'
          ]

#To specify the output file name of the screenshot
shift = '3rd'
emp_id = 'i51'        

# Define the interval between capturing each screenshot (in seconds)s.
# Default interval is 1800 for 30mins 2 cycles per hour
interval = 1800

print(rf"""
 ______   ______     _                                         __      
/\__  _\ /\  ___\  /' \                             __        /\ \__   
\/_/\ \/ \ \ \__/ /\_, \        ____    ___   _ __ /\_\  _____\ \ ,_\  
   \ \ \  \ \___``\/_/\ \      /',__\  /'___\/\`'__\/\ \/\ '__`\ \ \/  
    \_\ \__\/\ \L\ \ \ \ \    /\__, `\/\ \__/\ \ \/ \ \ \ \ \L\ \ \ \_ 
    /\_____\\ \____/  \ \_\   \/\____/\ \____\\ \_\  \ \_\ \ ,__/\ \__\
    \/_____/ \/___/    \/_/    \/___/  \/____/ \/_/   \/_/\ \ \/  \/__/
                                 {decodedstring}       \ \_\       
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

log_file = open("log.txt", "a")        

with sync_playwright() as playwright:
    browser = playwright.firefox.launch(headless=True)

    while True:
        try:
            for i, url in enumerate(urls):
                folder = folders[i]
                os.makedirs(folder, exist_ok=True)
                count = len(os.listdir(folder))

                #To include another extension in the filename, you can copy one of the "elif" statements added above the "else" statement 
                if "BCB" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-BCB.png"
                elif "Conjunta" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Conjunta.png"
                elif "litreleases" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-LR.png"
                elif "de-recursos-de-terceiros" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Administração-de-Recursos.png"       
                elif "opinions" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Comm Opinion.png"
                elif "friactions" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-AA.png"  
                elif "admin" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-AP.png"    
                elif "codigo-de-etica" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Código-de-Ética.png"
                elif "atividades-conveniadas" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Atividades-Conveniadas.png"
                elif "servicos-qualificados" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Serviços-Qualificados.png"
                elif "certificacao" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-certificacao.png"
                elif "negociacao-de-instrumentos-financeiros" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Negociação-de-Instrumentos-Financeiros.png" 
                elif "ofertas-publicas" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Ofertas-Públicas.png"                                                       
                else:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}.png"

                page = browser.new_page()
                print(f"Capturing screenshot of {names[i]}...")
                retry = True
                while retry:
                    try:
                        page.goto(url)
                        page.wait_for_load_state()
                        accept_cookies(page)
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
                        print(f"Screenshot of {names[i]} taken at {consoleTimestamp} has been saved.\n")
                        log_file.write(f"Screenshot of {names[i]} taken at {consoleTimestamp} has been saved.\n")
                        retry = False
                
                    except TimeoutError:
                        print(f"Timeout occurred while loading the page: {url}. Retrying...")
                        log_file.write(f"Timeout occurred while loading the page: {url}. Retrying...\n")
                        continue     
                page.close()
            time.sleep(interval)    
        except KeyboardInterrupt:
            break
>>>>>>> master
