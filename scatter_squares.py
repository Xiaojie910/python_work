import matplotlib.pyplot as plt

x_values = list(range(1,6))
y_values = [x**3 for x in x_values]
plt.scatter(x_values,y_values,edgecolor="none",s=40,c=x_values,cmap=plt.cm.Reds)

#设置图表的标题和坐标轴的标签
plt.title("Square numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
plt.axis([0,6,0,130])
plt.show()

