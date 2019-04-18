# 第11章：机器学习
# 很多人眼里，数据科学就是机器学习，数据科学家每天做的事情就是建立，训练和调整机器学习模型
# 数据科学的主要内容：收集数据，理解数据，清理数据，整理数据格式 + 机器学习
# 11.1建模
# 针对存在不同变量之间的数字（或概率）联系的一种规范
# 11.2机器学习
# 创建并使用那些由学习数据而得到的模型
# 11.3 过拟合和欠拟合
# 过拟合：训练数据上表现良好，但是对任何新数据的泛化能力很差的模型
# 欠拟合：训练数据和新数据上都没有好的表现
# 划分数据集，三分之二用来训练模型，三分之一来衡量模型表现
import random


def split_data(data, prob):
    results = [], []
    for row in data:
        results[0 if random.random() < prob else 1].append(row)
    return results


def train_test_split(x, y, test_pct):
    data = zip(x, y)
    train, test = split_data(data, 1 - test_pct)
    x_train, y_train = zip(*train)
    x_test, y_test = zip(*test)
    return x_train, y_train, x_test, y_test


model = SomeKindOfMode()
x_train, x_test, y_train, y_test = train_test_split(xs, yx, 0.33)
model.tarin(x_train, y_train)
performance = model.test(x_test, y_test)
