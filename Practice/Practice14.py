# 第15章：多重回归分析
from Practice.Practice4 import dot, median
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


# 15.6 Bootstrap:利用bootstrap来获得新的数据集，即选择n个数据点代替原来的数据，然后合成的数据集的中位数
# 即每n个数据点得到一个中位数，再将多个中位数组成一个数据集，得出最后的中位数
def bootstrap_sample(data):
    return [random.choice(data) for _ in data]


def bootstrap_statistic(data, stats_fn, num_samples):
    return [stats_fn(bootstrap_sample(data)) for _ in range(num_samples)]


# 检验：101个点都很接近100
close_to_100 = [99.5 + random.random() for _ in range(101)]
# 检验：101个点，50个接近0，50个接近200
far_from_100 = [[99.5 + random.random()] +
                [random.random() for _ in range(50)] +
                [200 + random.random() for _ in range(50)]]

print(bootstrap_statistic(close_to_100, median, 100))
print(bootstrap_statistic(far_from_100, median, 100))


# 15.7 回归系数的标准误差
# 估计回归系数的标准误差：对数据进行重复采样
def estimate_sample_beta(sample):
    x_sample, y_sample = zip(*sample)  # 魔法般的解压方式
    return estimate_beta(x_sample, y_sample)

# 15.8 正则化
# 正则化是指给误差项添加一个惩罚项，并且该惩罚项会随beta的增大而增大
# 例如岭回归:是一种专用于共线性数据分析的有偏估计回归方法，实质上是一种改良的最小二乘估计法，通过放弃最小二乘法的无偏性，
# 以损失部分信息、降低精度为代价获得回归系数更为符合实际、更可靠的回归方法，对病态数据的拟合要强于最小二乘法。
