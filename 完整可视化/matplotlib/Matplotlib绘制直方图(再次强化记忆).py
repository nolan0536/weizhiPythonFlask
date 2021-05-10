import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir("E:/input/清晰图表数据(matplotlib)")
Data = pd.read_csv("直方图+散点图.csv",encoding="gbk")

x_data = Data["最低分"]
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

plt.figure(figsize=(6.48,4.8),dpi=120,facecolor="white")
plt.title("2020年各高校各专业最低分频率直方图")
plt.xlabel("最低分")
plt.hist(x_data,bins=30,color="blue",edgecolor="black",density=True,alpha=0.5,label="最低分")
x_data.plot(kind="kde",color="red",xlim=[450,700],label="核密度图")
plt.legend(loc="best")
plt.show()
