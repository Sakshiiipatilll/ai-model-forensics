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

---

## Getting Started

### Installation

```bash
git clone https://github.com/Sakshiiipatilll/ai-model-forensics.git
cd ai-model-forensics
pip install -r requirements.txt
```

### Run the Dashboard

```bash
streamlit run dashboard.py
```

Upload a `.pt` or `.pth` PyTorch model file to get a forensic risk assessment, detection signals, and a downloadable JSON report.

### Reproduce the Evaluation Dataset

The classifier is trained and evaluated on a synthetic dataset of 60 clean and 60 tampered models. To regenerate it from scratch:

```bash
python data/models/create_model.py   # generates 60 clean + 60 tampered models -> data/features.csv
python tests/train.py                # retrains the classifier and prints Accuracy / Precision / Recall / F1
```

Both scripts use a fixed random seed (42), so results are reproducible.

### Project Structure

```text
app/
  loader.py               # safe PyTorch model loading (weights_only=True)
  model_utils.py           # weight extraction helpers
  analysis/                 # statistical, bit-level, correlation analysis
  detectors/                 # ML classifier, risk scoring, trigger test
data/
  models/create_model.py    # synthetic clean/tampered dataset generator
  features.csv               # generated feature dataset (see above)
tests/
  train.py                   # trains + evaluates the Random Forest detector
dashboard.py                  # Streamlit forensic scanning UI
```

---

## Disclaimer

This is a research prototype. Evaluation metrics are reported on a synthetic dataset and should not be interpreted as guaranteed real-world detection performance against real-world malicious model artifacts.