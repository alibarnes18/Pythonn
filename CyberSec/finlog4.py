import re

#web.log dosyasını oku
#401 failed geçen satırlardaki IP'leri say
#4 veya daha fazla hata yapan IP'leri tespit et
#Sonucu web_blocked.txt'e yaz

hata_sayac = {}

with open("web.log", "r") as f:
    for line in f:
        if "401 failed" in line:
            ip = re.search(r"\d{1,3}(?:\.\d{1,3}){3}", line)

            if ip:
                ip_adres = ip.group()

                if ip_adres in hata_sayac:
                    hata_sayac[ip_adres] += 1
                else:
                    hata_sayac[ip_adres] = 1

with open("web_blocked.txt", "w") as f:
    for ip, sayac in hata_sayac.items():
        if sayac >= 4 :
            print(f"Web Log: {ip} -> {sayac}")
            f.write(f"Web Log: {ip} -> {sayac}")
    
