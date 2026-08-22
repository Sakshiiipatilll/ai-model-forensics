from app.config import ANOMALY_THRESHOLD


def generate_report(risk, level, confidence, anomalies, correlation, trigger):
    suspicious = [
        name for name, score in anomalies.items()
        if score > ANOMALY_THRESHOLD
    ]

    print("\n===== MODEL FORENSIC REPORT =====")
    print(f"Risk Score        : {risk}/100")
    print(f"Risk Level        : {level}")
    print(f"Confidence        : {confidence}")
    print(f"Layer Correlation : {correlation:.3f}")
    print(f"Trigger Score     : {trigger:.3f}")

    print("\nSuspicious Layers:")
    for layer in suspicious or ["None"]:
        print(f"- {layer}")

    print("\nDetection Evidence:")
    print("- Weight distribution")
    print("- Entropy")
    print("- Precision patterns")
    print("- Bit-level patterns")
    print("- Layer correlation")
    print("- Trigger behavior")

    print("=================================")