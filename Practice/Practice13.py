# 第14章：简单线性回归
# 14.1模型
from Practice.Practice4 import correlation, standard_deviation, mean, de_mean


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


# 决定系数或R平方，更好的指标来评估模型对数据的拟合效果
# R的平方越大，模型对数据的拟合度越高
def total_sum_of_squares(y):
    return sum(v ** 2 for v in de_mean(y))


def r_squared(alpha, beta, x, y):
    return 1.0 - (sum_of_squared_errors(alpha, beta, x, y) / total_sum_of_squares(y))


# 14.2利用梯度下降法
def squared_error(x_i, y_i, theta):
    alpha, beta = theta
    return error(alpha, beta, x_i, y_i) ** 2


def squared_error_gradient(x_i, y_i, theta):
    alpha, beta = theta
    return [-2 * error(alpha, beta, x_i, y_i),  # alpha偏导数
            -2 * error(alpha, beta, x_i, y_i) * x_i]  # beta偏导数

# 14.3最大似然估计
