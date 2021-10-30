import numpy as np

#np.arrange(1,21) == np.array(range(1,21))
num_arr = np.arange(1,21)

print(num_arr)
print(num_arr[::-1])
print("num_arr 내의 모든 원소의 합:",sum(num_arr))
print(num_arr.reshape(5,4))

