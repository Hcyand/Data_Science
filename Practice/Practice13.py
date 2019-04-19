# 第14章：简单线性回归
# 14.1模型
from Practice.Practice4 import correlation, standard_deviation, mean


# 线性模型y=βx+α+误差项，即计算alpha和beta
def predict(alpha, beta, x_i):
    return beta * x_i + alpha


# 计算误差
def error(alpha, beta, x_i, y_i):
    return y_i - predict(alpha, beta, x_i)


# 误差的平方求和
def sum_of_squared_errors(alpha, beta, x, y):
    return sum(error(alpha, beta, x_i, y_i) ** 2
               for x_i, y_i in zip(x, y))


# 最小二乘法选择alpha和beta
def least_squared_fit(x, y):
    beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
    alpha = mean(y) - beta * mean(x)
    return beta, alpha
