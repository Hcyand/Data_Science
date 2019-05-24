"""
划分一次用水事件
判断流水记录是否属于同一次用水事件，通过间隔时间来判断
"""
import pandas as pd

# 阈值为四分钟
threshold = pd.Timedelta(minutes=4)
inputfile = 'water_heater.xls'
outputfile = 'dividsequence.xls'
data = pd.read_excel(inputfile)
data['发生时间'] = pd.to_datetime(data['发生时间'], format='%Y%m%d%H%M%S')
data = data[data['水流量'] > 0]  # 只要水流量大于0的数据
d = data['发生时间'].diff() > threshold  # 相邻时间做差分，比较是否大于阈值
data['事件编号'] = d.cumsum() + 1  # 通过累计求和的方式为事件编号
data.to_excel(outputfile)
