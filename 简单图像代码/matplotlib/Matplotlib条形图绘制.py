import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir(r"E:\input")
# 获取数据
demo1 = pd.read_excel("Text_tow.xls")
# 分组
demo2 = demo1.groupby("id").mean()["上限流量"]
# 设置x,y
print(demo2)
x_data = demo2.values
print(x_data)
y_data = demo2.index
print(y_data)
# 解决乱码问题
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# 绘制条形图
# x = range(0,len(x_data))设置数据长度,height设置y轴数据,width设置条形图宽度,color设置条形图填充颜色
# linewidth设置条形图边框宽度,edgecolor设置条形图边框颜色,tick_label设置条形图刻度标签,align设置x轴上对齐方式
plt.bar(x = range(0,len(x_data)),height = x_data,width=0.8,color = "orange",linewidth = 1.1,\
        edgecolor = "black",tick_label = y_data,align="center")
# 设置标题
plt.title("上限流量统计",pad=15)
# 设置坐标轴名称
plt.xlabel("id",labelpad=5)
plt.ylabel("上限流量",labelpad=5)
# 设置储存位置
# plt.savefig("E:\output\可视化4.pdf")
# 图像展示
plt.show()