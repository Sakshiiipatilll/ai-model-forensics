import numpy as np


def calculate_risk(anomaly_scores, correlation):
    layer_score = np.mean(list(anomaly_scores.values()))
    score = 0.7 * layer_score + 0.3 * correlation

    return round(float(np.clip(score * 25, 0, 100)), 2)