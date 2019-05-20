"""
原始数据分为训练数据和测试数据
构建LM神经网络模型
绘制ROC曲线
"""
import pandas as pd
import matplotlib.pyplot as plt
from random import shuffle  # 导入随机函数shuffle，用来打散数据
from keras.models import Sequential  # 导入神经网络初始化函数
from keras.layers.core import Dense, Activation  # 导入神经网络层函数，激活函数
from sklearn.metrics import roc_curve  # 导入ROC曲线函数

inputfile = 'model.xls'
data = pd.read_excel(inputfile)
data = data.values  # 将表格转化为矩阵
shuffle(data)  # 随机打乱数据

p = 0.8
train = data[:int(len(data) * p), :]  # 前80%为训练集
test = data[int(len(data) * p):, :]  # 后20%为测试集

netfile = 'net.model'
net = Sequential()  # 建立神经网络
net.add(Dense(input_dim=3, output_dim=10))  # 输入层和输出层
net.add(Activation('relu'))  # 隐藏层使用relu函数
net.add(Dense(input_dim=10, output_dim=1))  # 输入层和输出层
net.add(Activation('sigmoid'))  # 输出层使用sigmoid函数
net.compile(loss='binary_crossentropy', optimizer='adam')  # 编译模型，使用adam方法求解

net.fit(train[:, :3], train[:, 3], epochs=20, batch_size=1)  # 训练模型，1000次
net.save_weights(netfile)  # 保存模型

predict_result = net.predict_classes(train[:, :3]).reshape(len(train))  # 预测结果变形


def cm_plot(y, yp):
    from sklearn.metrics import confusion_matrix

    cm = confusion_matrix(y, yp)

    import matplotlib.pyplot as plt
    plt.matshow(cm, cmap=plt.cm.Greens)
    plt.colorbar()

    for x in range(len(cm)):
        for y in range(len(cm)):
            plt.annotate(cm[x, y], xy=(x, y), horizontalalignment='center', verticalalignment='center')

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    return plt


cm_plot(train[:, 3], predict_result).show()

# 绘制ROC曲线函数
predict_result = net.predict(test[:, :3]).reshape(len(test))
fpr, tpr, thresholds = roc_curve(test[:, 3], predict_result, pos_label=1)
plt.plot(fpr, tpr, linewidth=2, label='ROC of LM')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.xlim(0, 1.05)
plt.ylim(0, 1.05)
plt.legend(loc=4)
plt.show()
