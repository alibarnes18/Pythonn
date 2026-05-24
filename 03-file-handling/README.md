# 03 — Dosya İşleme

Metin dosyalarını okuma, filtreleme ve yeni dosyaya yazma.

## Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `log_error_filter.py` | `access.log` içinden ERROR satırlarını ayıklar |
| `data/access.log` | Örnek erişim günlüğü |

## Çalıştırma

```bash
python log_error_filter.py
```

## Kavramlar

- `with open(...)` bağlam yöneticisi
- Satır satır okuma (`for line in f`)
- Alt dizinde veri dosyası (`data/access.log`)

## Not

`log_error_filter.py` henüz tamamlanmamış olabilir (sözdizimi). Tamamlarken `error.log` çıktısını aynı klasöre yazmayı hedefleyin.
