import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pymysql

db = pymysql.connect(host="localhost",user="root",password="123456",port=3306,db="web_01",charset="utf8")
cursor = db.cursor()
sql = "select * from fill_radar"
cursor.execute(sql)
datas = cursor.fetchall()

test1 = []
test2 = []
test3 = []
for tmp in datas:
    test1.append(tmp[0])
    test2.append(int(tmp[1]))
    test3.append(int(tmp[2]))

text1 = pd.DataFrame(test1)
text2 = pd.DataFrame(test2)
text3 = pd.DataFrame(test3)

x_data = text1[0]
y_data1 = text2[0]
y_data2 = text3[0]
cursor.close()
db.close()

# 闭合
arr1 = np.concatenate((x_data,[x_data[0]]))
arr2 = np.concatenate((y_data1,[y_data1[0]]))
arr3 = np.concatenate((y_data2,[y_data2[0]]))

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.figure(figsize=(6.48,4.8),dpi=110,facecolor="white")
# 设置边框
plt.polar(arr1,arr2,arr3)
# 填充
plt.fill(arr1,arr2,color="green",alpha=0.5,label="预计开销")
plt.fill(arr1,arr3,color="orange",alpha=0.5,label="实际开销")
plt.legend(loc="upper left")
plt.show()