# AI Model Forensics

## Detecting Suspicious AI Model Artifacts

AI Model Forensics is a defensive machine-learning system designed to detect suspicious modifications and hidden anomalies inside trained AI model artifacts.

Instead of analyzing the model's source code, the system performs forensic analysis directly on model weights and combines statistical, structural, behavioral, and machine-learning signals.

---

## Key Features

- PyTorch model scanning
- Weight distribution analysis
- Entropy analysis
- Precision-pattern analysis
- Bit-level analysis
- Layer correlation analysis
- Layer anomaly detection
- Behavioral trigger analysis
- Random Forest forensic classifier
- Explainable risk scoring
- Suspicious-layer identification
- Streamlit forensic dashboard
- JSON forensic reports
- Downloadable scan reports

---

## System Architecture

```text
             PyTorch Model
                   |
                   v
            Model Loader
                   |
                   v
            Weight Extraction
                   |
        +----------+----------+
        |          |          |
        v          v          v
   Statistical   Bit-Level  Behavioral
    Analysis     Analysis    Analysis
        |          |          |
        +----------+----------+
                   |
                   v
          Feature Engineering
                   |
                   v
        Random Forest Detector
                   |
                   v
          ML Probability
                   |
                   v
          Risk Score Engine
                   |
          +--------+--------+
          |                 |
          v                 v
     CLEAN /              Risk
   SUSPICIOUS            Score
          |                 |
          +--------+--------+
                   |
                   v
          Streamlit Dashboard
                   |
                   v
          Forensic JSON Report