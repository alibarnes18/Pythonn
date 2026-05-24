#baglantilar = [
#    {"ip": "192.168.1.5", "port": 22},
#    {"ip": "10.0.0.2",    "port": 80},
#    {"ip": "192.168.1.5", "port": 443},
#    {"ip": "172.16.0.9",  "port": 21},
#    {"ip": "10.0.0.2",    "port": 22},
#]
Görevin:

#Kaç farklı IP bağlanmış? → set kullan
#Port 22'ye bağlanan IP'leri listele
#En çok hangi port kullanılmış? (manuel say, hazır fonksiyon yok)

#Beklenen çıktı:
#Farklı IP sayısı: 3
#Port 22'ye bağlananlar: ['192.168.1.5', '10.0.0.2']
#En çok kullanılan port: 22 (2 kez)

connections = [
    {"ip": "192.168.1.5", "port": 22},
    {"ip": "10.0.0.2",    "port": 80},
    {"ip": "192.168.1.5", "port": 443},
    {"ip": "172.16.0.9",  "port": 21},
    {"ip": "10.0.0.2",    "port": 22},
]

ipler = set()
for b in connections:
    ipler.add(b["ip"])
print(f"Farklı IP sayısı: {len(ipeler)}")

port22_ipler = []
for b in connections:
    if b["port"] == 22:
        port22_ipler.append(b["ip"])
print(f"Port 22'ye bağlananlar: {port22_ipler}")

sayac = {}
for bb in connections:
    port = b["port"]
    if port in sayac:
        sayac[port] += 1
        else:
            sayac[port] = 1

max_port = max(sayac, key=sayac.get)
print(f"En çok kullanılan port: {max_port} ({sayac[max_port]} kez)")