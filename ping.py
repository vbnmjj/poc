import os

ips = open('ip.txt').readlines()
for ip in ips:
    os.system(f"ping -n 1 {ip}")