import numpy as np
from scipy.stats import skew, kurtosis


def get_statistics(weights):
    x = weights.detach().cpu().numpy().ravel()

    return {
        "mean": float(np.mean(x)),
        "std": float(np.std(x)),
        "min": float(np.min(x)),
        "max": float(np.max(x)),
        "median": float(np.median(x)),
        "zero_ratio": float(np.mean(x == 0)),
        "skewness": float(skew(x)),
        "kurtosis": float(kurtosis(x))
    }