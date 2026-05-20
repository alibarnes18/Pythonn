import dns.resolver

kayit_tipleri = ["A", "MX", "NS"]
domain = "google.com"

for tip in kayit_tipler:
    print(f"\n{tip} Kayitlar: ")
    sonuc = dns.resolver.resolve(domain, tip)