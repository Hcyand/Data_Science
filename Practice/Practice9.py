# 第十章：数据工作
# 专家更依赖数据，而非主观判断
# 10.1：探索数据
# 10.1.1 探索一维数据
import random
import datetime
from numpy import *
from collections import Counter
from matplotlib import pyplot as plt
from Practice.Practice5 import inverse_normal_cdf
from Practice.Practice4 import correlation


def bucketize(point, bucket_size):
    return bucket_size * math.floor(point / bucket_size)


def make_histogram(points, bucket_size):
    return Counter(bucketize(point, bucket_size) for point in points)


def plot_histogram(points, bucket_size, title=""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()


# random.seed(0)作用：使得随机数据可预测，即只要seed的值一样，后续生成的随机数都一样
random.seed(0)
# -100到100之间均匀抽取
uniform = [200 * random.random() - 100 for _ in range(10000)]
# 均值为0标准差为57的正态分布
noraml = [57 * inverse_normal_cdf(random.random()) for _ in range(10000)]


# 均匀分布直方图
# plot_histogram(uniform, 10, "均匀分布的直方图")
# plot_histogram(noraml,10,"正态分布的直方图")


# 10.1.2 二维数组
def random_normal():
    return inverse_normal_cdf(random.random())


# 伪数据集
xs = [random_normal() for _ in range(1000)]
ys1 = [x + random_normal() / 2 for x in xs]
ys2 = [-x + random_normal() / 2 for x in xs]
plt.scatter(xs, ys1, marker='.', color='black', label='ys1')
plt.scatter(xs, ys2, marker='.', color='gray', label='ys2')
plt.xlabel('xs')
plt.ylabel('ys')
plt.legend(loc=9)
plt.title("差别很大的联合分布")
print(correlation(xs, ys1))
print(correlation(xs, ys2))
plt.show()


# 10.1.3 多维数组
# 了解各个维度如何相关， 考察相关矩阵，矩阵第i行j列的元素表示第i维和第j维的相关性
# def correlation_matrix(data):
#     _, num_columns = shape(data)
#     def matrix_entry(i,j):
#         return correlation(get_column(data,i),get_column(data,j))
#     return make_matrix(num_columns,num_columns,matrix_entry)

# 维度不多时，做散点图矩阵，通过plt.subplots()可以生成子图
# 学会阅读散点图矩阵


# 10.2 清理与修改的重要性
# 一系列解析器
# 用None表示对这列什么都不做
def parse_row(input_row, parsers):
    return [try_or_none(parser)(value) if parser is not None else value
            for value, parser in zip(input_row, parsers)]


def parse_rows_with(reader, parsers):
    for row in reader:
        yield parse_row(row, parsers)


def try_or_none(f):
    def f_or_none(x):
        try:
            return f(x)
        except:
            return None

    return f_or_none


# 10.3 数据处理
# 数据处理的基本目的是从大量的、可能是杂乱无章的、难以理解的数据中抽取并推导出对于某些特定的人们来说是有价值、有意义的数据
data = [
    {'closing_price': 102.06,
     'date': datetime.datetime(2014, 8, 29, 0, 0),
     'symbol': 'AAPL'
     }
    # ...
]
# 我们想知道AAPL有史以来最高的收盘价
# （1）将数据限定在AAPL行上
# （2）从每行中提取出收盘价closing_price
# （3）取价格中的最大值max
max_aapl_price = max(row["closing_price"]
                     for row in data
                     if row["symbol"] == "AAPL")

# 数据集中每一只股票的最高收盘价
# （1）聚集起股票代码（symbol）相同的行
# （2）在每一组中重复之前的工作
# 按股票代码对行分组
by_symbol = dict(list)
for row in data:
    by_symbol[row["symbol"]].append(row)
# 使用字典解析找到每个股票代码的最大值
max_price_by_symbol = {symbol: max(row["closing_price"] for row in grouped_rows)
                       for symbol, grouped_rows in by_symbol.items()}


# 每日百分比变动的最大值和最小值分别是什么（price_today/price_yesterday -1）
# (1)按照日期排列价格
# (2)通过命令zip得到配对价格（前一天的，今天的）
# (3)将配对价格转换为新的"百分比变动"行
# def percent_price_change(yesterday, today):
#     return today["closing_price"] / yesterday["closing_price"] - 1
#
#
# def day_over_day_changes(grouped_rows):
#     # 按照日期进行排序
#     ordered = sorted(grouped_rows, key=picker("date"))

# 10.4 数据调整
# 许多数据对数据单位敏感
# 比如:百位数据科学家的身高和体重的数据集，需要创建体型大小的聚类
# 单位变化导致结果发生变化，需要对数据进行调整
# 使得每个维度均值都为0，标准差都为1


# 10.5降维
# 降维多用于维数很高的情形
# 主成分分析（PCA）
