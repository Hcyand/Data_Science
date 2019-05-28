"""
地方财政收入神经网络预测模型
"""
import pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense, Activation
import matplotlib.pyplot as plt

inputfile = 'data1_GM11.xls'
outputfile = 'revenue.xls'
modelfile = '1-net.model'
data = pd.read_excel(inputfile)
feature = ['x1', 'x2', 'x3', 'x4', 'x5', 'x7']

# range返回列表，不能用来key
data_train = data.loc[:19].copy()  # 取2014年以前的数字及前20个数据
data_mean = data_train.mean()
data_std = data_train.std()
data_train = (data_train - data_mean) / data_std
x_train = data_train[feature].values
y_train = data_train['y'].values

model = Sequential()
model.add(Dense(12, input_dim=6))
model.add(Activation('relu'))
model.add(Dense(1, input_dim=12))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x_train, y_train, nb_epoch=1000, batch_size=16)  # 训练1000 次
model.save_weights(modelfile)  # 保存模型

x = ((data[feature] - data_mean[feature]) / data_std[feature]).values
data['y_pred'] = model.predict(x) * data_std['y'] + data_mean['y']  # 预测值
data.to_excel(outputfile)

p = data[['y', 'y_pred']].plot(subplots=True, style=['b-o', 'r-*'])
plt.show()
