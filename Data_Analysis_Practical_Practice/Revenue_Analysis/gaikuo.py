"""
原始数据概括性度量
最小值，最大值，均值，标准差
"""
import pandas as pd
import numpy as np

inputfile = 'data1.csv'
data = pd.read_csv(inputfile)
r = [data.min(), data.max(), data.mean(), data.std()]
r = pd.DataFrame(r, index=['Min', 'Max', 'Mean', 'STD'])
np.round(r, 2)  # 保留两位小数
print(r)
