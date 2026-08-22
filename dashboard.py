import json
import tempfile

import joblib
import pandas as pd
import streamlit as st

from app.loader import load_model
from app.model_utils import get_weights
from app.analysis.scanner import scan_model
from app.analysis.correlation import layer_correlation
from app.analysis.bit_analysis import bit_pattern_score
from app.detectors.layer_anomaly import detect_anomalies
from app.detectors.risk_score import calculate_risk
from app.detectors.classification import classify_risk
from app.detectors.trigger_test import load_model as load_behavior_model
from app.detectors.trigger_test import trigger_score


st.set_page_config(
    page_title="AI Model Forensics",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 AI Model Forensics")
st.caption(
    "Detect suspicious AI model artifacts, tampering and hidden anomalies"
)

uploaded = st.file_uploader(
    "Upload a PyTorch model",
    type=["pt", "pth"]
)

if uploaded:
    with tempfile.NamedTemporaryFile(
        delete=False, suffix=".pt"
    ) as f:
        f.write(uploaded.read())
        path = f.name

    model = load_model(path)
    weights = get_weights(model)

    results = scan_model(weights)
    anomalies = detect_anomalies(results)
    correlation = layer_correlation(weights)

    bits = [
        bit_pattern_score(t)
        for t in weights.values()
        if t.is_floating_point()
    ]

    bit_score = sum(bits) / len(bits)

    behavior_model = load_behavior_model(path)
    trigger = trigger_score(behavior_model)

    base_risk = calculate_risk(
        anomalies,
        correlation,
        trigger,
        bit_score
    )

    detector = joblib.load("app/detectors/model.pkl")
    columns = detector.feature_names_in_

    x = pd.DataFrame(list(results.values()))
    x = x.reindex(columns=columns, fill_value=0)

    ml_probability = detector.predict_proba(x)[:, 1].mean()
    ml_suspicious = ml_probability >= 0.5

    risk = round(
        0.4 * base_risk + 60 * ml_probability,
        2
    )

    level = classify_risk(risk)

    if ml_suspicious:
        st.error("🚨 SUSPICIOUS MODEL DETECTED")
    else:
        st.success("✅ MODEL APPEARS CLEAN")

    st.subheader("Model Risk Assessment")

    c1, c2, c3 = st.columns(3)

    c1.metric("Risk Score", f"{risk}/100")
    c2.metric("Risk Level", level)
    c3.metric(
        "ML Verdict",
        "SUSPICIOUS" if ml_suspicious else "CLEAN"
    )

    st.progress(min(risk / 100, 1.0))

    st.subheader("Detection Signals")

    c1, c2, c3 = st.columns(3)

    c1.metric("ML Probability", f"{ml_probability:.3f}")
    c2.metric("Layer Correlation", f"{correlation:.3f}")
    c3.metric("Bit Score", f"{bit_score:.3f}")

    c1, c2 = st.columns(2)

    c1.metric("Trigger Score", f"{trigger:.3f}")
    c2.metric(
        "Parameters Analyzed",
        f"{sum(v['num_parameters'] for v in results.values()):,}"
    )

    st.subheader("Layer Anomaly Scores")
    st.bar_chart(anomalies)

    suspicious = {
        k: v
        for k, v in anomalies.items()
        if v > 1
    }

    st.subheader("Suspicious Layers")

    if suspicious:
        st.dataframe(
            pd.DataFrame(
                list(suspicious.items()),
                columns=["Layer", "Anomaly Score"]
            ),
            use_container_width=True
        )
    else:
        st.success("No highly anomalous layers detected.")

    report = {
        "model": uploaded.name,
        "risk_score": risk,
        "risk_level": level,
        "ml_verdict": (
            "SUSPICIOUS" if ml_suspicious else "CLEAN"
        ),
        "ml_probability": ml_probability,
        "layer_correlation": correlation,
        "bit_score": bit_score,
        "trigger_score": trigger,
        "suspicious_layers": suspicious
    }

    st.subheader("Forensic Report")

    st.json(report)

    st.download_button(
        "⬇ Download Forensic Report",
        data=json.dumps(report, indent=4),
        file_name="forensic_report.json",
        mime="application/json"
    )

    st.subheader("Detection Evidence")

    for item in [
        "Weight distribution",
        "Entropy analysis",
        "Precision patterns",
        "Bit-level patterns",
        "Layer correlations",
        "Trigger behavior",
        "ML classification"
    ]:
        st.write(f"✓ {item}")

    st.success("Forensic scan completed.")