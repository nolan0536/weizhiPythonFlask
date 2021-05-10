import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
"""
    雷达图没有标题
"""

os.chdir("E:/input/清晰图表数据(matplotlib)")

Data = pd.read_csv("雷达图+饼状图.csv",encoding="gbk")

test1 = Data["部门"]
test2 = Data["预计开销"]
test3 = Data["实际开销"]

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

plt.figure(figsize=(6.48,4.8),dpi=110,facecolor="white")
# 闭合
arr1 = np.concatenate((test1,[test1[0]]))
arr2 = np.concatenate((test2,[test2[0]]))
arr3 = np.concatenate((test3,[test3[0]]))
# 设置边框
plt.polar(arr1,arr2,arr3)

# 填充
plt.fill(arr1,arr2,color="purple",alpha=0.5,label="预计开销")
plt.fill(arr1,arr3,color="green",alpha=0.6,label="实际开销")
plt.legend(loc="upper left")
plt.show()