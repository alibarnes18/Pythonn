import socket
import threading
import sys
import json

if len(sys.argv) < 2:
    print("Kullanım: python portscanner.py <IP> <başlangıç_portu> <bitiş_portu>")
    sys.exit()



def port_ac_mi(ip, port, acik):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((ip, port))
        s.close()
        print(f"✅ Port {port} — AÇIK")
        acik.append(port)
    except:
        print(f"❌ Port {port} — kapalı")


def scanner(ip, portlar):
    acik = []
    threads = []

    print(f"\n{ip} taranıyor...\n")

    for port in portlar:
        t = threading.Thread(target=port_ac_mi, args=(ip, port, acik))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return acik


hedef = sys.argv[1]
portlar = range(1, 1025)

sonuc = scanner(hedef, portlar)

data = {
    "ip": hedef,
    "open_ports": sonuc
}

with open("sonuc.json", "w") as f:
    json.dump(data, f, indent=4)
print(f"\nToplam {len(sonuc)} açık port bulundu")

with open("acik_ports.txt", "w") as f:
        for port in sonuc:
            f.write(f"{port}\n")