from sklearn.tree import DecisionTreeClassifier
import numpy as np

X = [
    [100, 80],
    [150, 443],
    [200, 8080],
    [8000, 22],
    [9500, 21],
    [7000, 22],
]

y = [0, 0, 0, 1, 1, 1]  

model = DecisionTreeClassifier()

model.fit(X, y)

test = [
    [120, 80],
    [8800, 21],
    [300, 443]
]


tahminler = model.predict(test)

for veri, sonuc in zip(test, tahminler):
    if sonuc == 0:
        durum = "Normal"
    else:
        durum = "Saldırı"
    
    print(f"{veri} -> {durum}")