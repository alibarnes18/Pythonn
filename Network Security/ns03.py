import socket

hedef = "scanme.nmap.org"
portlar = [21, 22, 80, 25]

with open("banner_report.txt", "w", encoding="utf-8") as rapor:

    for port in portlar:

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)

            s.connect((hedef, port))

            try:
                banner = s.recv(1024).decode().strip()

                if banner:
                    sonuc = f"[+] Port {port} → {banner}"
                else:
                    sonuc = f"[-] Port {port} → Banner alınamadı"

            except:
                sonuc = f"[-] Port {port} → Banner alınamadı"

            print(sonuc)
            rapor.write(sonuc + "\n")

            s.close()

        except Exception as e:
            hata = f"[!] Port {port} → Bağlantı başarısız ({e})"
            print(hata)
            rapor.write(hata + "\n")