import torch
import torch.nn as nn


class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(20, 10),
            nn.ReLU(),
            nn.Linear(10, 2)
        )

    def forward(self, x):
        return self.net(x)


model = Model()
model.net[2].bias.data[1] += 5.0

torch.save(model.state_dict(), "data/samples/backdoor_model.pt")
print("Backdoor test model created.")