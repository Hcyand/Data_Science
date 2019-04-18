# 绘制简单的折线图
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5, 6]
line = [1, 4, 9, 16, 25, 36]
plt.plot(input_values, line, linewidth=5)

# 图标标题，并给坐标轴给上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=14)

plt.show()
