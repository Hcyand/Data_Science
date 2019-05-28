"""
Adaptive-Lasso变量选择
"""
import pandas as pd
from sklearn.linear_model import LassoCV

inputfile = 'data1.csv'
data = pd.read_csv(inputfile)
model = LassoCV(cv=5)
model.fit(data.iloc[:, 0:13], data['y'])
result = model.coef_  # 各个特征的系数
print(result)
