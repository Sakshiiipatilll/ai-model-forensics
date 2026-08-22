import torch


def load_model(path):
    model = torch.nn.Sequential(
        torch.nn.Linear(20, 10),
        torch.nn.ReLU(),
        torch.nn.Linear(10, 2)
    )

    weights = torch.load(path, map_location="cpu", weights_only=True)
    model.load_state_dict(weights)
    model.eval()

    return model


def trigger_score(model):
    clean = torch.randn(100, 20)
    triggered = clean.clone()
    triggered[:, :3] = 10.0

    with torch.no_grad():
        clean_out = model(clean)
        trigger_out = model(triggered)

    difference = torch.abs(trigger_out - clean_out).mean()
    return float(torch.sigmoid(difference).item())