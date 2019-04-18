# 第五章：统计学
# 代码练习
from collections import Counter
import math


# 均值练习
def mean(v):
    return sum(v) / len(v)


# 寻找中位数函数median
def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2

    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        high = sorted_v[midpoint]
        lower = sorted_v[midpoint - 1]
        return (high + lower) / 2


# 分位数练习
# p为概率
def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(p_index)


# 众数练习
# item字典
def mode(x):
    counts = Counter(x)
    max_counts = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_counts]


# 极差练习
def data_range(x):
    return max(x) - min(x)


# 方差练习
# 点乘
def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


# 平方
def sum_of_squares(v):
    return dot(v, v)


# x减平均值
def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


# 求方差：衡量每一个变量对均值的偏离程度
# n - 1 的原因是因为样本方差的计算，需要减去1
def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)


# 标准差
def standard_deviation(x):
    return math.sqrt(variance(x))


# 相关：相关是由协方差除以两个变量的标准差
# 协方差：衡量两个变量对均值的串联偏离程度
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)


# 相关系数处于1到-1之间，1为正完全相关，-1为负完全相关
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0

# 很多时候会有异常值对结果进行影响，需要检查数据消除异常值
# 可以通过可视化数据判断是否存在异常值
# 找出异常项，将其排除
# outlier = num_friend.index(100) # outlier的索引
# num_friends_good = [x for i,x in enumerate(num_friends) if i != outlier]
# daily_minutes_good = [x for i,x in enumerate(daily_minutes) if i != outlier]

# 辛普森悖论
# 相关系数
# 相关和因果
