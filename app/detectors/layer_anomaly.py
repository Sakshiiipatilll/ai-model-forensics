import numpy as np


def detect_anomalies(results):
    values = np.array([
        [v["mean"], v["std"], v["skewness"], v["kurtosis"], v["entropy"]]
        for v in results.values()
    ])

    mean = values.mean(axis=0)
    std = values.std(axis=0) + 1e-8

    scores = {}

    for i, name in enumerate(results):
        z = np.abs((values[i] - mean) / std)
        scores[name] = float(np.mean(z))

    return scores