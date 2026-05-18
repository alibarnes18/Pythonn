import re

hata_sayac = {}

with open("brute.log", "r") as f:
    for line in f:
        if "login failed" in line:
            ip = re.search(r"\d{1,3}(?:\.\d{1,3}){3}", line)

            if ip:
                ip_adresi = ip.group()

                if ip_adresi in hata_sayac:
                     hata_sayac[ip_adresi] += 1
                else:
                     hata_sayac[ip_adresi] = 1

     

with open("blocked_ips.txt", "w") as f:
    for ip, sayac in hata_sayac.items():
        if sayac >= 3:
            print(f"Brute Force: {ip} -> {sayac} deneme")
            f.write(f"Brute Force: {ip} -> {sayac} deneme\n") 