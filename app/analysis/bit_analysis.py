import numpy as np


def bit_pattern_score(weights):
    x = weights.detach().cpu().numpy().astype(np.float32).ravel()
    bits = x.view(np.uint32)
    low_bits = bits & 255

    counts = np.bincount(low_bits, minlength=256)
    p = counts[counts > 0] / len(low_bits)

    entropy = -np.sum(p * np.log2(p))

    return float(entropy)