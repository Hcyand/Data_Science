"""
拉格朗日插值法原理：
    平面上n个点可以找到n-1次多项式
"""
import pandas as pd
from scipy.interpolate import lagrange

inputfile = 'catering_sale.xls'
outputfile = 'sales.xls'

data = pd.read_excel(inputfile)
data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None


def ployinterp_column(s, n, k=5):
    y = s[list(range(n - k, n)) + list(range(n + 1, n + k))]
    y = y[y.notnull()]
    return lagrange(y.index, list(y))(n)


for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            data[i][j] = ployinterp_column(data[i], j)
data.to_excel(outputfile)
