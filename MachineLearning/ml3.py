import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

veri = {
    "paket_boyutu": [100,150,200,8000,9500,7000,120,8800,300,9000,180,7500],
    "port":         [80,443,8080,22,21,22,80,21,443,22,8080,21],
    "sure":         [1,2,1,30,25,28,1,27,2,29,1,26],
    "etiket":       [0,0,0,1,1,1,0,1,0,1,0,1]
}

df = pd.DataFrame(veri)


X = df[["paket_boyutu", "port", "sure"]]


y = df["etiket"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = DecisionTreeClassifier()


model.fit(X_train, y_train)


tahminler = model.predict(X_test)


print("Doğruluk:", accuracy_score(y_test, tahminler))


print(classification_report(y_test, tahminler))