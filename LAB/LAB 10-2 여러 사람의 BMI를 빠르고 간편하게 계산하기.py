import numpy as np

height = [1.83, 1.76,1.69,1.86,1.77,1.73]
weight = [86,74,59,95,80,68]

np_height = np.array(height)
np_weight = np.array(weight)


bmi = np_weight / (np_height**2)

print('대상자들의 키: ', np_height)
print('대상자들의 몸무게: ', np_weight)
print('대상자들의 BMI: ',bmi)
