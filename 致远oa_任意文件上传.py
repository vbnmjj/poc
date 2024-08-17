
from tqdm import tqdm
import requests
import warnings

import threading
warnings.filterwarnings('ignore')
def req1(url):
    path = "/seeyon/htmlofficeservlet"
    val_url1 = url+path
    try:
        response1 = requests.get(val_url1 ,verify=False,timeout=5)
        
        if response1.status_code == 200:
            print(val_url1)
    except:
        pass

urls = open("urls.txt","r").readlines()
for url in tqdm(urls):
    url = url.strip()
    req1(url)
