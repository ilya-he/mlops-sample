import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

os.makedirs('models', exist_ok=True)

data = load_iris()
X, y = data.data, data.target

clf = RandomForestClassifier()
clf.fit(X, y)

joblib.dump(clf, 'models/model.pkl')
print("Model trained and saved to models/model.pkl")
