import json


def save_report(path, risk, level, confidence, anomalies, correlation, trigger):
    report = {
        "model": path,
        "risk_score": risk,
        "risk_level": level,
        "confidence": confidence,
        "layer_correlation": correlation,
        "trigger_score": trigger,
        "anomalous_layers": anomalies
    }

    with open("forensic_report.json", "w") as file:
        json.dump(report, file, indent=4)

    print("Report saved: forensic_report.json")