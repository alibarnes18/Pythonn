# 06 — Socket ve Ağ Programlama

TCP bağlantıları, port tarama ve IP/subnet hesaplamaları.

## Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `socket_basics.py` | Basit socket bağlantısı |
| `port_check_single.py` | Tek host/port kontrolü |
| `port_scan_simple.py` | Basit port taraması, rapor dosyası |
| `port_functions.py` | Modüler port fonksiyonları |
| `port_scanner_threaded.py` | **Threading** ile hızlı port tarayıcı |
| `subnet_calculator.py` | CIDR subnet analizi (`ipaddress`) |

## Çalıştırma

```bash
# Threading port tarayıcı
python port_scanner_threaded.py <IP> <başlangıç> <bitiş>

# Örnek
python port_scanner_threaded.py scanme.nmap.org 1 100
```

## Kavramlar

- `socket.connect`, `settimeout`
- `threading.Thread` ve `join()`
- JSON/txt çıktı (`sonuc.json`, `acik_ports.txt` → `data/reports/`)

## Eğitim Notu

Threading mantığı için: [docs/port_scanner_tutorial.md](../docs/port_scanner_tutorial.md)

## Uyarı

Yalnızca izin verilen hedeflerde tarayın.
