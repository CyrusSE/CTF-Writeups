import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random

class FlagModel(nn.Module):
    def __init__(self):
        super(FlagModel, self).__init__()
        self.layers = nn.Sequential(
            nn.Linear(34, 496),
            nn.Linear(496, 128),
            nn.Linear(128, 24)
        )
    def forward(self, x):
        return self.layers(x)

def wb(_in, _out):
    weight = np.round(np.random.uniform(-1, 1, (_out, _in)).astype(np.float32), 2)
    bias = np.round(np.random.uniform(-1, 1, _out).astype(np.float32), 2)
    return torch.from_numpy(weight), torch.from_numpy(bias)
    
np.random.seed(0x2024)
model = FlagModel()
layer_shapes = [(34, 496), (496, 128), (128, 24)]

for i, (input_dim, output_dim) in enumerate(layer_shapes):
    weight, bias = wb(input_dim, output_dim)
    model.layers[i].weight.data = weight
    model.layers[i].bias.data = bias

target_output = torch.tensor([4366.66357421875, 32835.87890625, -9967.134765625, 63776.640625, 8547.775390625, 12823.4013671875, 28502.36328125, 5493.84423828125, -38881.9609375, -51316.02734375, 8324.1591796875, -26985.572265625, -28508.75, -18546.349609375, -5972.76904296875, 10322.6025390625, -7311.9833984375, -10486.3115234375, -6370.478515625, 18390.52734375, 41471.14453125, -34282.4921875, -1481.2928466796875, -51079.13671875])

def convert(ip):
    return torch.tensor([[float(ord(i)) for i in ip]], dtype=torch.float32)

def reconstruct_flag(seed):
    torch.manual_seed(seed)
    known_prefix = "gemastik{"
    known_suffix = "}"
    unknown_length = 34 - len(known_prefix) - len(known_suffix)
    unknown_part = torch.randint(32, 127, (1, unknown_length), dtype=torch.float32, requires_grad=True)
    optimizer = optim.Adam([unknown_part], lr=0.01)
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, 'min', patience=500, factor=0.5, verbose=True)
    criterion = nn.MSELoss()
    best_loss = float('inf')
    best_unknown = None
    for i in range(50000):
        optimizer.zero_grad()        
        full_input = torch.cat([
            convert(known_prefix),
            unknown_part.view(1, -1),
            convert(known_suffix)
        ], dim=1)
        output = model(full_input)
        loss = criterion(output[0], target_output)
        loss.backward()
        optimizer.step()
        scheduler.step(loss)
        with torch.no_grad():
            unknown_part.data.clamp_(32, 126)
        if loss < best_loss:
            best_loss = loss.item()
            best_unknown = unknown_part.clone().detach()
        if i % 1000 == 0:
            print(f"Iteration {i}, Loss: {loss.item()}")
        if i % 5000 == 0 and i > 0:
            unknown_part.data += torch.randn_like(unknown_part.data) * 0.1
    return best_unknown

def verify_flag(result):
    import hashlib
    md5_hash = hashlib.md5(result.encode()).hexdigest()
    print("MD5 hash of the result:", md5_hash)
    print("Expected MD5 hash:      bfa1d885956a9ee88017d2b05b23b4ed")
    return md5_hash == "bfa1d885956a9ee88017d2b05b23b4ed"

for attempt in range(5):
    print(f"\nAttempt {attempt + 1}")
    best_unknown = reconstruct_flag(random.randint(1, 10000))
    unknown_part = ''.join([chr(int(round(x))) for x in best_unknown.numpy()[0]])
    result = f"gemastik{{{unknown_part}}}"
    print("Reconstructed flag:", result)
    if verify_flag(result):
        print("Flag found!")
        break
else:
    print("Failed to find the correct flag after 5 attempts.")