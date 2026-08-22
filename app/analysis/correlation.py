import numpy as np


def layer_correlation(weights):
    layers = [
        v.detach().cpu().numpy().ravel()
        for v in weights.values()
        if v.numel() >= 20
    ]

    if len(layers) < 2:
        return 0.0

    size = min(len(x) for x in layers)
    data = np.array([x[:size] for x in layers])

    corr = np.corrcoef(data)
    values = corr[np.triu_indices_from(corr, 1)]

    return float(np.mean(np.abs(values)))