# CyberSec — Siber Güvenlik Araçları

Log üretimi, analizi, brute-force tespiti, hash kırma, port tarama ve ML tabanlı raporlama.

## Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `Cyber001.py` | Örnek `network.log` oluşturur |
| `Cyber002.py` | Log + Pandas + Decision Tree ile analiz ve `final_report.txt` |
| `findlog.py` | `brute.log` örnek verisi oluşturur |
| `findlog2.py` | Brute-force IP tespiti → `blocked_ips.txt` |
| `findlog3.py` | `web.log` oluşturur |
| `finlog4.py` | Web log 401 analizi → `web_blocked.txt` |
| `findlog5.py` | `ssh.log` oluşturur |
| `findlog6.py` | SSH başarısız giriş analizi → `ssh_blocked.txt` |
| `hashlibb01.py` | MD5/SHA1 sözlük saldırısı (hash kırıcı) |
| `hashlib02.py` | Wordlist üzerinde hash döngüsü |
| `portscannerr01.py` | Socket ile port tarayıcı |
| `analyzer.py` | Scapy ile paket yakalama ve analiz |

## Çalıştırma Sırası (Log analizi zinciri)

```bash
python Cyber001.py
python findlog.py && python findlog2.py
python findlog3.py && python finlog4.py
python findlog5.py && python findlog6.py
python Cyber002.py
```

## Bağımlılıklar

```bash
pip install pandas scikit-learn scapy
```

Wordlist: `../data/wordlists/wordlist.txt`

## Uyarı

Hash kırma ve log analizi yalnızca eğitim ortamında kullanılmalıdır.
