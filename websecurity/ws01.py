import requests

def dir_brute(hedef, dizinler, dosya):

    with open(dosya, "w", encoding="utf-8") as f:

     for dizin in dizinler:
        url = f"{hedef}/{dizin}"

        try:
             cevap = requests.get(url, timeout=5)

             if cevap.status_code == 200:
                sonuc= f"[+] Bulundu: {url}"

                print(sonuc)
                f.write(sonuc + "\n")

             else:
                print(f"[-] Yok: {url} ({cevap.status_code})")

        except requests.exceptions.RequestException as hata:
            print(f"[!] Hata: {url} -> {hata}")


hedef = "http://httpbin.org"

dizinler = [
    "admin",
    "login",
    "backup",
    "uploads",
    "config",
    "test",
    "db",
    "api",
    "panel"
]

dir_brute(hedef, dizinler, "dir_report.txt")