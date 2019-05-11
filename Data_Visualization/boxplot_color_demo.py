import matplotlib.pyplot as plt
import numpy as np

np.random.seed(123)
# 决定箱型图的样式
all_data = [np.random.normal(0, std, 100) for std in range(1, 4)]
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(6, 4))
# rectangular box plot
bplot1 = axes[0].boxplot(all_data, vert=True, patch_artist=True)
# notch box plot
bplot2 = axes[1].boxplot(all_data, notch=True, vert=True, patch_artist=True)
# 颜色
colors = ['pink', 'lightblue', 'lightgreen']
for bplot in (bplot1, bplot2):
    for patch, color in zip(bplot['boxes'], colors):
        # 涂色
        patch.set_facecolor(color)
for ax in axes:
    # 横向线条
    ax.yaxis.grid(True)
    ax.set_xticks([y + 1 for y in range(len(all_data))], )
    ax.set_xlabel('xlabel')
    ax.set_ylabel('ylabel')
plt.setp(axes, xticks=[y + 1 for y in range(len(all_data))], xticklabels=['x1', 'x2', 'x3', 'x4'])
plt.show()
