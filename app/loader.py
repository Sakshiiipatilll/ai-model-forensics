import torch


def load_model(path):
    return torch.load(path, map_location="cpu", weights_only=True)