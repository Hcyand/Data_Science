"""
层次聚类算法
"""
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

standardizedfile = 'standardized.xls'
data = pd.read_excel(standardizedfile, index_col='基站编号')
k = 3

model = AgglomerativeClustering(n_clusters=k, linkage='ward')
model.fit(data)

# 详细输出原始数据及其类别
r = pd.concat([data, pd.Series(model.labels_, index=data.index)], axis=1)
# 详细输出每个样本对应的类别
r.columns = list(data.columns) + ['聚类类别']  # 重命名表头

style = ['ro-', 'go-', 'bo-']
xlabels = ['工作日人均停留时间', '凌晨人均停留时间', '周末人均停留时间', '日均人流量']
pic_output = 'type_'

for i in range(k):
    plt.figure()
    tmp = r[r['聚类类别'] == i].iloc[:, :4]  # 提取每一类
    for j in range(len(tmp)):
        plt.plot(range(1, 5), tmp.iloc[j], style[i])
    plt.xticks(range(1, 5), xlabels, rotation=20)  # 坐标标签
    plt.subplots_adjust(bottom=0.15)  # 调整底部
    plt.savefig('%s%s.png' % (pic_output, i))  # 保存图片
