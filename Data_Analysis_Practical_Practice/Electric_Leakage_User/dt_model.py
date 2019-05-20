"""
原始数据分为训练数据和测试数据
构建CART决策树模型
绘制ROC曲线
"""
import pandas as pd
import matplotlib.pyplot as plt
from random import shuffle  # 导入随机函数shuffle，用来打散数据
from sklearn.metrics import roc_curve  # 导入ROC曲线函数
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib

inputfile = 'model.xls'
data = pd.read_excel(inputfile)
data = data.values  # 将表格转化为矩阵
shuffle(data)  # 随机打乱数据

p = 0.8
train = data[:int(len(data) * p), :]  # 前80%为训练集
test = data[int(len(data) * p):, :]  # 后20%为测试集

treefile = 'tree.pkl'
tree = DecisionTreeClassifier()
tree.fit(train[:, :3], train[:, 3])

# 保存模型
joblib.dump(tree, treefile)


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


cm_plot(train[:, 3], tree.predict(train[:, :3])).show()

# 绘制ROC曲线函数
fpr, tpr, thresholds = roc_curve(test[:, 3], tree.predict_proba(test[:, :3])[:, 1], pos_label=1)
plt.plot(fpr, tpr, linewidth=2, label='ROC of LM')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.xlim(0, 1.05)
plt.ylim(0, 1.05)
plt.legend(loc=4)
plt.show()
