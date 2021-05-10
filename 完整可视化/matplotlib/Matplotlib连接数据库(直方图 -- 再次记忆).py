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
for tmp in datas:
    test1.append(float(tmp[3]))

text1 = pd.DataFrame(test1)

x_data = text1[0]
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.figure(figsize=(6.48,4.8),dpi=120,facecolor="white")
plt.title("sale分布直方图")
plt.hist(x_data,bins=30,color="purple",edgecolor="black",alpha=0.5,density=True,label="sale")
x_data.plot(kind="kde",xlim=[8000,23000],color="red",label="核密度图")
plt.legend(loc="best")
plt.show()


