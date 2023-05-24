from playwright.sync_api import Playwright, sync_playwright
from playwright._impl._api_types import TimeoutError
from datetime import date
from datetime import datetime
import time
import os
import subprocess
import ctypes
import binascii

winTitle = b'49353120536372697074'
decodeString = '446576656c6f7065642062793a204a50617363'
decoded_hex = binascii.unhexlify(winTitle)
decoded_string = decoded_hex.decode()
decoded_hex = binascii.unhexlify(decodeString)
decodedstring = decoded_hex.decode()
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleTitleW(decoded_string)
subprocess.call('mode con: cols=80 lines=10', shell=True)

#list all url in ORDER separated with comma same with simplified and folder names. 
#BE CAREFUL WITH THE FORMAT TO AVOID ERRORS
urls = [''
       ]

#Simplified name (will reflect to the screenshot timestamp)
names = [''
        ]

#Folder name
folders = [''
          ]

#specify your shift and emp_id for the output file name of the screenshot
shift = '3rd'
emp_id = 'i51'        
interval = 360 # Default interval is 1800 for 30mins 2 cycles per hour

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
time.sleep(3)

#custom step for each row id before capturing screenshot
def custom_step(page):
    try: 
        tap_year = page.locator('a[alt="year/2023"]') #219 fix
        #Row id 213 search 100-04
        searchFilter = page.locator('input[data-drupal-selector="edit-combine"]')
        searchBtn = page.locator('input[data-drupal-selector="edit-submit-dlv-transmittals"]')

        # Row id 202 input > search > click file date function
        search_input = page.locator('input[data-drupal-selector="edit-body-value"]')
        search_button = page.locator('input[data-drupal-selector="edit-submit-regulations-section"]')
        file_date_button = page.locator('a:has-text("File Date")')  

        cvm_locator = page.locator('input#resolucoes.toggleNext[type="checkbox"]')
        showallButton = page.query_selector('.govuk-accordion__show-all') #Row id 0019 Show all button auto click

        if tap_year.is_visible():
             tap_year.click()

        if searchFilter.is_visible() and searchBtn.is_visible():
            searchFilter.fill("100-04")
            searchBtn.click()     

        if showallButton is not None and button.is_visible():
           showallButton.click()

        if search_input.is_visible() and search_button.is_visible() and file_date_button.is_visible():
             search_input.fill("HB-1-3555")
             search_button.click()
             time.sleep(2)
             file_date_button.click()

        if cvm_locator.is_visible():
             cvm_locator.click()    

    except Exception as e:
        print(e)        

log_file = open("log.txt", "a")        

with sync_playwright() as playwright:
    browser = playwright.firefox.launch_persistent_context(headless=True, user_data_dir='DO NOT DELETE', accept_downloads=False) #cache files for accept cookies

    while True:
        try:
            for i, url in enumerate(urls):
                folder = folders[i]
                os.makedirs(folder, exist_ok=True)
                count = len(os.listdir(folder))

                #To include another extension in the filename, you can copy one of the "elif" statements 
                # added above the "else" statement
                #FILE NAME EXTENSION
                
                #0001 start
                if "gov.uk/new/uksi" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-SI.png"  
                elif "guidance-and-regulation?" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Guidance and regulation.png"      
                elif "policy-papers-and-consultations" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Policy papers and consultations.png"       
                #0001 end

                #0007 start
                elif "whatsnew#tab-content-1" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-CRR.png"   
                elif "whatsnew#tab-content-3" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Solvency II.png"            
                #0007 end

                #0019 start
                elif "vat-accounting" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-VAT Accounting.png"  
                elif "vat-annual-accounting-system" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-VAT Annual Accounting Scheme.png"      
                elif "vat-assessments-and-error-correction" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-VAT Assessments and Error Correction.png"           
                elif "vat-bad-debt-relief" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-vat-bad-debt-relief.png"
                #0019 end

                #0219 start
                elif "opinion-letters" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-OLS.png"   
                elif "field-assistance-bulletins" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-FAB.png"            
                #0219 end

                #951
                elif "318" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Content.png"
                elif "Conjunta" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Conjunta.png"
                elif "BCB" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-BCB.png"    
                #951

                #1003
                elif "de-recursos-de-terceiros" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-Administração-de-Recursos.png"     
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
                #1003

                #0221 start
                elif "M26_4.asp" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-m26-4.png"   
                elif "pam26_7.asp" in url:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}-pamphlet26-7.png"            
                #0221 end
                
                #Default file naming                                                            
                else:
                    filename = f"{date.today().strftime('%m-%d')}-{shift}_{emp_id}-{count+1}.png"

                page = browser.new_page()
                print(f"Capturing screenshot of {names[i]}...")
                retry = True
                while retry:
                    try:
                        page.goto(url)
                        page.wait_for_load_state()
                        custom_step(page)
                        time.sleep(10)
                        timestamp = datetime.now().strftime("Date: %m-%d-%Y || Time: %I:%M:%S %p")
                        consoleTimestamp = datetime.now().strftime("%I:%M:%S %p")
                        page.evaluate(f"""
                            const timestamp = new Date().toLocaleString('en-US', {{ hour12: true }});
                            const url = document.URL;
                            const div = document.createElement('div');
                            div.style.position = 'absolute';
                            div.style.top = '0';
                            div.style.left = '0';
                            div.style.backgroundColor = 'blue';
                            div.style.padding = '5px';
                            div.style.width = '100%';
                            div.style.color = 'white';
                            div.style.fontWeight = 'bold';
                            div.style.height = 'auto';
                            div.style.zIndex = '9999999';
                            div.textContent = `{timestamp} || {names[i]} || {url}`;
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
