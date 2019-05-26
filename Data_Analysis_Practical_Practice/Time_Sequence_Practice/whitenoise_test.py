"""
白噪声检验：
为了检验序列中有用的信息是否已经被提取完毕，需要对序列进行白噪声检验
"""
import pandas as pd
from statsmodels.stats.diagnostic import acorr_ljungbox

# 参数初始化
discfile = 'discdata_processed.xls'
data = pd.read_excel(discfile)
data = data.iloc[:len(data) - 5]

# 白噪声检验
[[lb], [p]] = acorr_ljungbox(data['CWXT_DB:184:D:\\'], lags=1)
if p < 0.05:
    print('原始序列为非白噪声序列，对应的p值为：%s' % p)
else:
    print('原始序列为白噪声序列，对应的p值为：%s' % p)
[[lb],[p]] = acorr_ljungbox(data['CWXT_DB:184:D:\\'].diff().dropna(), lags=1)
if p < 0.05:
    print('一阶差分序列为非白噪声序列，对应的p值为：%s' % p)
else:
    print('一阶差分序列为白噪声序列，对应的p值为：%s' % p)
