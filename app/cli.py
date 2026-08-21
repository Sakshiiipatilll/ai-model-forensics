import sys

from app.loader import load_model
from app.model_utils import get_weights
from app.analysis.scanner import scan_model
from app.analysis.correlation import layer_correlation
from app.detectors.layer_anomaly import detect_anomalies
from app.detectors.risk_score import calculate_risk
from app.detectors.classification import classify_risk
from app.reporting.report import generate_report


def scan(path):
    model = load_model(path)
    weights = get_weights(model)

    results = scan_model(weights)
    anomalies = detect_anomalies(results)
    correlation = layer_correlation(weights)
    risk = calculate_risk(anomalies, correlation)
    level = classify_risk(risk)

    generate_report(risk, level, anomalies, correlation)


if __name__ == "__main__":
    scan(sys.argv[1])