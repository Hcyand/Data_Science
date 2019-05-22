"""
数据聚类离散化
"""
from __future__ import print_function
import pandas as pd
from sklearn.cluster import KMeans

datafile = 'data.xls'
processedfile = 'data_processed.xls'
data = pd.read_excel(datafile)
typelabel = {'肝气郁结证型系数': 'A', '热毒蕴结证型系数': 'B', '冲任失调证型系数': 'C',
             '气血两虚证型系数': 'D', '脾胃虚弱证型系数': 'E', '肝肾阴虚证型系数': 'F'}
k = 4
keys = list(typelabel.keys())
"""
DataFrame定义：1.一个表格型的数据结构/2.含有一组有序的列/3.可以看作共享同一个index的Series集合
DataFrame（数据帧）是二维数据结构
Series 是一个类数组的数据结构，同时带有标签（lable）或者说索引（index）
Series的定义：Series是一种类似于一维数组的对象，它由一组数据（各种NumPy数据类型）以及一组与之相关的数据标签（即索引）组成。
"""
result = pd.DataFrame()

if __name__ == '__main__':
    for i in range(len(keys)):
        print('正在进行“%s”的聚类' % keys[i])
        kmodel = KMeans(n_clusters=k, n_jobs=4)
        kmodel.fit(data[[keys[i]]].values)

        r1 = pd.DataFrame(kmodel.cluster_centers_, columns=[typelabel[keys[i]]])
        r2 = pd.Series(kmodel.labels_).value_counts()
        r2 = pd.DataFrame(r2, columns=[typelabel[keys[i]] + 'num'])
        # axis=0表示沿着每一列或行标签\索引值向下执行方法；axis=1表示沿着每一行或者列标签模向执行对应的方法
        r = pd.concat([r1, r2], axis=1).sort_values(typelabel[keys[i]])
        r.index = [1, 2, 3, 4]

        r[typelabel[keys[i]]] = r[typelabel[keys[i]]].rolling(2).mean()  # 取两个聚类中心的平均数
        r[typelabel[keys[i]]][1] = 0.0
        result = result.append(r.T)  # 结果相加，转置
    result = result.sort_index()
    result.to_excel(processedfile)
