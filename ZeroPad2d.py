import torch
import torch.nn as nn

print()
input= torch.randn(1,1,3,3)

print(input, end="\n")
print()

m = nn.ZeroPad2d((0,1,0,1))
result = m(input)

print(result, end="\n\n")

t = nn.ZeroPad2d((1,1,2,0))
result2 = t(input)

print(result2, end="\n")