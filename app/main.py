from app.loader import load_model
from app.model_utils import get_weights
from app.analysis.scanner import scan_model
from app.analysis.correlation import layer_correlation
from app.detectors.layer_anomaly import detect_anomalies
from app.detectors.risk_score import calculate_risk
from app.reporting.report import generate_report


model = load_model("data/models/model.pt")
weights = get_weights(model)

results = scan_model(weights)
anomalies = detect_anomalies(results)
correlation = layer_correlation(weights)
risk = calculate_risk(anomalies, correlation)

generate_report(risk, anomalies, correlation)