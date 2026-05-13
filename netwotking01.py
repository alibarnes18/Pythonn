import requests

urls = [
    "https://httpbin.org/status/200",
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/403",
    "https://httpbin.org/status/500",
]




for url in urls:

    response = requests.get(url)

    status = response.status_code

    if response.status_code == 200:
        durum = "✅ Açık"
    
    elif response.status_code == 403:
        durum = "⛔ Erişim engellendi"

    elif response.status_code == 404:
        durum = "❌ Bulunamadı"

    elif response.status_code == 500:
        durum = "💥 Sunucu hatası"
    
    else:
        durum = "Bilinmeyen bir durum"

    print(f"{url} -> {durum}")