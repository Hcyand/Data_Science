"""
使用K-Means算法聚类消费行为特征数据
"""
import pandas as pd
from sklearn.cluster import KMeans

inputfile = 'consumption_data.xls'
outputfile = 'data_type.xls'
data = pd.read_excel(inputfile)
k = 3  # 聚类的类别
iteration = 500  # 聚类最大循环次数
data_zs = 1.0 * (data - data.mean()) / data.std()  # 数据标准化

model = KMeans(n_clusters=k, n_jobs=4, max_iter=iteration)  # 分为k类，并发数为4（进程数）
model.fit(data_zs)  # 开始聚类

# 简单打印结果
r1 = pd.Series(model.labels_).value_counts()  # 统计各个类别的数目
r2 = pd.DataFrame(model.cluster_centers_)  # 找出聚类中心
r = pd.concat([r2, r1], axis=1)  # 横向链接（0是纵向），得到聚类中心对应的类别下的数目
r.columns = list(data.columns) + [u'类别数目']  # 重命名表头
print(r)

# 详细输出原始数据及其类别
r = pd.concat([data, pd.Series(model.labels_, index=data.index)], axis=1)  # 详细输出每个样本对于的类别
r.columns = list(data.columns) + [u'聚类类别']  # 重命题表头
r.to_excel(outputfile)  # 保存结果


# 自定义作图函数
def density_plot(data, title):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正确表示负号
    plt.figure()
    for i in range(len(data.iloc[0])):  # 逐列作图
        (data.iloc[:, i]).plot(kind='kde', label=data.columns[i], linewidth=2)
    plt.ylabel('密度')
    plt.xlabel('人数')
    plt.title('聚类类别%S各属性的密度曲线' % title)
    plt.legend()
    return plt


# 自定义作图函数
def density_plot(data):
    import matplotlib.pyplot as plt
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    p = data.plot(kind='kde', linewidth=2, subplots=True, sharex=False)
    [p[i].set_ylabel('密度') for i in range(k)]
    plt.legend()
    return plt


pic_output = 'pd_'  # 概率密度图文件名前缀
for i in range(k):
    density_plot(data[r['聚类类别'] == i]).savefig('%s%s.png' % (pic_output, i))
