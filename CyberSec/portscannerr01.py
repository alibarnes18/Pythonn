import socket
import time

def port_tarayici(host, portlar, dosya="port_scan_report.txt"):

    servis_map = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        80: "HTTP",
        443: "HTTPS",
        3306: "MySQL",
        8080: "HTTP-Alt"
    }

    acik_portlar = []

    baslangic = time.time()

    for port in portlar:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:

            sock.settimeout(1)

            sonuc = sock.connect_ex((host, port))

        servis = servis_map.get(port, "Bilinmeyen")

        if sonuc == 0:
            print(f"{port} ({servis}) → Açık")
            acik_portlar.append(f"{port} ({servis}) → Açık")

        else:
            print(f"{port} ({servis}) → Kapalı")

    sure = time.time() - baslangic

    with open(dosya, "w", encoding="utf-8") as f:
        f.write("Port Tarama Raporu\n")
        f.write(f"Host: {host}\n")
        f.write(f"Tarama süresi: {sure:.2f} saniye\n")
        f.write("-" * 30 + "\n")

        for port in acik_portlar:
            f.write(port + "\n")

    return acik_portlar


host = "scanme.nmap.org"
portlar = [21, 22, 23, 80, 443, 3306, 8080]

aciklar = port_tarayici(host, portlar)

print("\nAçık Portlar listesi:")
print(aciklar)