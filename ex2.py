#portlar = [21, 22, 80, 443, 8080] listesi verilmiş
#Her port için döngü kur
#21 → "FTP - Riskli!"
#22 → "SSH - Dikkatli kullan"
#80 veya 443 → "HTTP/HTTPS - Normal"
#Diğerleri → "Bilinmeyen port"

ports = [21, 22, 80, 443, 8080]
for port in ports:
    if port == 21:
        print("FTP - Riskli!")
    elif port == 22:
        print("SSH - Dikkatli kullan")
    elif port == 80 or port == 443:
        print("HTTP/HTTPS - Normal")
    else:
        print("Bilinmeyen port")