import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir(r"E:\input")
# list1 = np.array([["数学","语文","英语","综合","总分"],["94","97","56","213","460",],["61","83","29","156","329"],\
#                   ["78","82","73","177",'410'],["84","96","90","146","416"],["91","99","30","231","451"]]);
# list2 = list1.groupby("综合").mean("总分")
# print(list2)
demo1 = pd.read_csv("工作簿1.csv",encoding = "gbk",na_values="-")
demo2 = demo1.groupby("班级").mean()["总分"]
print(demo2)
x_data = demo2.values # 获取列的数据
y_data = demo2.index # 获取行的数据
print(x_data)
print(y_data)
explode = [0,0.1,0.2] # 突出显示饼的形状
colors = ["red","blue","purple"] # 每个饼的颜色.
plt.rcParams["font.sans-serif"] = ["SimHei"] # 解决乱码问题
plt.rcParams["axes.unicode_minus"] = False
# autopct 数据显示格式,pctdistance 设置百分比标签(百分比数据距圆心距离),labeldistance 设置文本标签距圆心的距离
# startangle 设置饼图初始角度,radius 设置饼图半径,counterclock 是否逆时针,wedgeprops中linewidth设置饼图边框宽度、edgecolor设置边框颜色
# textprops 设置文本信息: fontsize 字体大小、color 字体颜色,shadow 设置图像是否有阴影
plt.pie(x = x_data,explode = explode,labels = y_data,colors = colors,autopct="%.1f%%",pctdistance=0.5,\
        labeldistance=1.1,startangle=120,radius=1.2,counterclock=False,wedgeprops={"linewidth":1.5,"edgecolor":"white"},\
        textprops={"fontsize":10,"color":"black"},shadow=True)
# 设置标题,pad 设置标题与饼图的间隔距离
plt.title("各班分数比例",pad=30)
# plt.savefig("E:\output\可视化5.pdf")
plt.show()