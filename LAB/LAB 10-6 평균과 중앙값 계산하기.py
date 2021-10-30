import numpy as np

p = np.zeros((100,3))

p[:,0] = 10 * np.random.randn(100) + 175
p[:,1] = 10 * np.random.randn(100) + 70
p[:,2] = np.floor(10 * np.random.randn(100)) + 22

h = p[:,0]
print("신장 평균값: ", np.mean(h))
print("신장 중앙값: ", np.median(h))
print()

w = p[:,1]
print("몸무게 평균값: ", np.mean(w))
print("몸무게 중앙값: ", np.median(w))
print()

a = p[:,2]
print("나이 평균값: ", np.mean(a))
print("나이 중앙값: ", np.median(a))
