import torch 
from torch.masked import as_masked_tensor

data = torch.tensor([[1.0, float('nan'), 3.0]])
mask = torch.isnan(data)

masked = as_masked_tensor(data, mask)

print(masked)