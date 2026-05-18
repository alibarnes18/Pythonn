import re

hata_sayac = {}

with open("ssh.log", "r") as f:
    for line in f:
        if "Failed password" in line:
            ip = re.search(r"\d{1,3}(?:\.\d{1,3}){3}", line)

            if ip:
                ip_adress = ip.group()
                parcalar = line.split()
                kullanici = parcalar[parcalar.index("for") + 1]

                if ip_adress in hata_sayac:
                    hata_sayac[ip_adress]["sayi"] += 1
                else:
                    hata_sayac[ip_adress] = {"sayi": 1, "kullanici": kullanici}

with open("ssh_blocked.txt", "w", encoding="utf-8") as f:
    for ip, bilgi in hata_sayac.items():
        if bilgi["sayi"] >= 3:
            print(f"{ip} → {bilgi['sayi']} deneme → hedef: {bilgi['kullanici']}")
            f.write(f"{ip} → {bilgi['sayi']} deneme → hedef: {bilgi['kullanici']}\n")