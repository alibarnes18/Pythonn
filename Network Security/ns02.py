import dns.resolver

def dns_sorgula(domain, dosya):

    kayit_tipleri = ["A", "MX", "NS"]

    with open(dosya, "w", encoding="utf-8") as rapor:


        for tip in kayit_tipleri:
            rapor.write(f"\n{tip} Kayıtları:\n")
            print(f"\n{tip} Kayıtlar:")

            try:
                sonuc = dns.resolver.resolve(domain, tip)

                for kayit in sonuc:
                    satir = f" {kayit}"
                    print(satir)
                    rapor.write(satir + "\n")
            
            except Exception as e:
                hata = f"  [!] {tip} kaydı alınamadı: {e}"
                print(hata)
                rapor.write(hata + "\n")  
domain = "google.com"
dosya = "dns_report.txt"

dns_sorgula(domain, dosya)