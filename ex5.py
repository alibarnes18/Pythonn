#satirlar = [
#    "INFO 192.168.1.1 login success",
#    "ERROR 10.0.0.2 login failed",
#    "INFO 192.168.1.5 logout",
#    "ERROR 172.16.0.9 login failed",
#]

import re

satirlar = [
    "INFO 192.168.1.1 login success",
    "ERROR 10.0.0.2 login failed",
    "INFO 192.168.1.5 logout",
    "ERROR 172.16.0.9 login failed",
]

for satir in satirlar:
    ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', satir)
    print(ip)
