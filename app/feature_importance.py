import pandas as pd
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv("data/features.csv")

X = df.drop(columns="label")
y = df["label"]

model = RandomForestClassifier(
    n_estimators=100, random_state=42
)

model.fit(X, y)

importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print("\nFeature Importance:")
print(importance)