import numpy as np
import matplotlib.pyplot as plt

# 取值0到1之间500个等距点
x = np.linspace(0, 1, 500)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
fig, ax = plt.subplots()
ax.fill(x, y, zorder=10)
# 画格子
ax.grid(True, zorder=5)
plt.show()
