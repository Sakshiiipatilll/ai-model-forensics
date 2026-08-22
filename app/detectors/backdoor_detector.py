import torch


def behavior_score(model_path):
    weights = torch.load(model_path, map_location="cpu", weights_only=True)

    scores = []

    for weight in weights.values():
        if weight.is_floating_point():
            scores.append(float(torch.abs(weight).mean()))

    return sum(scores) / len(scores)