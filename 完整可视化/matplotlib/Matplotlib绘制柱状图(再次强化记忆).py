import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir("E:/input/清晰图表数据(matplotlib)")
text =  pd.read_csv("柱状图+散点图.csv")

test1 = text.groupby("品牌名称").sum()["成交金额"]
x_data = test1.index
y_data1 = test1.values
test2 = text.groupby("品牌名称").sum()["成本金额"]
y_data2 = test2.values
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# 将数据转化成类型为<class 'numpy.ndarray'>的数组索引
index = np.arange(len(x_data))
print(type(index))

plt.figure(figsize=(6.48,4.8),dpi=120,facecolor="white")
plt.title("各品牌的成交,成本金额")
plt.xlabel("品牌名称")
plt.ylabel("金额")

plt.bar(x_data,y_data1,align="center",width=0.40,label="成交金额")
plt.bar(index+0.40,y_data2,align="center",width=0.40,label="成本金额")
plt.legend(loc="best")
plt.show()