"""
arima时序模型
"""
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller as ADF
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.stats.diagnostic import acorr_ljungbox
from statsmodels.tsa.arima_model import ARIMA

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

discfile = 'arima_data.xls'
forecastnum = 5  # 预测的数目
# 指定日期为指标，pandas自动将“日期”列识别为Datetime格式
data = pd.read_excel(discfile, index_col='日期')

# 时序图
data.plot()
plt.show()

# 自相关图
plot_acf(data).show()

# 平稳性检测
print('原始序列的ADF检验结果为：', ADF(data['销量']))

# 差分后结果
D_data = data.diff().dropna()
D_data.columns = ['销量差分']
D_data.plot()
plt.show()
plot_acf(D_data).show()
plot_pacf(D_data).show()
print('差分序列的ADF检验结果为：', ADF(D_data['销量差分']))

# 白噪声检验
print('差分序列的白噪声检验结果为：', acorr_ljungbox(D_data, lags=1))  # 返回统计量和p值

# 定阶
pmax = int(len(D_data) / 10)  # 一般阶数不超过length/10
qmax = int(len(D_data) / 10)  # 一般阶数不超过length/10
bic_matrix = []  # bic矩阵
for p in range(pmax + 1):
    tmp = []
    for q in range(qmax + 1):
        try:  # 存在部分报错，所有用try来跳过报错
            tmp.append(ARIMA(data, (p, 1, q)).fit().bic)
        except:
            tmp.append(None)
    bic_matrix.append(tmp)
bic_matrix = pd.DataFrame(bic_matrix)  # 从中可以找到最小值
p, q = bic_matrix.stack().idxmin()  # 先用stack展平，再用idxmin找到最小值位置
print('BIC最小的p值和q值为：%s，%s' % (p, q))
model = ARIMA(data, (p, 1, q)).fit()  # 建立ARIMA(0,1,1)模型
print(model.summary2())  # 给出一份模型报告
print(model.forecast(5))  # 做为期五天的预测，返回预测结果，标准误差，置信区间
