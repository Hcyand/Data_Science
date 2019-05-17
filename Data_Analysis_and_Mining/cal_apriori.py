"""
使用Apriori算法挖掘菜品订单关联规则，算法
"""
from __future__ import print_function
from Data_Analysis_and_Mining.apriori import *  # 导入自行编导的apriori函数
import pandas as pd

inputfile = 'menu_orders.xls'
outputfile = 'apriori_rules.xls'  # 结果文件
data = pd.read_excel(inputfile, header=None)

print('\n转换原始数据至0-1矩阵')
ct = lambda x: pd.Series(1, index=x[pd.notnull(x)])  # 转换0-1矩阵的过渡函数
b = map(ct, data.as_matrix())  # 用map方式执行
data = pd.DataFrame(list(b)).fillna(0)  # 实现矩阵转换，空值用0填充
print('\n转换完毕')
del b  # 删除中间

support = 0.2  # 最小支持度
confidence = 0.5  # 最小置信度
ms = '---'  # 连接符，默认‘---’，用来区分不同元素
find_rule(data, support, confidence, ms).to_excel(outputfile)  # 保存结果
