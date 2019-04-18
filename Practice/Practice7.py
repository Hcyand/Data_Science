# 梯度下降
# 简单函数
from functools import partial  # partial为偏函数
from matplotlib import pyplot as plt
import random


def sum_of_squares(v):
    return sum(v_i ** 2 for v_i in v)


# 导数表示
def difference_quotient(f, v, h):
    return (f(v + h) - f(v)) / h


# 差商近似值的拟合度
def square(v):
    return v * v


def derivative(v):
    return 2 * v


def step(v, direction, step_size):
    return [v_i + step_size * direction_i for v_i, direction_i in zip(v, direction)]


def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]


# 安全应用函数，对无效输入值返回无限值
def safe(f):
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf')  # python中的无限值
        return safe_f()


# 随机梯度下降
# 随机序列迭代
def in_random_order(data):
    indexes = [i for i, _ in enumerate(data)]
    random.shuffle(indexes)  # shuffle() 方法将序列的所有元素随机排序
    for i in indexes:
        # yield 的作用就是把一个函数变成一个 generator
        # generator最重要的原因是可以按需生成并“返回”结果，而不是一次性产生所有
        yield data[i]


def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    data = zip(x, y)
    theta = theta_0
    alpha = alpha_0
    min_theta, min_value = None, float('inf')
    iterations_with_no_improvement = 0
    # 如果循环超过100次仍无法改进，停止
    while iterations_with_no_improvement < 100:
        value = sum(target_fn(x_i, y_i, theta) for x_i, y_i in data)
        if value < min_value:
            # 如果找到新的值，记住它
            # 并返回最初的步长
            min_theta, min_value = theta, value
            iterations_with_no_improvement = 0
            alpha = alpha_0
        else:
            # 尝试缩小步长，否则没有改进
            iterations_with_no_improvement += 1
            alpha *= 0.9
        # 在每个数据点上向梯度方向前进一步
        for x_i, y_i in in_random_order(data):
            gradient_i = gradient_fn(x_i, y_i, theta)
        #  theta = vector_subtract(theta,scalar_multiply(alpha,gradient_i))
    return min_theta
