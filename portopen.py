import socket

def is_port_open(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)  # 设置超时时间为1秒
    try:
        s.connect((ip, port))
    except (socket.timeout, socket.error):
        return False
    else:
        s.close()
        return True

for ip in open("ip.txt").readlines():
    ip = ip.strip()
    port = 6379  # 替换为你想测试的端口号

    if is_port_open(ip, port):
        print(f"{ip}  Port {port}  is open")
    else:
        print(f"{ip}  Port {port}  is closed")
