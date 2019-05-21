"""
数据变换
标准差标准化
"""
import pandas as pd

datafile = 'zscoredata.xls'
zscoredfile = 'zscoreddata.xls'
data = pd.read_excel(datafile)

data = (data - data.mean(axis=0)) / (data.std(axis=0))
data.columns = ['Z' + i for i in data.columns]  # 表头重命名
data.to_excel(zscoredfile, index=False)
