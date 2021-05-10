import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir(r"E:\input")
# 获取数据
data = pd.read_csv("工作簿1.csv",encoding = "gbk",na_values="-")
# 解决乱码问题
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# print(data["总分"].value_counts())
# 绘制直方图
# x = 设置x轴数据,bins 设置条形数目,color 设置条形颜色,edgecolor 设置边框颜色,density 是否以频数展示
# alpha设置条形透明度
plt.hist(x=data["总分"],bins=30,color="purple",edgecolor = "black",alpha = 0.8,density=True)

plt.title("2019年下学期思政总分分布图")
plt.legend("best")
# plt.savefig(r"E:\output\可视化6.pdf")
plt.show()