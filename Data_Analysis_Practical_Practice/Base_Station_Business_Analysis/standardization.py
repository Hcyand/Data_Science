"""
离差标准化至[0,1]
"""
import pandas as pd

filename = 'business_circle.xls'
standardizedfile = 'standardized.xls'
data = pd.read_excel(filename, index_col='基站编号')
data = (data - data.min()) / (data.max() - data.min())
data = data.reset_index()
data.to_excel(standardizedfile, index=False)
