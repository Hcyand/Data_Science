"""
连续属性离散化：
1.等宽法：将属性的值域分为相同宽度的区间，0~4，4~8，8~12（由值域确定）
2.等频法：将相同数量的记录放进区间
3.基于聚类分析的方法：a)将连续属性的值用聚类算法（如K-Means算法）进行聚类；b)聚类得到的簇进行处理，合并簇的连续属性值并做同一标记

K-Means算法（简单理解）：假设样本两个特征值，在分布中有明显的簇（聚集在一块区域），随机选取两个点a，b，距离两点更近样本的归在a类或者b类
，计算a类中所有样本的平均点位得到新的a点（同理得到新的b点），重复以上步骤，直至a，b不再变化或者变化很小（图解更容易理解）
"""
# 数据规范化练习
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

datafile = 'discretization_data.xls'
data = pd.read_excel(datafile)
data = data[u'肝气郁结证型系数'].copy()
k = 4

d1 = pd.cut(data, k, labels=range(k))  # 等宽离散化

# 等频率离散化
w = [1.0 * i / k for i in range(k + 1)]  # 0%，25%，50%,75%,100%
w = data.describe(percentiles=w)[4:4 + k + 1]  # 使用describe函数自动计算分位数
w[0] = w[0] * (1 - 1e-10)
d2 = pd.cut(data, w, labels=range(k))

# 基于聚类分析的方法
# pandas升级后部分函数应用改变
kmodel = KMeans(n_clusters=k, n_jobs=4)  # 建立模型，n_jobs是并行数，一般等于CPU数比较好，k表示质心
kmodel.fit(data.values.reshape((len(data), 1)))  # 训练模型，reshape的运用需要加一个values
c = pd.DataFrame(kmodel.cluster_centers_).sort_values(0)  # 输出聚类中心，并且排序，排序在pandas中需要用sort_values
w = c.rolling(2).mean().iloc[1:]  # 相邻两项求中点，作为边界值
w = [0] + list(w[0]) + [data.max()]  # 把首末边界点加上
d3 = pd.cut(data, w, labels=range(k))


def cluster_plot(d, k):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    plt.figure(figsize=(8, 3))
    for j in range(0, k):
        plt.plot(data[d == j], [j for j in d[d == j]], 'o')
    plt.ylim(-0.5, k - 0.5)
    return plt


cluster_plot(d1, k).show()
cluster_plot(d2, k).show()
cluster_plot(d3, k).show()
