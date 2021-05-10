import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir("E:/input/清晰图表数据(matplotlib)")

test1 = pd.read_csv("折线图.csv",encoding="gbk")

x_data = test1["品牌"]
y_data1 = test1["成本"]
y_data2 = test1["利润"]

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

plt.figure(figsize=(6.48,4.8),dpi=120,facecolor="white")
plt.title("各品牌利润和成本")
plt.xlabel("品牌")
plt.ylabel("金额")

plt.plot(x_data,y_data1,ls="--",lw=1.3,color="purple",label="成本")
plt.plot(x_data,y_data2,ls="-",lw=1.2,color="blue",label="利润")
plt.legend(loc="best")
plt.show()