import numpy as np


def calculate_risk(anomaly_scores, correlation, trigger=0, bit_score=0):
    layer = np.mean(list(anomaly_scores.values()))

    score = (
        0.4 * layer +
        0.2 * correlation +
        0.2 * trigger +
        0.2 * bit_score
    )

    return round(float(np.clip(score * 25, 0, 100)), 2)