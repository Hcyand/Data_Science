"""
地方财政收入灰色预测
"""
import pandas as pd
from Data_Analysis_Practical_Practice.Revenue_Analysis.GM11 import GM11

inputfile = 'data1.csv'
outputfile = 'data1_GM11.xls'
modelfile = 'net.model'
data = pd.read_csv(inputfile)
data.index = range(1994, 2014)

data.loc[2014] = None
data.loc[2015] = None
l = ['x1', 'x2', 'x3', 'x4', 'x5', 'x7']
for i in l:
    f = GM11(data[i][:-2].values)[0]
    data[i][2014] = f(len(data) - 1)
    data[i][2015] = f(len(data))
    data[i] = data[i].round(2)
data[l + ['y']].to_excel(outputfile)
