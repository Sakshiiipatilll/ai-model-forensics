import numpy as np


def layer_correlation(weights):
    layers = [v.detach().cpu().numpy().ravel() for v in weights.values()]
    layers = [x for x in layers if len(x) > 1]

    if len(layers) < 2:
        return 0.0

    size = min(map(len, layers))
    data = np.array([x[:size] for x in layers])

    corr = np.corrcoef(data)
    return float(np.mean(np.abs(corr[np.triu_indices_from(corr, 1)])))