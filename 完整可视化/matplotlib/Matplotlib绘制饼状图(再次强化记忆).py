import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir("E:/input/清晰图表数据(matplotlib)")
Data = pd.read_csv("雷达图+饼状图.csv")

x_data = Data["部门"]
y_data = Data["实际开销"]
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

plt.figure(figsize=(6.48,4.8),dpi=110,facecolor="white")
plt.title("各部门实际开销所占百分比")
plt.pie(y_data,labels=x_data,shadow=True,radius=1.0,autopct="%.2f%%",startangle=0,explode=[0,0,0,0.05,0.07,0])
plt.legend(loc="upper left")
plt.show()