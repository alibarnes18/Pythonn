import socket


host = "scanme.nmap.org"  
portlar = [21, 22, 80, 443, 8080, 9999]

conculsions = []

for port in portlar:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)

    durum = sock.connect_ex((host, port))

    if durum == 0:
        print(f"{host}:{port} -> Açık")
        conculsions.append(f"{port} -> Açık")
    else:
         print(f"{host}:{port} → Kapalı")
         conculsions.append(f"{port} → Kapalı")

    sock.close()

with open("scan_report.txt", "w", encoding="utf-8") as f:
    f.write("Port Tarama Raporu\n")   
    f.write("------------------\n")   
    for satir in conculsions:         
        f.write(satir + "\n")        