import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,98,1998)
# print(x)
y = np.sin(x),
# 配置信息
plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False
# 设置图像
plt.figure(figsize=(6.4,4.84),dpi=120,facecolor="white")
# 图像标题
plt.title("可视化图像")
# 坐标轴名称
plt.xlabel("x")
plt.ylabel("y")
# x与y的关系
plt.xlim(0,1.45)
plt.ylim(0,1.45)
# 轴刻度
plt.xticks([0,0.25,0.5,0.75,1.0,1.25,1.50])
plt.yticks([0,0.25,0.5,0.75,1.0,1.25,1.50])
# 设置图像上线条和点的属性
plt.plot(x,y,c = "blue",lw = 1.2,ls = "--",marker = "v",markersize = "1",markeredgecolor = "red",\
         markerfacecolor = "purple",label = "y = x^2")
# 图例显示
plt.legend(loc = "best") # best 最好的.
# 图像保存
# plt.savefig(r"E:\output\可视化2.pdf")
# 图像展示
plt.show()