"""
原始数据求解Pearson相关系数
"""
import numpy as np
import pandas as pd

inputfile = 'data1.csv'
data = pd.read_csv(inputfile)
# round为四舍五入
# corr为相关系数计算函数，method='person'
# 计算相关系数矩阵，保留两位小数
print(np.round(data.corr(method='pearson'), 2))
