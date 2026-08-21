def generate_report(risk, level, anomalies, correlation):
    suspicious = [
        name for name, score in anomalies.items()
        if score > 1
    ]

    print("\n===== MODEL FORENSIC REPORT =====")
    print(f"Risk Score       : {risk}/100")
    print(f"Risk Level       : {level}")
    print(f"Layer Correlation: {correlation:.3f}")

    print("\nSuspicious Layers:")

    if suspicious:
        for layer in suspicious:
            print(f"- {layer}")
    else:
        print("- None")

    print("\nDetection Signals:")
    print("- Statistical distribution")
    print("- Entropy")
    print("- Precision patterns")
    print("- Bit-level patterns")
    print("- Layer correlation")

    print("=================================")