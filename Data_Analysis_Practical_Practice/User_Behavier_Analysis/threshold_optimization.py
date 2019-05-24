"""
寻找阈值最优
"""
import numpy as np
import pandas as pd

inputfile = 'water_heater.xls'
n = 4  # 使用以后四个点的平均斜率

threshold = pd.Timedelta(minutes=5)  # 专家阈值
data = pd.read_excel(inputfile)
data['发生时间'] = pd.to_datetime(data['发生时间'], format='%Y%m%d%H%M%S')
data = data[data['水流量'] > 0]


def event_num(ts):
    d = data['发生时间'].diff() > ts  # 相邻时间差分，比较是否大于阈值
    return d.sum() + 1  # 直接返回事件数


dt = [pd.Timedelta(minutes=i) for i in np.arange(1, 9, 0.25)]
h = pd.DataFrame(dt, columns=['阈值'])  # 定义阈值列
h['事件数'] = h['阈值'].apply(event_num)  # 计算每个阈值对于的事件数
h['斜率'] = h['事件数'].diff() / 0.25  # 计算每两个相邻点对于的斜率
h['斜率指标'] = h['斜率'].abs().rolling(n).mean()  # 采用后n个的斜率绝对值的平均数作为斜率指标
ts = h['阈值'][h['斜率指标'].idxmin() - n]  # 返回中最小index，由于rolling(n).mean()自动计算的是前n个斜率的绝对值，需要进行平移
if ts > threshold:
    ts = pd.Timedelta(minutes=4)
print(ts)
