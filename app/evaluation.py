import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split


df = pd.read_csv("data/features.csv")

X = df.drop(columns="label")
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

model = RandomForestClassifier(
    n_estimators=100, random_state=42
)

model.fit(X_train, y_train)
prediction = model.predict(X_test)

print("\nClassification Report:")
print(classification_report(y_test, prediction))

print("Confusion Matrix:")
print(confusion_matrix(y_test, prediction))