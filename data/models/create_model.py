import torch
import torch.nn as nn


model = nn.Sequential(
    nn.Linear(20, 10),
    nn.ReLU(),
    nn.Linear(10, 2)
)

torch.save(model.state_dict(), "data/models/model.pt")
print("Model created.")

import torch
import torch.nn as nn


model = nn.Sequential(
    nn.Linear(20, 10),
    nn.ReLU(),
    nn.Linear(10, 2)
)

torch.save(model.state_dict(), "data/models/model.pt")
print("Model created.")