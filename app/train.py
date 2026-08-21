from app.detectors.ml_detector import train_detector


model = train_detector("data/features.csv")
print("ML detector trained.")