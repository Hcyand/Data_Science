"""
K-Means聚类算法对客户进行分类（5类）
"""
import pandas as pd
from sklearn.cluster import KMeans

inputfile = 'zscoreddata.xls'
k = 5
data = pd.read_excel(inputfile)

kmodel = KMeans(n_clusters=k, n_jobs=4)
kmodel.fit(data)

print(kmodel.cluster_centers_)  # 查看聚类中心
