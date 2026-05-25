import requests

def xss_tara(url, payloadlar, dosya):

    with open(dosya, "w", encoding="utf-8") as f:
        for payload in payloadlar:
            cevap = requests.get(url, params={"yorum": payload})

            if payload in cevap.text and "<" in payload:
                sonuc = f"[!] XSS bulundu: {payload}"
            else:
                sonuc = f"[+] Temiz: {payload}"

            print(sonuc)
            f.write(sonuc + "\n")

url = "http://127.0.0.1:5000/comment"

payloadlar = [
    "<script>alert('XSS')</script>",
    "<img src=x onerror=alert(1)>",
    "<body onload=alert('XSS')>",
    "normal yorum"
]

xss_tara(url, payloadlar, "sonuclar.txt")