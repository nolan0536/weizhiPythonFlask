import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pymysql

db = pymysql.connect(host="localhost",user="root",password="123456",port=3306,db="mart",charset="utf8")
cursor = db.cursor()
sql = "select * from monthlysale"
cursor.execute(sql)
datas = cursor.fetchall()

test1 = []
test2 = []
test3 = []
for tmp in datas:
    test1.append(tmp[0])
    test2.append(float(tmp[3]))
    test3.append(float(tmp[4]))

text1 = pd.DataFrame(test1)
text2 = pd.DataFrame(test2)
text3 = pd.DataFrame(test3)

x_data = text1[0]
y_data1 = text2[0]
y_data2 = text3[0]

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

plt.figure(figsize=(6.48,4.8),dpi=120,facecolor="white") # 设置图像各属性的开始代码
plt.title("id的sale,cost的变化")
plt.xlabel("id")
plt.plot(x_data,y_data1,color="blue",ls="--",lw=1.2,label="sale")
plt.plot(x_data,y_data2,ls=":",lw=1.2,label="cost")
plt.legend(loc="best")
plt.show()
