import torch
import torch.nn as nn

X = torch.tensor([
    [100.0, 80.0, 1.0],
    [150.0, 443.0, 2.0],
    [8000.0, 22.0, 30.0],
    [9500.0, 21.0, 25.0],
], dtype=torch.float32)

y = torch.tensor([[0.0], [0.0], [1.0], [1.0]])



model = nn.Sequential(
    nn.Linear(3, 8),
    nn.ReLU(),
    nn.Linear(8, 1),
    nn.Sigmoid()
)

loss_fn = nn.BCELoss()

optimizer = torch.optim.Adam(model.parameters(), lr = 0.01)

for epoch in range(1, 100):

    outputs = model(X)
    loss = loss_fn(outputs, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print(f"Epoch {epoch} Loss: {loss.item():.4f}")