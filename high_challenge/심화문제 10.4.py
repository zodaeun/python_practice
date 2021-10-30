import numpy as np

np_arr=np.random.randint(0,2,25).reshape(5,5)
print(np_arr)

print("행렬의 열 방향 성분의 합:",np_arr.sum(axis = 0))
print("행렬의 행 방향 성분의 합:",np_arr.sum(axis = 1))

