"""
逻辑回归分析，特征筛选
F检验：
稳定性选择：
    通过检查特征在被检查的特征子集中的被选择为最重要的次数。
    我们可以预期，最强大的特征的出现次数将达到100%，因为他们总是在可能的情况下被选择到；
    较弱但是也比较相关的特征的将具有一个非零的数字，因为当在当前选择的子集中不存在较强特征时将选择它们，
    而不相关特征将具有零分（接近于零），因为它们将永远不会被选中特征。
递归特征消除：
    递归特征消除是重复构建模型（比如SVM或者回归模型），然后选择表现最佳或最差的特征（比如基于corr），
    把特征放在一遍，然后重复该过程。对这个过程一直进行重复，直到数据集中的所有特征都用尽，然后根据特征被消除的先后顺序进行排序。
    所以这是一种寻找最佳特征子集的贪婪算法。
"""
# 稳定性选择方法 随机逻辑回归
# 逻辑回归 自动建模
import pandas as pd
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR

filename = 'bankloan.xls'
data = pd.read_excel(filename)
x = data.iloc[:, :8].as_matrix()
y = data.iloc[:, 8].as_matrix()


rlr = RLR()
rlr.fit(x, y)
rlr.get_support()
print('通过随机逻辑回归模型筛选特征结束')
print('有效特征为：%s' % ','.join(data.columns[rlr.get_support()]))
x = data[data.columns[rlr.get_support()]].as_matrix()

lr = LR()
lr.fit(x, y)
print('逻辑回归模型训练结束')
print('模型平均正确率：%s' % lr.score(x, y))
