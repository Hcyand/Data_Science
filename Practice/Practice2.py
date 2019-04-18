# 使用scatter()绘制散点图并设置其样式
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(500)
plt.scatter(x, x ** 3, c=x ** 3, cmap=plt.cm.Blues, edgecolors='none', s=40)
plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=16)
plt.ylabel("Square of Value", fontsize=16)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()
