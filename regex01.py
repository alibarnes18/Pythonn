import re

metin = "ERROR 10.0.0.2 login failed"
ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", metin)
print(ip)