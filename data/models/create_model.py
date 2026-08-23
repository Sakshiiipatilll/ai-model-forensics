import os
import random

import pandas as pd
import torch
import torch.nn as nn

from app.model_utils import get_weights
from app.analysis.scanner import scan_model

SEED = 42
N_CLEAN = 60
N_TAMPERED = 60
OUT_DIR = "data/models"
FEATURES_PATH = "data/features.csv"


def build_model():
    return nn.Sequential(
        nn.Linear(20, 10),
        nn.ReLU(),
        nn.Linear(10, 2)
    )


def tamper(state_dict):
    """
    Simulates a backdoor/tampering attack by injecting a large,
    localized perturbation into a random layer's weights -- mimicking
    a targeted change to model behavior rather than uniform noise.
    """
    tampered = {k: v.clone() for k, v in state_dict.items()}
    weight_keys = [k for k in tampered if "weight" in k]
    target_key = random.choice(weight_keys)

    noise = torch.randn_like(tampered[target_key]) * 5.0
    mask = torch.rand_like(tampered[target_key]) < 0.3  # perturb ~30% of values
    tampered[target_key][mask] += noise[mask]

    return tampered


def main():
    torch.manual_seed(SEED)
    random.seed(SEED)

    os.makedirs(OUT_DIR, exist_ok=True)
    rows = []

    for i in range(N_CLEAN):
        model = build_model()
        path = f"{OUT_DIR}/clean_{i}.pt"
        torch.save(model.state_dict(), path)

        weights = get_weights(model)
        features = scan_model(weights)
        row = {}
        for layer_feats in features.values():
            for k, v in layer_feats.items():
                row[k] = row.get(k, 0) + v
        row["label"] = 0
        rows.append(row)

    for i in range(N_TAMPERED):
        model = build_model()
        tampered_state = tamper(model.state_dict())
        model.load_state_dict(tampered_state)
        path = f"{OUT_DIR}/tampered_{i}.pt"
        torch.save(model.state_dict(), path)

        weights = get_weights(model)
        features = scan_model(weights)
        row = {}
        for layer_feats in features.values():
            for k, v in layer_feats.items():
                row[k] = row.get(k, 0) + v
        row["label"] = 1
        rows.append(row)

    df = pd.DataFrame(rows).fillna(0)
    df.to_csv(FEATURES_PATH, index=False)

    print(f"Generated {N_CLEAN} clean + {N_TAMPERED} tampered models.")
    print(f"Saved features to {FEATURES_PATH} ({len(df)} rows).")


if __name__ == "__main__":
    main()