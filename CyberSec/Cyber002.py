import re
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

kayitlar = []

with open(r"c:\Users\alioz\Downloads\Funda. of Py\CyberSec\network.log", "r") as f:
    for line in f:
        durum = line.split()[0] 
        ip = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        port = re.search(r"\s(\d{2,5})\s", line)

        if ip and port:
            kayitlar.append({
                "durum": durum,
                "ip": ip.group(),
                "port": int(port.group().strip())
            })

for k in kayitlar:
    print(k)
   

df = pd.DataFrame(kayitlar)

print(df.head())
print("\nHata sayıları:")
print(df[df["durum"] == "ERROR"]["ip"].value_counts())

df["etiket"] = df["durum"].apply(lambda x: 1 if x == "ERROR" else 0)

X = df[["port"]].values
y = df["etiket"].values

model = DecisionTreeClassifier()
model.fit(X, y)

test = [[22], [80], [21], [443]]
tahminler = model.predict(test)

for port, sonuc in zip(test, tahminler):
    durum = "Şüpheli" if sonuc == 1 else "Normal"
    print(f"Port {port[0]} → {durum}")


with open(r"c:\Users\alioz\Downloads\Funda. of Py\CyberSec\final_report.txt", "w", encoding="utf-8") as f:
    f.write("Network Anomaly Report\n")
    f.write("======================\n\n")

    f.write("Şüpheli IP'ler\n")
    hata_sayilari = df[df["durum"] == "ERROR"]["ip"].value_counts()
    for ip, sayi in hata_sayilari.items():
        f.write(f"{ip} -> {sayi} hata\n")

    f.write("\Port Analizi:\n")
    for port, sonuc in zip(test, tahminler):
        durum = "Şüpheli" if sonuc == 1 else "Normal"
        f.write(f"Port {port[0]} -> {durum}\n")


print("final_report.txt oluşturuldu ✅")