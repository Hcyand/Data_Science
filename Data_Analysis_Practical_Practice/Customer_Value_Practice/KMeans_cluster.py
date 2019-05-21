"""
K-Means聚类算法对客户进行分类（5类）
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

inputfile = 'zscoreddata.xls'
k = 5
data = pd.read_excel(inputfile)

kmodel = KMeans(n_clusters=k, n_jobs=4)
kmodel.fit(data)
quantity = pd.Series(kmodel.labels_).value_counts()  # 获取每个簇中样本数量

# 绘制雷达图
labels = data.columns
centers = kmodel.cluster_centers_  # 获取聚类中心
centers = np.hstack((centers, centers[:, 0].reshape(5, 1)))  # 数据首尾相连
n = len(labels)
angles = np.linspace(0, 2 * np.pi, n, endpoint=False)  # n决定几边行，（0，2*pi)表示⚪
angles = np.concatenate((angles, [angles[0]]))  # 数据首尾相连

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

floor = np.floor(centers.min())  # 小于最小值的整数
ceil = np.ceil(centers.max())  # 大于最大值的整数
# 画若干个五边形
for i in np.arange(floor, ceil + 0.5, 0.5):
    ax.plot(angles, [i] * (n + 1), '--', lw=0.5, color='black')
# 画不同客户群的分割线
for i in range(n):
    ax.plot([angles[i], angles[i]], [floor, ceil], '--', lw=0.5, color='black')
# 画不同客户群所占的大小
for i in range(5):
    ax.plot(angles, centers[i], lw=2)
    ax.fill(angles, centers[i])
ax.set_thetagrids(angles * 180 / np.pi, labels)  # 设置显示的角度，将弧度转换为角度
plt.legend(loc='lower right', bbox_to_anchor=(1.5, 0.0))  # 设置图例的位置，在画布外
ax.set_theta_zero_location('N')  # 设置极坐标的起点（即0°）在正北方向，即相当于坐标轴逆时针旋转90°
ax.spines['polar'].set_visible(False)  # 不显示极坐标最外圈的圆
ax.grid(False)  # 不显示默认的分割线
ax.set_yticks([])  # 不显示坐标间隔
plt.show()
