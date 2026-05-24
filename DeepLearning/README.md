# Deep Learning — PyTorch

Basit tam bağlı (fully connected) sinir ağı ile tensor işlemleri.

## Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `dl1.py` | `nn.Sequential`: Linear → ReLU → Linear → Sigmoid |
| `dl2.py` | Geliştirilmiş ağ / eğitim döngüsü örneği |

## Çalıştırma

```bash
pip install torch
python dl1.py
python dl2.py
```

## Kavramlar

- `torch.tensor` ve boyutlar
- `nn.Linear`, `nn.ReLU`, `nn.Sigmoid`
- İleri geçiş (forward pass) çıktısı

## Sonraki Adım

Spam veya phishing sınıflandırıcısı için `MachineLearning/ml3.py` veri setini PyTorch `Dataset` formatına dönüştürün.
