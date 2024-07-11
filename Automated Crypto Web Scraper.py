
# Automated Crypto Web Scraper

from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
import time
from datetime import datetime
    

def automated_crypto_pull():
    url = 'https://coinmarketcap.com/currencies/bitcoin/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    crypto_name = soup.find('span', class_ = 'sc-d1ede7e3-0 bEFegK').contents[0]
    crypto_price = soup.find('span', class_ = 'sc-d1ede7e3-0 fsQm base-text').text
    final_price = crypto_price.replace('$', '')

    date_time = datetime.now()
    crypto_dict = {'Crypto Name': crypto_name,
                   'Price': final_price,
                   'TimeStamp': date_time}

    df = pd.DataFrame([crypto_dict])

    path = r'C:\Users\garri\OneDrive\Desktop\Python Notes\Crypto Web Puller\Crypto_Automated_Pull.csv'

    if os.path.exists(path):
        df.to_csv(path, mode = 'a', header = False, index = False)
    else:
        df.to_csv(path, index = False)
    
    print(df)
  
while True:
    automated_crypto_pull()
    time.sleep(10)