import joblib
import pandas as pd
import torch

from app.model_utils import get_weights
from app.analysis.scanner import scan_model


def classify(path):
    model = torch.load(path, map_location="cpu", weights_only=True)
    results = scan_model(get_weights(model))

    detector = joblib.load("app/detectors/model.pkl")
    columns = detector.feature_names_in_

    rows = [list(v.values()) for v in results.values()]
    x = pd.DataFrame(rows, columns=columns)

    prediction = detector.predict(x)

    return "SUSPICIOUS" if any(prediction) else "CLEAN"


print("Model:", classify("data/samples/tampered_model.pt"))