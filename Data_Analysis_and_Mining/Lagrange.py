"""
拉格朗日插值法原理：
    平面上n个点可以找到n-1次多项式
"""
import pandas as pd
from scipy.interpolate import lagrange  # 拉格朗日插值函数

inputfile = 'catering_sale.xls'
outputfile = 'sales.xls'

data = pd.read_excel(inputfile)
data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None  # 过滤异常值，将其变成空值


# 自定义列向量插值函数
# s位列向量，n为插值的位置，k为取前后的数据个数
def ployinterp_column(s, n, k=5):
    y = s[list(range(n - k, n)) + list(range(n + 1, n + k))]  # 取数
    y = y[y.notnull()]  # 剔除空值（异常值）
    return lagrange(y.index, list(y))(n)  # 插值并返回插值结果


# 逐个元素判断是否需要插值
for i in data.columns:  # 查看列数
    for j in range(len(data)):
        if (data[i].isnull())[j]:  # 如果为空值即插值
            data[i][j] = ployinterp_column(data[i], j)
data.to_excel(outputfile)
