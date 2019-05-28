"""
谱系聚类图
从谱系图中可以看到将聚类分为3类
"""
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram

standardizedfile = 'standardized.xls'
data = pd.read_excel(standardizedfile, index_col='基站编号')

Z = linkage(data, method='ward', metric='euclidean')  # 谱系聚类图
p = dendrogram(Z, 0)  # 画谱系聚类图
plt.show()
