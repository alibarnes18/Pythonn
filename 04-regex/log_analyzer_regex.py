import re

satirlar = [
    "INFO 192.168.1.1 login success\n",
    "ERROR 10.0.0.2 login failed\n",
    "INFO 192.168.1.5 logout\n",
     "ERROR 172.16.0.9 login failed\n",
    "ERROR 10.0.0.2 login failed\n",
     "INFO 172.16.0.9 login success\n",
]

#with open("access.log", "w") as f:
#  f.writelines(satirlar)



error_ips = []


from pathlib import Path

_LOG = Path(__file__).resolve().parent.parent / "03-file-handling" / "data" / "access.log"
with open(_LOG, "r") as f:
    for line in f:
        if "ERROR" in line :
            match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
            if match:
                error_ips.append(match.group())

unique_ips = set(error_ips)

ip_counts = {}

for ip in error_ips:
    if ip in ip_counts:
        ip_counts[ip] += 1
    else:
        ip_counts[ip] = 1

with open("report.txt", "w", encoding="utf-8") as report:
    report.write("Şüpheli IP Raporu\n")
    report.write("-----------------\n")

    for ip in unique_ips:
        report.write(f"{ip} -> {ip_counts[ip]} kez hata\n")
         
print("Hata Raporu oluşturuldu: report.txt ")

