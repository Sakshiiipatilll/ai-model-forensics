import torch
import random
from pathlib import Path


clean = torch.load("data/models/model.pt", weights_only=True)
Path("data/samples/generated").mkdir(exist_ok=True)

for i in range(50):
    clean_sample = {k: v.clone() for k, v in clean.items()}
    torch.save(clean_sample, f"data/samples/generated/clean_{i}.pt")

    tampered = {k: v.clone() for k, v in clean.items()}

    for weight in tampered.values():
        if weight.is_floating_point():
            x = weight.view(-1)
            x[::20] += random.uniform(0.01, 0.1)

    torch.save(tampered, f"data/samples/generated/tampered_{i}.pt")

print("50 clean and 50 tampered models generated.")