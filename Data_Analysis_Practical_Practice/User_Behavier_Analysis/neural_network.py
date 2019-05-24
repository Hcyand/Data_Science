"""训练多重神经网络"""
from __future__ import print_function
import pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation

inputfile1 = 'train_neural_network_data.xls'
inputfile2 = 'test_neural_network_data.xls'
testoutputfile = 'test_output_file.xls'
data_train = pd.read_excel(inputfile1)
data_test = pd.read_excel(inputfile2)
y_train = data_train.iloc[:, 4].values
x_train = data_train.iloc[:, 5:17].values
y_test = data_test.iloc[:, 4].values
x_test = data_test.iloc[:, 5:17].values

model = Sequential()
model.add(Dense(input_dim=11, output_dim=17))
model.add(Activation('relu'))
model.add(Dense(input_dim=17, output_dim=10))
model.add(Activation('relu'))
model.add(Dense(input_dim=10, output_dim=1))
model.add(Activation('sigmoid'))
# 编译模型，损失函数为binary_crossentroy,用adam法求解
model.compile(loss='binary_crossentropy', optimizer='adam')
model.fit(x_train, y_train, nb_epoch=100, batch_size=1)  # 训练模型
model.save_weights('net.model')  # 保存模型参数

r = pd.DataFrame(model.predict_classes(x_test), columns=['预测结果'])
pd.concat([data_test.iloc[:, :5], r], axis=1).to_excel(testoutputfile)
model.predict(x_test)
