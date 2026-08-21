import glob
import torch
import pandas as pd

from app.model_utils import get_weights
from app.analysis.scanner import scan_model


def extract(path, label):
    model = torch.load(path, map_location="cpu", weights_only=True)
    results = scan_model(get_weights(model))

    return [{**stats, "label": label} for stats in results.values()]


rows = []

for path in glob.glob("data/samples/generated/clean_*.pt"):
    rows += extract(path, 0)

for path in glob.glob("data/samples/generated/tampered_*.pt"):
    rows += extract(path, 1)

df = pd.DataFrame(rows)
df.to_csv("data/features.csv", index=False)

print("Dataset:", df.shape)
print(df["label"].value_counts())