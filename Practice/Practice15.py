# 第16章：逻辑回归
# 16.1 问题
# 取值为0（非付费用户）和1（付费用户）
# 用线性回归不能很好的解决问题了。
# 16.2 Logistic函数
import math
import random
from Practice.Practice4 import dot, vector_add
from functools import reduce, partial


# 函数
def logistic(x):
    return 1.0 / (1 + math.exp(x))


# 导数
def logistic_prime(x):
    return logistic(x) * (1 - logistic(x))


# 最大化似然函数
def logistic_log_likelihood_i(x_i, y_i, beta):
    if y_i == 1:
        return math.log(logistic(dot(x_i, beta)))
    else:
        return math.log(1 - logistic(dot(x_i, beta)))


# 各个对数似然之和
def logistic_log_likilihood(x, y, beta):
    return sum(logistic_log_likelihood_i(x_i, y_i, beta) for x_i, y_i in zip(x, y))


# 计算梯度
def logistic_log_partial_ij(x_i, y_i, beta, j):
    return (y_i - logistic(dot(x_i, beta))) * x_i[j]


def logistic_log_gradient_i(x_i, y_i, beta):
    return [logistic_log_partial_ij(x_i, y_i, beta, j) for j, _ in enumerate(beta)]


def logistic_log_gradient(x, y, beta):
    return reduce(vector_add, [logistic_log_gradient_i(x_i, y_i, beta) for x_i, y_i in zip(x, y)])


# 16.3 应用模型
# ...
# 16.4 拟合优度
# true_positives = false_positives = true_negatives = false_negatives = 0
# for x_i, y_i in zip(x_test, y_test):
#     predict = logistic(dot(beta_hat, x_i))
#     if y_i == 1 and predict >= 0.5:
#         true_positives += 1
#     elif y_i == 1:
#         false_negatives += 1
#     elif predict >= 0.5:
#         false_positives += 1
#     else:
#         true_negatives += 1
# 再计算查准率和查全率

# 16.5 支持向量机
# 即寻找将距离每个类别中的最近点的距离最大化的平面
# 寻找一个超平面的过程就是最优化的过程
