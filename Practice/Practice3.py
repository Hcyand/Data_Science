# 创建Randomwalk()类 --   三个属性    --  包含__init__() & fill_walk() 两个方法
# 方法__init__()中包含初始地址/多少个点/属性
# 方法fill_walk()生成漫步的点，决定漫步的方向，前进的距离，拒绝原地踏步，前进的点以及加入数组当中
# 绘制随机漫步图：创建实例，绘制出图像
from random import choice
import matplotlib.pyplot as plt
import numpy as np


class RandomWalk():
    def __init__(self, num=6000):
        self.num = num
        self.x = [0]
        self.y = [0]

    def fill_walk(self):
        while len(self.x) < self.num:
            x_choice = choice([-2, -1, 0, 1, 2])
            y_choice = choice([-2, -1, 0, 1, 2])
            if x_choice == 0 and y_choice == 0:
                continue
            # -1是因为要和最后一个值相加
            next_x = self.x[-1] + x_choice
            next_y = self.y[-1] + y_choice
            self.x.append(next_x)
            self.y.append(next_y)


# True大写开头！
while True:
    rw = RandomWalk()
    # 生成漫步的点才能绘制
    rw.fill_walk()
    point = np.arange(rw.num)
    plt.scatter(rw.x, rw.y, c=point, cmap=plt.cm.Blues, s=10)
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.x[-1], rw.y[-1], c='red', edgecolors='none', s=50)
    plt.show()

    again = input("Do it again?(y/n)：")
    if again == 'n':
        break

# 1.模拟多次随机漫步
#   处于活动状态，输入（input）n停止
# 2.给点着色，重新绘制起点和终点，隐藏坐标轴，增加点数
#   arange以及numpy   起点和终点绿色和红色加粗
#   隐藏坐标轴plt.axes().get_yaxis().set_visible(False)
# 3.调整尺寸适合屏幕
#   figure(figsize=(
