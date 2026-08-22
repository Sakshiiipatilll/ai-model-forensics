from app.config import RISK_LOW, RISK_MEDIUM, RISK_HIGH


def classify_risk(score):
    if score < RISK_LOW:
        return "LOW"
    if score < RISK_MEDIUM:
        return "MEDIUM"
    if score < RISK_HIGH:
        return "HIGH"
    return "CRITICAL"