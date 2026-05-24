# Machine Learning — Saldırı Sınıflandırma

Scikit-learn `DecisionTreeClassifier` ile ağ trafiği / port verisinden etiket tahmini.

## Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `Mldi.py` | Minimal Decision Tree (port + paket boyutu) |
| `Ml2.py` | Benzer basit model örneği |
| `ml3.py` | Train/test split, accuracy, classification report |

## Çalıştırma

```bash
pip install numpy pandas scikit-learn
python ml3.py
```

## Özellikler (ml3.py)

- `paket_boyutu`, `port`, `sure` → `etiket` (0 normal / 1 saldırı)
- `train_test_split`, `accuracy_score`

## İlişkili Modüller

- `CyberSec/Cyber002.py` — log verisinden ML pipeline
- `DeepLearning/` — PyTorch ile derin model
