import matplotlib.pyplot as plt

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs', 'cats', 'fish'
sizes = [15, 30, 15, 25, 5, 10]
explode = (0, 0.1, 0, 0, 0, 0)
fig1, ax1 = plt.subplots()
# 切片标签/自动标记百分比/下拉阴影/逆时针旋转90度开始/突出某块区域
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')
plt.show()
