# 使用Pygal模拟掷骰子
# 创建Die()类，包含__init__()方法--骰子默认面数和roll()方法返回随机数，randint类
# 掷骰子：创建骰子D6，投掷结果存入数列当中，显示结果
# 分析结果，各点数出现的次数。遍历点数+count统计出现次数+append加入同一个数列
# 绘制直方图，hist = pygal.Bar()(进行可视化） title/x_labels/add/render_to_file（svg图片）

from random import randint
import pygal


class Die():
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


die_1 = Die()
die_2 = Die()
results = []
for roll_num in range(100000):
    result_1 = die_1.roll()
    result_2 = die_2.roll()
    result = result_1 + result_2
    results.append(result)

times = []
for sides in range(2, die_1.num_sides + die_2.num_sides + 1):
    time = results.count(sides)
    times.append(time)

hist = pygal.Bar()

hist.title = "test1"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "num"

hist.add('D6', times)
hist.render_to_file('test2.svg')

print(times)
