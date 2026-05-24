# Network Security — Ağ Güvenliği

Keşif ve bilgi toplama: subdomain, DNS, servis banner ve CVE sorgulama.

## Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `ns01.py` | Subdomain enumeration (`socket.gethostbyname`) |
| `ns02.py` | DNS kayıt sorgusu (`dnspython`) |
| `ns03.py` | Port banner grabbing |
| `cveanalyzer.py` | NVD API ile CVE arama |

## Çalıştırma

```bash
pip install dnspython requests
python ns01.py
python ns02.py
python ns03.py
python cveanalyzer.py
```

## Çıktı Dosyaları

Raporlar genelde `../data/reports/` altına yazılır (ör. `subdomain_report.txt`, `dns_report.txt`, `cve_report.txt`).

## Kavramlar

- DNS A/AAAA/MX kayıtları
- Servis fingerprint (banner)
- CVE ve CVSS skorları

## Uyarı

Subdomain ve port taraması yalnızca yetkili hedeflerde yapılmalıdır.
