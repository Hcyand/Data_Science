"""
决策树方法
ID3算法，C4.5算法，CART算法
ID3算法简介和基本原理：
    在每个非叶节点选择信息增益最大的属性作为测试属性->较小的决策树
    核心在于决策树的各级节点上都用信息增益作为判断标准进行属性的选择
    属性进行离散化
ID3算法具体流程：
    1.对当前样本集合，计算所有属性的信息增益
    2.选择信息增益最大的属性作为测试属性，把测试属性取值相同的样本划分为同一个子样本集
    3.若子样本集的类别属性只含有单个属性，则分支为叶子节点，判断其属性值并标上相应的符号，
        然后返回调用处；否则对子样本集递归调用本算法
"""
# ID3决策树算法预测销量高低
import pandas as pd
from sklearn.tree import export_graphviz
from sklearn.tree import DecisionTreeClassifier as DTC

# 参数初始化
filename = 'sales_data.xls'
data = pd.read_excel(filename, index_col=u'序号')

# 数据是类别标签，将它转换为数据
# 用1来表示“好”，“是”，“高”三个属性，用-1来表示想反属性
data[data == u'好'] = 1
data[data == u'是'] = 1
data[data == u'高'] = 1
data[data != 1] = -1
x = data.iloc[:, :3].astype(int)
y = data.iloc[:, 3].astype(int)

dtc = DTC()  # 建立决策树模型，基于信息嫡
dtc.fit(x, y)  # 训练模型

# 导入相关数据，可视化决策树
# 导出的结果是一个dot文件，需要安装Graphviz才能将它转换为pdf或者png格式
with open('tree.dot', 'w') as f:
    f = export_graphviz(dtc, feature_names=x.columns, out_file=f)
