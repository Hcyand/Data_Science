"""
航空公司客户价值分析:
数据探索分析:
对数据进行基本的探索
返回缺失值个数以及最大值和最小值
"""
import pandas as pd

datafile = 'air_data.csv'
resultfile = 'explore.xls'
data = pd.read_csv(datafile, encoding='utf-8')

explore = data.describe(percentiles=[], include='all').T
explore['null'] = len(data) - explore['count']

explore = explore[['null', 'max', 'min', 'std', 'mean']]
explore.columns = ['空值数', '最大值', '最小值', '方差', '平均数']
explore.to_excel(resultfile)
