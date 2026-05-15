import torch
import torch.nn as nn


X = torch.tensor([[100.0, 80.0, 1.0],
                  [9000.0, 22.0, 29.0]], )


model = nn.Sequential(
    nn.Linear(3, 8),
    nn.ReLU(),
    nn.Linear(8, 1),
    nn.Sigmoid()
)


cikti = model(X)
print(cikti)  