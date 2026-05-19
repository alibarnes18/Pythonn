import socket
import time

host = "scanme.nmap.org"
portlar = [21, 22, 23, 80, 443, 3306, 8080]

servis_map = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt"
}

baslangic = time.time()

for port in portlar:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    sonuc = sock.connect_ex((host, port))
    sock.close()

    servis = servis_map.get(port, "Bilinmeyen")

    if sonuc == 0:
        print(f" {port} ({servis}) → Açık")
    else:
        print(f" {port} ({servis}) → Kapalı")

sure = time.time() - baslangic
print(f"\nTarama süresi: {sure:.2f} saniye")