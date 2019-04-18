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
# import random
#
#
# def split_data(data, prob):
#     results = [], []
#     for row in data:
#         results[0 if random.random() < prob else 1].append(row)
#     return results
#
#
# def train_test_split(x, y, test_pct):
#     data = zip(x, y)
#     train, test = split_data(data, 1 - test_pct)
#     x_train, y_train = zip(*train)
#     x_test, y_test = zip(*test)
#     return x_train, y_train, x_test, y_test
#
#
# model = SomeKindOfMode()
# x_train, x_test, y_train, y_test = train_test_split(xs, yx, 0.33)
# model.tarin(x_train, y_train)
# performance = model.test(x_test, y_test)

# 11.4正确性
# 真阳性：邮件是垃圾邮件，预测正确
# 假阳性（第1类错误）：邮件不是垃圾邮件，预测是垃圾邮件
# 假阴性（第2类错误）：邮件是垃圾邮件，预测不是垃圾邮件
# 真阴性：邮件不是垃圾邮件，预测正确


# （1）准确率：
def accuracy(tp, fp, fn, tn):
    correct = tp + tn
    total = tp + fp + fn + tn
    return correct / total


# （2）查准率：
def precision(tp, fp, fn, tn):
    return tp / (tp + fp)


# （3）查全率：
def recall(tp, fp, fn, tn):
    return tp / (tp + fn)


# （4）查准率和查全率的调和平均数
def f1_score(tp, fp, fn, tn):
    p = precision(tp, fp, fn, tn)
    r = recall(tp, fp, fn, tn)
    return 2 * p * r / (p + r)


print(accuracy(70, 4930, 13930, 981070))
print(precision(70, 4930, 13930, 981070))
print(recall(70, 4930, 13930, 981070))
print(f1_score(70, 4930, 13930, 981070))

# 11.5偏倚-方差权衡
# 高偏倚低方差——欠拟合；高方差低偏倚——过拟合
# 高偏倚应当加入更多特征；高方差应当移除特征或者获得更多数据

# 11.6特征提取和选择
# 特征的选择，需要经验和专业的结合

