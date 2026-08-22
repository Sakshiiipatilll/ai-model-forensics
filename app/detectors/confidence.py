def confidence(risk):
    if risk >= 80:
        return "Very High"
    if risk >= 60:
        return "High"
    if risk >= 40:
        return "Moderate"
    return "Low"