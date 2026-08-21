import torch


clean = torch.load("data/models/model.pt", weights_only=True)
tampered = {}

for name, weight in clean.items():
    x = weight.clone()

    if x.is_floating_point():
        x.view(-1)[::10] += 0.05

    tampered[name] = x

torch.save(tampered, "data/samples/tampered_model.pt")
print("Tampered model created.")