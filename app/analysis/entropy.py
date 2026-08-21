import numpy as np


def calculate_entropy(weights, bins=50):
    x = weights.detach().cpu().numpy().ravel()
    hist, _ = np.histogram(x, bins=bins, density=True)
    hist = hist[hist > 0]

    return float(-np.sum(hist * np.log2(hist)))