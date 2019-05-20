"""
拉格朗日法进行缺失值处理
"""
import pandas as pd
from scipy.interpolate import lagrange

inputfile = 'missing_data.xls'
outputfile = 'missing_data_processed.xls'
data = pd.read_excel(inputfile, header=None)


# 自定义列向量插值函数
# s为列向量，n为被插值的位置，k为取值前后的个数，默认为5
def ployinterp_column(s, n, k=5):
    y = s[list(range(n - k, n)) + list(range(n + 1, n + k))]
    y = y[y.notnull()]  # 剔除空值
    return lagrange(y.index, list(y))(n)  # 插值并返回插值结果


# 逐个元素判断是否需要插值
for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:  # 如果空值即插入
            data[i][j] = ployinterp_column(data[i], j)

data.to_excel(outputfile, header=None, index=False)
