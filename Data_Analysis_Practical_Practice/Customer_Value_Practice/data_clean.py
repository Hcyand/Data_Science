"""
数据预处理
1.丢弃票价为空的记录
2.丢弃票价为0，平均折扣率不为0，总飞行公里数大于0的记录
"""
import pandas as pd

datafile = 'air_data.csv'
cleanfile = 'data_cleaned.csv'
data = pd.read_csv(datafile, encoding='utf-8')

data = data[data['SUM_YR_1'].notnull() * data['SUM_YR_2'].notnull()]
index1 = data['SUM_YR_1'] != 0
index2 = data['SUM_YR_2'] != 0
index3 = (data['SEG_KM_SUM'] == 0) & (data['avg_discount'] == 0)
data = data[index1 | index2 | index3]
data.to_csv(cleanfile)
