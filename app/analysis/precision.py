import numpy as np


def precision_stats(weights):
    x = weights.detach().cpu().numpy().ravel()
    frac = np.abs(x * 1000) % 1

    return {
        "unique_ratio": float(np.unique(x).size / len(x)),
        "low_precision_ratio": float(np.mean(frac < 0.001))
    }