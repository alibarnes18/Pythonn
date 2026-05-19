from scapy.all import *

proto_map = {6: "TCP", 17: "UDP", 1: "ICMP"}
rapor = []

def paket_analizi(paket):
    if IP in paket:
        kaynak = paket[IP].src
        hedef = paket[IP].dst
        proto = proto_map.get(paket[IP].proto, "Diğer")

        satir = f"{kaynak} -> {hedef} | {proto}"
        print(satir)
        rapor.append(satir)


print("Dinleniyor...")
sniff(count = 10, prn = paket_analizi)

with open("trafik_raporu.txt", "w", encoding="utf-8") as f:
    f.write("Trafik Raporu\n")
    f.write("-" *30 + "\n")

    for satir in rapor:
        f.write(satir + "\n")