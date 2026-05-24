# Data — Paylaşılan Veri Dosyaları

Scriptlerin ürettiği veya okuduğu log, rapor ve wordlist dosyaları.

## Alt Klasörler

| Klasör | İçerik |
|--------|--------|
| `logs/` | `web.log`, `brute.log`, `ssh.log` |
| `reports/` | Tarama ve analiz raporları (txt, json, csv) |
| `wordlists/` | `wordlist.txt`, `hosts.txt` |

## Modül İçi Veri

- `03-file-handling/data/access.log` — dosya işleme ve regex örnekleri
- `CyberSec/network.log`, `brute.log` vb. — script çalıştırıldığında CyberSec klasöründe de oluşabilir

## Not

Bazı scriptler çıktıyı çalıştığı dizine yazar. Tutarlılık için rapor yollarını `Path(__file__).parent` ile yapılandırmanız önerilir.
