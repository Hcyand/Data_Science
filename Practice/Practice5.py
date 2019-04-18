# 第六章：概率
# 独立与不独立
# 条件概率
# （1）两个孩子都是女孩并且大孩子是女孩的概率
# （2）两个孩子都是女孩并且至少一个孩子是女孩的概率
# -*- coding: utf-8 -*-
import random
import math
from matplotlib import pyplot as plt
# 显示中文
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


# def random_kid():
#     return random.choice(["boy", "girl"])
#
#
# both_girls = 0
# old_girl = 0
# either_girl = 0
#
# random.seed(0)
# for _ in range(1000):
#     younger = random_kid()
#     older = random_kid()
#     if younger == "girl" and older == "girl":
#         both_girls += 1
#     if older == "girl":
#         old_girl += 1
#     if younger == "girl" or older == "girl":
#         either_girl += 1
#
# print('p(both/older):', both_girls / old_girl)
# print('p(both/either', both_girls / either_girl)


# 贝叶斯定理
# 随机变量
# 连续分布
# 正态分布:钟形曲线形态分布函数：均值和标准差两个参数决定

# def normal_pdf(x, mu=0, sigma=1):
#     sqrt_two_pi = math.sqrt(2 * math.pi)
#     return (math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))
#
#
# xs = [x / 10.0 for x in range(-50, 50)]
# plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
# plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='mu=0,sigma=2')
# plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
# plt.plot(xs, [normal_pdf(x, mu=-1, sigma=1) for x in xs], '-.', label='mu=-1,sigma=1')
# plt.legend()
# plt.title("多个正态分布的概率密度函数")
# plt.show()


# 标准正态分布的累积分布函数，python中可用math.erf描述
def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


# xs = [x / 10.0 for x in range(-50, 50)]
# plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
# plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label='mu=0,sigma=2')
# plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='mu=0,sigma=0.5')
# plt.plot(xs, [normal_cdf(x, mu=1) for x in xs], '-.', label='mu=1,sigma=1')
# plt.legend(loc=4)  # 底部右边
# plt.title("多个正态分布的累积分布函数")
# plt.show()


# 因为normal_cdf严格递增，寻找特定的概率可同个二分法查找
# p为所查找的概率，必须符合标准型
def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    # 如果非标准型，先调整单位使之服从标准型
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    # -10.0接近0概率，10.0解决1概率
    low_z, low_p = -10.0, 0
    hi_z, hi_p = 10.0, 1
    while hi_z - low_z > tolerance:
        mid_z = (hi_z + low_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            hi_z, hi_p = mid_z, mid_p
        else:
            break
    return mid_z
