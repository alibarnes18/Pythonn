import re

satirlar = [
    "INFO 192.168.1.1 login success",
    "ERROR 10.0.0.2 login failed",
    "INFO 192.168.1.5 logout",
    "ERROR 172.16.0.9 login failed",
]

for satir in satirlar:
    ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", satir)
    if ip:
        print(ip.group())


suspects = []

for satir in satirlar:
    if "ERROR" in satir:
        ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", satir)
        if ip:
            suspects.append(ip.group())

print(f"Suspects IP: {suspects}" )