# Bilinen tehlikeli portlar listesi
tehlikeli_portlar = [21, 22, 23, 80, 443, 3389]

# Her portu yazdır
print("Taranacak portlar:")
for port in tehlikeli_portlar:
    print(f"Port {port} taranıyor...")

# Yeni port ekle
tehlikeli_portlar.append(8080)
print(f"\nToplam {len(tehlikeli_portlar)} port var")

# En yüksek port numarasını bul
print(f"En yüksek port: {max(tehlikeli_portlar)}")

# Ekstra: Kullanıcıdan yeni bir port al ve listeye ekle
yeni_port = int(input("\nYeni bir port numarası gir: "))
tehlikeli_portlar.append(yeni_port)
print(f"Güncel port listesi: {tehlikeli_portlar}")

# Süper ekstra: 80 portu listede var mı kontrol et
if 80 in tehlikeli_portlar:
    print("80 portu listede var.")
else:
    print("80 portu listede yok.")