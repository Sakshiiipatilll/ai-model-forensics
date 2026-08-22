import numpy as np


def detect_anomalies(results):
    valid = {
        k: v for k, v in results.items()
        if v["num_parameters"] >= 20
    }

    if len(valid) < 2:
        return {k: 0.0 for k in results}

    values = np.array([
        [
            v["mean"],
            v["std"],
            v["skewness"],
            v["kurtosis"],
            v["entropy"]
        ]
        for v in valid.values()
    ])

    mean = values.mean(axis=0)
    std = values.std(axis=0) + 1e-8

    scores = {}

    for i, name in enumerate(valid):
        z = np.abs((values[i] - mean) / std)
        scores[name] = float(np.mean(z))

    for name in results:
        if name not in scores:
            scores[name] = 0.0

    return scores