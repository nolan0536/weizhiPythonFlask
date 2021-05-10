import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pymysql

db = pymysql.connect(host="localhost",user="root",password="123456",port=3306,db="web_01",charset="utf8")
cursor = db.cursor()
sql = "select * from iphone_de"
cursor.execute(sql)
datas = cursor.fetchall()

test1 = []
test2 = []
for tmp in datas:
    test1.append(tmp[5])
    test2.append(tmp[4])

text1 = pd.DataFrame(test1)
text2 = pd.DataFrame(test2)

x_data = text1[0]
y_data = text2[0]
cursor.close()
db.close()

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.figure(figsize=(6.48,4.8),dpi=110,facecolor="white")
plt.title("编号与流量的散点图")
plt.xlabel("编号")
plt.ylabel("流量")
plt.scatter(x=x_data,y=y_data,color="green",alpha=0.5,label="散点")
plt.legend(loc="best")
plt.show()