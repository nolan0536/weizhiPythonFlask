import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir(r"E:\input")
# 获取数据
demo1 = pd.read_excel("Text_tow.xls")
# 解乱码问题
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# 设置图像大小,分辨率,外围颜色
plt.figure(figsize=(6.84,4.8),dpi=120,facecolor="white")
# 绘制散点图
# x轴数据,y轴数据,s散点大小,c散点颜色,marker点的形状,alpha透明度设置,linewidths点边框宽度,edgecolors点边框颜色
plt.scatter(x=demo1["编号"],y = demo1["下限流量"],s = 10,c = "purple",marker = "o",alpha = 0.8,\
            linewidths = 1.2,edgecolors="green",label="下限流量")
plt.title("下限流量与编号之间的关系")
plt.xlabel("编号",fontsize = 10)
plt.ylabel("下限流量",fontsize = 10)
# 设置图例显示
plt.legend(loc="best")
# plt.savefig(r"E:\output\可视化8.pdf")
plt.show()