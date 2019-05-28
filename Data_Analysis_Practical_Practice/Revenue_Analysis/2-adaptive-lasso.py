"""
Adaptive-Lasso变量选择
"""
import pandas as pd
from sklearn.linear_model import LassoCV

inputfile = 'data2.csv'
data = pd.read_csv(inputfile)
model = LassoCV(cv=5)
model.fit(data.iloc[:, 0:6], data['y'])
result = model.coef_
print(result)
