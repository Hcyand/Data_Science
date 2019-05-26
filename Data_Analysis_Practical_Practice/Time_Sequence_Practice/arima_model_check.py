"""
模型检验代码
模型确认后检验是否为白噪声
如果不是白噪声，说明残差中存在有用信息，需要修改模型或进一步提取
"""
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.stats.diagnostic import acorr_ljungbox

discfile = 'discdata_processed.xls'
lagnum = 12  # 残差延迟个数
data = pd.read_excel(discfile, index_col='COLLECTTIME')
data = data.iloc[:len(data) - 5]
xdata = data['CWXT_DB:184:D:\\']

arima = ARIMA(xdata, (0, 1, 1)).fit()
xdata_pred = arima.predict(typ='levels')
pred_error = (xdata_pred - xdata).dropna()
lb, p = acorr_ljungbox(pred_error, lags=lagnum)
h = (p < 0.05).sum()
if h > 0:
    print('模型ARIMA(0,1,1)不符合白噪声模型')
else:
    print('模型ARIMA(0,1,1)符合白噪声模型')
