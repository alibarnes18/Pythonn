# Web Security — Web Uygulama Güvenliği

HTTP tabanlı keşif, SQL injection testi ve yerel Flask laboratuvar sunucusu.

## Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `ws01.py` | Dizin brute-force (admin, login, backup vb.) |
| `sqlinjection01.py` | SQLi payload listesi ile URL testi |
| `test_server.py` | Flask ile savunmasız test API (`/search`, `/comment`) |

## Çalıştırma

```bash
pip install requests flask

# Test sunucusu (ayrı terminal)
python test_server.py

# Dizin taraması
python ws01.py

# SQLi testi (yalnızca kendi lab ortamınızda)
python sqlinjection01.py
```

## Kavramlar

- HTTP status kodları (200, 401, 404)
- Gizli dizin keşfi
- SQL injection payload mantığı

## Uyarı

`test_server.py` kasıtlı olarak güvensizdir; internete açmayın. SQLi ve dizin taraması yalnızca izinli ortamlarda kullanılmalıdır.
