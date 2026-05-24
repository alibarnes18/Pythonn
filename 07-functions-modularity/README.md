# 07 — Fonksiyonlar ve Modülerlik

Kodu küçük, test edilebilir fonksiyonlara bölme; şifre gücü analizi örneği.

## Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `password_strength.py` | Uzunluk, büyük harf, rakam kontrolü → puan |
| `password_analyzer_advanced.py` | Özel karakter, çoklu şifre, en güçlüyü bulma |

## Çalıştırma

```bash
python password_strength.py
python password_analyzer_advanced.py
```

## Fonksiyon Yapısı

- `uzunluk_kontrol(sifre)` → bool
- `buyuk_harf_var_mi(sifre)` → bool
- `rakam_var_mi(sifre)` → bool
- `guc_hesapla(sifre)` → "Zayıf" / "Orta" / "Güçlü"

## Öğrenme Hedefi

Aynı mantığı port tarayıcı ve log analiz araçlarına taşıyarak tekrar kullanılabilir modüller oluşturmak.
