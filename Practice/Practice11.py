# 第12章：K近邻法
# 12.1 模型
# （1）某种距离的概念（2）一种彼此接近的点具有相似性质的假设
from collections import Counter
from matplotlib import pyplot as plt
from Practice.Practice4 import distance, mean
import random


def raw_majority_vote(labels):
    votes = Counter(labels)
    # 返回一个TopN列表。如果n没有被指定，则返回所有元素。当多个元素计数值相同时，排列是无确定顺序的
    winner, _ = votes.most_common(1)[0]
    return winner


# 当具有相同票数时，三种解决方案
# 1.随机选择一个 2.根据距离加权并选择加权的获胜者
# 3.减少k值知道找到唯一获胜者，我们运用第三种
def majority_vote(labels):
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count for count in vote_counts.values()
                       if count == winner_count])
    if num_winners == 1:
        return winner
    else:
        return majority_vote(labels[:-1])  # 去掉最远元素


# 创建分类器
def knn_classify(k, labeled_points, new_point):
    # 给标记好的点从近到远的顺序排序
    by_distance = sorted(labeled_points,
                         key=lambda point, _: distance(point, new_point))
    # 寻找k个最近的标签
    k_nearest_labels = [label for _, label in by_distance[:k]]
    return majority_vote(k_nearest_labels)


# 12.2案例：最喜欢的编程语言
cities = [(-86.75, 33.5666666666667, 'Python'),
          (-88.25, 30.6833333333333, 'Python'),
          (-112.016666666667, 33.4333333333333, 'Java'),
          (-110.933333333333, 32.1166666666667, 'Java'),
          (-92.2333333333333, 34.7333333333333, 'R'),
          (-121.95, 37.7, 'R'),
          (-118.15, 33.8166666666667, 'Python'),
          (-118.233333333333, 34.05, 'Java'),
          (-122.316666666667, 37.8166666666667, 'R'),
          (-117.6, 34.05, 'Python'),
          (-116.533333333333, 33.8166666666667, 'Python'),
          (-121.5, 38.5166666666667, 'R'),
          (-117.166666666667, 32.7333333333333, 'R'),
          (-122.383333333333, 37.6166666666667, 'R'),
          (-121.933333333333, 37.3666666666667, 'R'),
          (-122.016666666667, 36.9833333333333, 'Python'),
          (-104.716666666667, 38.8166666666667, 'Python'),
          (-104.866666666667, 39.75, 'Python'),
          (-72.65, 41.7333333333333, 'R'),
          (-75.6, 39.6666666666667, 'Python'),
          (-77.0333333333333, 38.85, 'Python'),
          (-80.2666666666667, 25.8, 'Java'),
          (-81.3833333333333, 28.55, 'Java'),
          (-82.5333333333333, 27.9666666666667, 'Java'),
          (-84.4333333333333, 33.65, 'Python'),
          (-116.216666666667, 43.5666666666667, 'Python'),
          (-87.75, 41.7833333333333, 'Java'),
          (-86.2833333333333, 39.7333333333333, 'Java'),
          (-93.65, 41.5333333333333, 'Java'),
          (-97.4166666666667, 37.65, 'Java'),
          (-85.7333333333333, 38.1833333333333, 'Python'),
          (-90.25, 29.9833333333333, 'Java'),
          (-70.3166666666667, 43.65, 'R'),
          (-76.6666666666667, 39.1833333333333, 'R'),
          (-71.0333333333333, 42.3666666666667, 'R'),
          (-72.5333333333333, 42.2, 'R'),
          (-83.0166666666667, 42.4166666666667, 'Python'),
          (-84.6, 42.7833333333333, 'Python'),
          (-93.2166666666667, 44.8833333333333, 'Python'),
          (-90.0833333333333, 32.3166666666667, 'Java'),
          (-94.5833333333333, 39.1166666666667, 'Java'),
          (-90.3833333333333, 38.75, 'Python'),
          (-108.533333333333, 45.8, 'Python'),
          (-95.9, 41.3, 'Python'),
          (-115.166666666667, 36.0833333333333, 'Java'),
          (-71.4333333333333, 42.9333333333333, 'R'),
          (-74.1666666666667, 40.7, 'R'),
          (-106.616666666667, 35.05, 'Python'),
          (-78.7333333333333, 42.9333333333333, 'R'),
          (-73.9666666666667, 40.7833333333333, 'R'),
          (-80.9333333333333, 35.2166666666667, 'Python'),
          (-78.7833333333333, 35.8666666666667, 'Python'),
          (-100.75, 46.7666666666667, 'Java'),
          (-84.5166666666667, 39.15, 'Java'),
          (-81.85, 41.4, 'Java'),
          (-82.8833333333333, 40, 'Java'),
          (-97.6, 35.4, 'Python'),
          (-122.666666666667, 45.5333333333333, 'Python'),
          (-75.25, 39.8833333333333, 'Python'),
          (-80.2166666666667, 40.5, 'Python'),
          (-71.4333333333333, 41.7333333333333, 'R'),
          (-81.1166666666667, 33.95, 'R'),
          (-96.7333333333333, 43.5666666666667, 'Python'),
          (-90, 35.05, 'R'),
          (-86.6833333333333, 36.1166666666667, 'R'),
          (-97.7, 30.3, 'Python'), (-96.85, 32.85, 'Java'),
          (-95.35, 29.9666666666667, 'Java'),
          (-98.4666666666667, 29.5333333333333, 'Java'),
          (-111.966666666667, 40.7666666666667, 'Python'),
          (-73.15, 44.4666666666667, 'R'),
          (-77.3333333333333, 37.5, 'Python'),
          (-122.3, 47.5333333333333, 'Python'),
          (-89.3333333333333, 43.1333333333333, 'R'),
          (-104.816666666667, 41.15, 'Java')
          ]
# 预测没有调查的地方最喜欢的语言
# 键时语言，值是成对的数据（longitudes，latitudes）
plots = {"Java": ([], []), "Python": ([], []), "R": ([], [])}
# 对每一种语言都有不同的标记和颜色
markers = {"Java": "o", "Python": "s", "R": "^"}
colors = {"Java": "r", "Python": "b", "R": "g"}

for (longitude, latitude), language in cities:
    plots[language[0]].append(longitude)
    plots[language[1]].append(latitude)
# 对每种语言创建一个散点序列
for language, (x, y) in plots.items():
    plt.scatter(x, y, colors=colors[language], marker=markers[language],
                label=language, zorder=10)


# plot_state_borders(plt) # 假设有一个实现这一步的函数(github上)
# plt.legend(loc=0)
# plt.axis([-130, -60, 20, 55])  # 设置轴
# plt.title("最受欢迎的编程语言")
# plt.show()


# 利用临近的城市预测每个城市的偏爱的语言
# for k in [1, 3, 5, 7]:
#     num_correct = 0
#     for city in cities:
#         location, actual_language = city
#         other_cities = [other_city for other_city in cities if other_city != city]
#         predicted_language = knn_classify(k, other_cities, location)
#         if predicted_language == actual_language:
#             num_correct += 1
#     print(k, "neighbor[s]:", num_correct, "correct out of", len(cities))


# 12.3 维度灾难
# 观察维度灾难的一种方法：高纬度空间随机生成数据点对，计算之间距离
def random_point(dim):
    return [random.random() for _ in range(dim)]


# 生成距离
def random_distance(dim, num_pairs):
    return [distance(random_point(dim), random_point(dim)) for _ in range(num_pairs)]


dimensions = range(1, 100)
avg_distances = []
min_distances = []
random.seed(0)
for dim in dimensions:
    distances = random_distance(dim, 10000)
    avg_distances.append(mean(distances))
    min_distances.append(min(distances))
# 随着维度数量的增加，点和点直接的平均距离增加
# 当维度增加后，相邻点距离小不能说明什么了
# 随着维度的增加，点也更加稀疏了，出现更多的空白地段
