import requests

url = "https://httpbin.org/status/404"

cevap = requests.get(url)

if cevap.status_code == 200:
    print("Site Açık")
elif cevap.status_code == 404:
    print("Sayfa bulunamadı!")
else:
    print("farklı bir durum: {status_code}")