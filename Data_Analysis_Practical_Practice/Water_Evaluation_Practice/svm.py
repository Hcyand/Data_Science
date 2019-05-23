"""
数据抽取代码
特征区间范围太小，得到的区分度会比较小，因此所有特征同意乘以一个适当的k，从而提高区分度和准确度（k=30左右合适）
支持向量机学习：
"""
import pandas as pd
from random import shuffle
from sklearn import svm
from sklearn import metrics

inputfile = 'moment.csv'
outputfile1 = 'cm_train.xls'
outputfile2 = 'cm_test.xls'
data = pd.read_csv(inputfile, encoding='gbk')  # 读取数据，指定编码为gbk
data = data.values
shuffle(data)

data_train = data[:int(0.8 * len(data)), :]
data_test = data[int(0.8 * len(data)):, :]

# 构造特征和标签
x_train = data_train[:, 2:] * 30
y_train = data_train[:, 0].astype(int)
x_test = data_test[:, 2:] * 30
y_test = data_test[:, 0].astype(int)

# 建立训练模型
model = svm.SVC()
model.fit(x_train, y_train)
cm_train = metrics.confusion_matrix(y_train, model.predict(x_train))  # 训练样本的混淆矩阵
cm_test = metrics.confusion_matrix(y_test, model.predict(x_test))  # 测试样本的混淆矩阵
# 保存结果
pd.DataFrame(cm_train, index=range(1, 4), columns=range(1, 4)).to_excel(outputfile1)
pd.DataFrame(cm_test, index=range(1, 5), columns=range(1, 5)).to_excel(outputfile2)
