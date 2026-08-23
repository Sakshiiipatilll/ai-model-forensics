import numpy as np


def calculate_risk(anomaly_scores, correlation, trigger=0, bit_score=0):
    """
    Combines four heuristic forensic signals into a single 0-100 score.

    Layer anomaly is weighted highest (0.4) since it's the strongest
    standalone indicator of tampered weights; correlation, trigger
    response, and bit-pattern score each contribute 0.2.

    This heuristic score becomes the "base_risk" used in dashboard.py,
    where it is combined with the ML detector's probability as:
        final_risk = 0.4 * base_risk + 60 * ml_probability
    giving the trained classifier 60% weight and this heuristic
    signal 40% weight in the final verdict (bounded 0-100).
    """
    layer = np.mean(list(anomaly_scores.values()))

    score = (
        0.4 * layer +
        0.2 * correlation +
        0.2 * trigger +
        0.2 * bit_score
    )

    return round(float(np.clip(score * 25, 0, 100)), 2)