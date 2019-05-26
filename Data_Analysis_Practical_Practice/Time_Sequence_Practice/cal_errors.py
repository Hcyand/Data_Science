"""
模型评价代码：
平均绝对误差；均方根误差；平均绝对百分误差
"""
import pandas as pd

file = 'predictdata.xls'
data = pd.read_excel(file)
# 计算误差
abs_ = (data['预测值'] - data['实际值']).abs()
mae_ = abs_.mean()
rmse_ = ((abs_ ** 2).mean()) ** 0.5
mape_ = (abs_ / data['实际值']).mean()
print('平均绝对误差为：%0.4f,\n均方根误差为：%0.4f,\n平均绝对百分误差为：%0.6f.' % (mae_, rmse_, mape_))
