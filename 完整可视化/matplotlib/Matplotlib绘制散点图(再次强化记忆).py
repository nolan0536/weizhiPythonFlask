import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir("E:/input/清晰图表数据(matplotlib)")

Data = pd.read_csv("直方图+散点图.csv",encoding="gbk")
Text = Data.groupby("BB").mean()["招录人数"]
x_data = Text.index
y_data = Text.values
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

plt.figure(figsize=(6.8,4.8),dpi=120,facecolor="white")
plt.title("BB和AVG招录人数的散点图")
plt.xlabel("BB")
plt.ylabel("招录人数")
plt.scatter(x=x_data,y=y_data,color="purple",marker="o",alpha=0.5,label="AVG招录人数")
plt.legend(loc="best")
plt.show()