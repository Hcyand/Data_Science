# 第七章：假设与推断
# 案例：掷硬币

import math
from Practice.Practice5 import normal_cdf, inverse_normal_cdf


# X的二项式随机变量可用用正态分布拟合
def normal_approximation_to_binomial(n, p):
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma


# 正态cdf是一个变量在一个阈值以下的概率
normal_probability_blow = normal_cdf


# 阈值以上概率
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)


# 区间内概率
def normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)


# 区间外概率
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)


# 均值为中心，覆盖60%可能性的区间，上尾和下尾都是20%
def normal_upper_bound(probability, mu=0, sigma=1):
    return inverse_normal_cdf(probability, mu, sigma)


def normal_lower_bound(probability, mu=0, sigma=1):
    return inverse_normal_cdf(1 - probability, mu, sigma)


def normal_two_sided_bounds(probability, mu=0, sigma=1):
    mid_probability = (1 - probability) / 2
    upper_bound = normal_lower_bound(mid_probability, mu, sigma)
    lower_bound = normal_upper_bound(mid_probability, mu, sigma)
    return lower_bound, upper_bound


mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
low, high = normal_two_sided_bounds(0.95, mu_0, sigma_0)
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)
# 通过设定的假设不同，有时进行单边假设：例如5%的检验找出小于95%的概率来
high2 = normal_upper_bound(0.95, mu_0, sigma_0)
type_2_probability = normal_probability_blow(high2, mu_1, sigma_1)


# 硬币是否均匀的两面检验
def two_sides_p_value(x, mu=0, sigma=1):
    if x >= mu:
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        return 2 * normal_probability_blow(x, mu, sigma)


# 已知准确精度，计算其执行区间
# 已知1000次中出现525次正面朝上
p_hat = 525 / 1000
mu_2 = p_hat
sigma_2 = math.sqrt(mu_2 * (1 - mu_2) / 1000)


# 案例：运行A/B测试
# 广告A和广告B的p是否相等
# 原假设为A，B的p相等
def estimated_parameters(N, n):
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma


def a_b_test_statistic(N_A, n_A, N_B, n_B):
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)


z = a_b_test_statistic(1000, 200, 1000, 180)
w = a_b_test_statistic(1000, 200, 1000, 150)
print(two_sides_p_value(z))  # 0.254无法拒绝原假设
print(two_sides_p_value(w))  # 0.003可以拒绝原假设

# 贝叶斯推断：存在先验分布和后验分布
