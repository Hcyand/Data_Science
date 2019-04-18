# 第三章：可视化数据
# 可视化数据练习
from matplotlib import pyplot as plt
from collections import Counter

# 线图1
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
plt.title("名义GDP")
plt.ylabel("十亿美元")
plt.show()


# 线图2
# variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
# bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
# total_error = [x + y for x, y in zip(variance, bias_squared)]
# xs = [i for i, _ in enumerate(variance)]
# plt.plot(xs, variance, 'g-', label='variance')
# plt.plot(xs, bias_squared, 'r-.', label='bias^2')
# plt.plot(xs, total_error, 'b:', label='total error')
#
# loc=9指的是“顶部中央”
# plt.legend(loc=9)
# plt.xlabel('model complex')
# plt.title('picture')
# plt.show()


# 条形图
# 可自动居中，不需要调节
# movies = ["annie hall", "ben-hur", "casablance", "gandhi", "west side story"]
# num_oscars = [5, 11, 3, 8, 10]
# plt.bar(movies, num_oscars)
# plt.title(" my favorite movies")
# plt.ylabel("num_oscars")
# plt.show()


# 条形图2
# grades = [83, 95, 91, 70, 0, 85, 82, 100, 67, 73, 77, 0]
# decile = lambda grade: grade // 10 * 10
# histogram = Counter(decile(grade) for grade in grades)
# plt.bar(histogram.keys(), histogram.values(), 8)
# plt.axis([-5, 105, 0, 5])
# plt.xticks([10 * i for i in range(11)])
# plt.xlabel('grade')
# plt.ylabel('num_student')
# plt.show()

# 散点图
# friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
# minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# plt.scatter(friends, minutes)
# 给每个点加上标记
# for label, friend_count, minute_count in zip(labels, friends, minutes):
#     plt.annotate(label,
#                  xy=(friend_count, minute_count),
#                  xytext=(5, -5),
#                  textcoords='offset points')
# plt.title('number')
# plt.xlabel('friend number')
# plt.show()
