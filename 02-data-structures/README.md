# 02 — Veri Yapıları

Liste, sözlük (dict) ve set kullanarak ağ bağlantı verilerini analiz etme.

## Dosyalar

| Dosya | Açıklama | Kavramlar |
|-------|----------|-----------|
| `port_risk_checker.py` | Bilinen portlara göre risk mesajı | `list`, `for`, `if/elif` |
| `connection_analyzer.py` | Bağlantı kayıtlarından IP ve port istatistiği | `dict`, `set`, sayaç mantığı |

## Örnek Çıktı (`connection_analyzer.py`)

```
Farklı IP sayısı: 3
Port 22'ye bağlananlar: ['192.168.1.5', '10.0.0.2']
En çok kullanılan port: 22 (2 kez)
```

## Çalıştırma

```bash
python port_risk_checker.py
python connection_analyzer.py
```

## Not

`connection_analyzer.py` içinde sözdizimi hataları olabilir; çalıştırmadan önce `else` girintisi ve döngü değişken adlarını kontrol edin.
