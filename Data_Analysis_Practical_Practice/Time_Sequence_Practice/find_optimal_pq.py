"""
模型识别代码
采用极大似然比方法进行模型的参数估计，估计每个参数的值
然后针对各个不同的模型，采用BIC信息准则对模型进行定阶
确定p，q参数，从而选择最优模型
"""
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA

# 参数初始化
discfile = 'discdata_processed.xls'
data = pd.read_excel(discfile, index_col='COLLECTTIME')
data = data.iloc[:len(data) - 5]
xdata = data['CWXT_DB:184:D:\\']

pmax = int(len(xdata) / 10)
qmax = int(len(xdata) / 10)
bic_matrix = []
for p in range(pmax + 1):
    tmp = []
    for q in range(qmax + 1):
        try:
            tmp.append(ARIMA(xdata, (p, 1, q)).fit().bic)
        except:
            tmp.append(None)
    bic_matrix.append(tmp)
bic_matrix = pd.DataFrame(bic_matrix)
p, q = bic_matrix.stack().astype('float64').idxmin()
print('BIC最小的p值和q值为：%s %s' % (p, q))
