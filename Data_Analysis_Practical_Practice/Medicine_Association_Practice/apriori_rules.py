"""
Apriori关联规则算法
"""
from __future__ import print_function
from Data_Analysis_Practical_Practice.Medicine_Association_Practice.apriori import *  # 导入自行编写的高效的Apriori函数
import time

inputfile = 'apriori.txt'
data = pd.read_csv(inputfile, header=None, dtype=object)

start = time.clock()
print('转换原始数据至0-1矩阵...')
ct = lambda x: pd.Series(1, index=x[pd.notnull(x)])  # 转换0-1矩阵的过渡函数，即将标签数据转换为1
# map() 会根据提供的函数对指定序列做映射。
b = map(ct, data.values)
data = pd.DataFrame(b).fillna(0)  # 实现矩阵转换，除1外，其余为空，空值用0填补
end = time.clock()
print('\n转换完毕，用时：%0.2f秒' % (end - start))
del b  # 删除中间变量b，节省内存

support = 0.06  # 最小支持度
confidence = 0.75  # 最小置信度
ms = '---'

start = time.clock()
print('\n开始搜索关联规则...')
find_rule(data, support, confidence, ms)
end = time.clock()
print('\n搜索完成，用时：%0.2f秒' % (end - start))
