from sklearn.tree import DecisionTreeClassifier
import numpy as np


X = [
    [100, 80],   
    [200, 443],  
    [9000, 22],  
    [8500, 21],  
]

y = [0, 0, 1, 1]  

model = DecisionTreeClassifier()
model.fit(X, y)  

tahmin = model.predict([[9500, 22]])  
print(tahmin)  