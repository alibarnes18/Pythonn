# 05 — HTTP İstekleri ve Web

`requests` kütüphanesi ile web sunucularına istek atma ve yanıt analizi.

## Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `get_status_headers.py` | GET isteği, status code ve header yazdırma |
| `request_basics.py` | `requests` temel kullanımı |
| `http_header_analyzer.py` | URL için header analizi fonksiyonu |
| `networking_requests.py` | Ağ / HTTP alıştırmaları |

## Çalıştırma

```bash
pip install requests
python get_status_headers.py
python http_header_analyzer.py
```

## Kavramlar

- HTTP status kodları (200, 404, 500)
- Response headers (`Server`, `Content-Length`)
- Timeout ve istisna yönetimi

## Mini Proje Fikri

Verilen URL için status code, sunucu bilgisi ve içerik uzunluğunu tek raporda toplayan bir “Mini Web Scanner” yazın.
