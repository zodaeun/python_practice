import numpy as np

n_arr = np.arange(25).reshape(5,5)

#1번
print(n_arr)
print()

#2번
print("첫 원소:",n_arr[0][0])
print("마지막 원소:",n_arr[-1][-1])
print()

#3번
print(n_arr[:2])
print()

#4번
print(n_arr[2:])
print()

#5번
print(n_arr[::,::2])
print()

#6번
print(n_arr[::2,::2])
print()

#7번
print(n_arr[:2].reshape(5,2))
