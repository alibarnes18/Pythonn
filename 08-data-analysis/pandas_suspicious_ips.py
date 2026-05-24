import pandas as pd

veri = {
    "ip": ["192.168.1.1", "10.0.0.2", "172.16.0.9", "192.168.1.5", "10.0.0.5"],
    "hata_sayisi": [3, 7, 1, 9, 2],
    "port": [22, 80, 21, 22, 443]
}

df = pd.DataFrame(veri)

ortalama = df["hata_sayisi"].mean()

print("Ortalama hata: ", ortalama)

supheli = df[df["hata_sayisi"] > ortalama]

print("\nŞüpheli IP'ler:")
print(supheli)

supheli.to_csv("suspicious.csv", index=False)