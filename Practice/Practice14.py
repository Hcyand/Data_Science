# 第15章：多重回归分析
from Practice.Practice4 import dot
from Practice.Practice7 import minimize_stochastic
from Practice.Practice13 import total_sum_of_squares
import random


# beta = [alpha,beta_1,...,beta_k]
# x_i = [1,x_i1,...,x_ik]
def predict(x_i, beta):
    return dot(x_i, beta)


# 保证模型的有效性：1.x和各列都是线性无关的；2.x的各列与误差都无关

# 拟合模型（梯度下降寻找）
def error(x_i, y_i, beta):
    return y_i - predict(x_i, beta)


def squared_error(x_i, y_i, beta):
    return error(x_i, y_, beta) ** 2


def squared_error_gradient(x_i, y_i, beta):
    return [-2 * x_ij * error(x_i, y_i, beta) for x_ij in x_i]


def estimate_beta(x, y):
    beta_initial = [random.random() for x_i in x[0]]
    return minimize_stochastic(squared_error, squared_error_gradient, x, y, beta_initial, 0.001)


# 解释模型
# 拟合优度,发现优度上升
def mulyiple_r_squared(x, y, beta):
    sum_of_squared_errors = sum(error(x_i, y_i, beta) ** 2 for x_i, y_i in zip(x, y))
    return 1.0 - sum_of_squared_errors / total_sum_of_squares(y)
