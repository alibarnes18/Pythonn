# 04 — Regular Expressions (Regex)

Log ve metinlerden IP, e-posta ve URL gibi kalıpları çıkarma.

## Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `regex_basics.py` | `re` modülüne giriş |
| `regex_ip_single.py` | Tek satırdan IP çıkarma |
| `regex_patterns.py` | Ek regex kalıpları |
| `ip_extract_from_lines.py` | Liste halindeki log satırlarından IP |
| `log_analyzer_regex.py` | `access.log` okuyup IP sayımı ve rapor |

## Çalıştırma

```bash
python regex_ip_single.py
python log_analyzer_regex.py
```

## Örnek Kalıp

```python
re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", metin)
```

## Bağımlılık

`log_analyzer_regex.py`, log dosyasını `03-file-handling/data/access.log` konumundan okur.
