import sys

from app.loader import load_model
from app.model_utils import get_weights
from app.analysis.scanner import scan_model
from app.analysis.correlation import layer_correlation
from app.analysis.bit_analysis import bit_pattern_score
from app.detectors.layer_anomaly import detect_anomalies
from app.detectors.risk_score import calculate_risk
from app.detectors.classification import classify_risk
from app.detectors.confidence import confidence
from app.detectors.trigger_test import load_model as load_behavior_model
from app.detectors.trigger_test import trigger_score
from app.reporting.report import generate_report
from app.reporting.json_report import save_report


def scan(path):
    model = load_model(path)
    weights = get_weights(model)

    results = scan_model(weights)
    anomalies = detect_anomalies(results)
    correlation = layer_correlation(weights)

    bit_scores = [
        bit_pattern_score(t)
        for t in weights.values()
        if t.is_floating_point()
    ]
    bit_score = sum(bit_scores) / len(bit_scores)

    behavior_model = load_behavior_model(path)
    trigger = trigger_score(behavior_model)

    risk = calculate_risk(
        anomalies, correlation, trigger, bit_score
    )

    level = classify_risk(risk)
    conf = confidence(risk)

    generate_report(
        risk, level, conf,
        anomalies, correlation, trigger
    )

    save_report(
        path, risk, level, conf,
        anomalies, correlation, trigger
    )


if __name__ == "__main__":
    scan(sys.argv[1])