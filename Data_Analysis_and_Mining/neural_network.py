"""
神经网络算法预测销量高低
"""
# 内存不足！！！问题？？？
import pandas as pd
from Data_Analysis_and_Mining.cm_plot import *
from keras.models import Sequential
from keras.layers.core import Dense, Activation

inputfile = 'sales_data.xls'
data = pd.read_excel(inputfile, index_col='序号')

data[data == '好'] = 1
data[data == '是'] = 1
data[data == '高'] = 1
data[data != 1] = 0
x = data.iloc[:, :3].astype(int)
y = data.iloc[:, 3].astype(int)

model = Sequential()
model.add(Dense(3, 10))
model.add(Activation('relu'))
model.add(Dense(10, 1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', class_mode='binary')
model.fit(x, y, nb_epoch=1000, batch_size=10)
yp = model.predict_classes(x).reshape(len(y))

cm_plot(y, yp).show()
