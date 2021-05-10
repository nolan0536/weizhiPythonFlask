import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

labels = np.array(['上限流量','下限流量'])
datalenth = 2

os.chdir(r"E:\input")
demo = pd.read_csv("Test_tow.csv",encoding="gbk")
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
arr1 = pd.DataFrame(demo)
dataLen = len(arr1)
angles = np.linspace(0,2*np.pi,dataLen,endpoint=False)
print(arr1["下限流量"])
arr2 = demo["上限流量"]
arr3 = demo["下限流量"]
data1 = np.concatenate((arr2,[arr2[0]])) # 闭合
data2 = np.concatenate((arr3,[arr3[0]])) # 闭合
pl = plt.polar(data1,data2)
plt.fill(data1,data2,facecolor = "purple",alpha = 0.8)

plt.show()