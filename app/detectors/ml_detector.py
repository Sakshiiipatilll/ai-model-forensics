import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train_detector(path):
    df = pd.read_csv(path)

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
    print("Accuracy:", accuracy_score(y_test, prediction))

    joblib.dump(model, "app/detectors/model.pkl")

    return model