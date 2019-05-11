import pandas as pd
import numpy as np

datafile = 'normalization_data.xls'
data = pd.read_excel(datafile, header=None)
data1 = (data - data.min()) / (data.max() - data.min())  # 最小-最大规范化
data2 = (data - data.mean()) / data.std()  # 零-均值规范化
data3 = data / 10 ** np.ceil(np.log10(data.abs().max()))  # 小数定标规范化
print(data)
print(data1)
print(data2)
print(data3)
