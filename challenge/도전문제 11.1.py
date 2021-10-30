import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1000)
y = np.random.randn(1000)

plt.plot(x, y, color = "green", marker = 'o', linestyle = 'solid')

plt.show()

