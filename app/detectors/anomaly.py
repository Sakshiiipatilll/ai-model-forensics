import numpy as np


def anomaly_score(stats):
    values = [
        abs(stats["skewness"]),
        abs(stats["kurtosis"]),
        stats["zero_ratio"]
    ]

    return float(np.mean(values))