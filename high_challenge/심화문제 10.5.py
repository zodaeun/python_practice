import numpy as np

a = np.arange(32).reshape(4,4,2)

print(a)
print("10번째 원소:",a.flatten()[10])
print("20번째 원소:",a.flatten()[20])
