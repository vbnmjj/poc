import requests
import time
def spider(page):
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://www.cnnvd.org.cn',
        'Referer': 'https://www.cnnvd.org.cn/home/loophole',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    }

    json_data = {
        'pageIndex': page,  # 页码
        'pageSize': 50, # 每页数量
        'keyword': '',  ## 漏洞关键字
        'hazardLevel': '',  # 危害等级 超危 高危 中危 低危
        'vulType': '',  # 漏洞类型
        'vendor': '',  # 厂商
        'product': '', # 产品
        'dateType': '', # 时间类型   更新时间"updateTime" 和 发布时间"publishTime"
        'beginupdateTime': '',
        'endupdateTime': ''
    }

    response = requests.post('https://www.cnnvd.org.cn/web/homePage/cnnvdVulList', headers=headers, json=json_data)
    record_list  = response.json()['data']['records']
    #recored_list data format
    '''
    元素
    {'id': '64fe659531234624ae514b4c5fdbc9d2', 'vulName': 'NLnet Labs Unbound 安全漏洞', 
    'cnnvdCode': 'CNNVD-202408-595',
    'cveCode': 'CVE-2024-43168', 'hazardLevel': 3, 
    'createTime': '2024-08-08', 
    'publishTime': '2024-08-07', 
    'updateTime': '2024-08-08', 
    'typeName': None, 
    'vulType': '0'},
    '''
    if record_list:
        return record_list
    # cnnvd_list = ["id", "vulName", "cnvdCode", "publishTime"]
    # with open("cnnvd.txt","a+",encoding="utf-8") as f:
    #         f.write(' '.join(cnnvd_list)+"\n")



num = 0
while num <3000:
    record_list = spider(num)
    num+=1
    if record_list:
        for unit in record_list:
            id = unit['id']
            vulName = unit['vulName']
            cnvdCode = unit['cnnvdCode']
            publishTime = unit['publishTime']
            cnnvd_list = [id, vulName, cnvdCode, publishTime]
            print(num,id, vulName, cnvdCode, publishTime)
            with open("cnnvd.txt","a+",encoding="utf-8") as f:
                f.write(''.join(cnnvd_list)+"\n")
    time.sleep(1)


