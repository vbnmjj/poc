import requests

headers = {
    'Host': 'www.cnnvd.org.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:128.0) Gecko/20100101 Firefox/128.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json;charset=utf-8',
    # 'Content-Length': '86',
    'Origin': 'https://www.cnnvd.org.cn',
    'Referer': 'https://www.cnnvd.org.cn/home/loophole',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Priority': 'u=0',
    # Requests doesn't support trailers
    # 'Te': 'trailers',
    'Connection': 'close',
}

json_data = {
    'id': '3324b37e50154040a839d1159c41fa67',
    'vulType': '0',
    'cnnvdCode': 'CNNVD-202408-596',
}

response = requests.post(
    'https://www.cnnvd.org.cn/web/cnnvdVul/getCnnnvdDetailOnDatasource',
    headers=headers,
    json=json_data,
    verify=False,
)