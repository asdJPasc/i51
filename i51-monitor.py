import requests
from bs4 import BeautifulSoup
import time
import winsound
from datetime import datetime

# Set the URLs of the websites you want to monitor
urls = {'191 - Congress': 'https://www.congress.gov/search?searchResultViewType=expanded&pageSort=latestAction:desc&q={%22source%22:%22legislation%22,%22type%22:%22bills%22,%22bill-status%22:%22law%22}&pageSize=25', 
        '192 - Federal Register': 'https://www.federalregister.gov/documents/current', 
        '195 - CFPB': 'https://www.consumerfinance.gov/enforcement/actions/?title=&statuses=post-order-post-judgment&from_date=2023-01-01&to_date=2023-12-31',
        '198 - CFTC': 'https://www.cftc.gov/LawRegulation/CFTCStaffLetters/letters.htm?title=&field_csl_letter_year_value=2023',
        '890 - DOF': 'https://webproxy.to/browse.php?u=https%3A%2F%2Fdof.gob.mx%2F&b=20&f=norefer',
        '960': 'http://www4.planalto.gov.br/legislacao/portal-legis/resenha-diaria/2023-resenha-diaria/marco-resenha-diaria'
       }

# Set the CSS selector of the element to monitor
selector = '#main, .wrapper, #content_main, .view-content, #tdcontent, #content'
# Set the CSS selectors of the elements to exclude
exclude_selectors = ['.no-monitor', '#another-element']

# Set checking interval in seconds
interval = 1


checksums = {name: None for name in urls}


while True:
    time.sleep(interval)

    for name, url in urls.items():
        response = requests.get(url)
        content = response.content
        soup = BeautifulSoup(content, 'html.parser')

        for exclude_selector in exclude_selectors:
            for tag in soup.select(exclude_selector):
                tag.decompose()

        element = soup.select_one(selector)
        if element is not None:
            element_hash = hash(element.prettify())
        else:
            element_hash = None

        if element_hash is not None and element_hash != checksums[name]:
            winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)
            timestamp = datetime.now().strftime('%I:%M:%S %p')
            print(f"The monitored url has changed for Row ID: {name} at {timestamp}.")
            checksums[name] = element_hash
