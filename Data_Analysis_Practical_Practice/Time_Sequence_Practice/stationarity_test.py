"""
平稳性检测：
    为了确定原始序列中没有随机趋势或者确定趋势，需要对数据进行平稳性检验，否则会出现“伪回归”的现象
采用单位根检验（ADF）的方法或者时序图方法
如果非平稳进行差分运算
"""
import pandas as pd
from statsmodels.tsa.stattools import adfuller as ADF

discfile = 'discdata_processed.xls'
data = pd.read_excel(discfile)
data = data.iloc[:len(data) - 5]  # 不使用最后五个数据

# 平稳性检验
diff = 0
adf = ADF(data['CWXT_DB:184:D:\\'])
while adf[1] >= 0.05:
    diff = diff + 1
    adf = ADF(data['CWXT_DB:184:D:\\'].diff(diff).dropna())
print('原始序列经过%s阶差后归于平稳，p值为%s' % (diff, adf[1]))
