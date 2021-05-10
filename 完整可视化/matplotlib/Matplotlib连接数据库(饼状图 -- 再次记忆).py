import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pymysql

db = pymysql.connect(host="localhost",user="root",password="123456",port=3306,db="mart",charset="utf8")
cursor = db.cursor()
sql = "select * from cardsum_copy"
cursor.execute(sql)
datas = cursor.fetchall()

test1 = []
test2 = []
for tmp in datas:
    test1.append(tmp[1])
    test2.append(tmp[2])

text1 = pd.DataFrame(test1)
text2 = pd.DataFrame(test2)

x_data = text1[0]
y_data = text2[0]

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.figure(figsize=(6.48,4.8),dpi=110,facecolor="white")
plt.title("各grade的sum的百分比")
plt.pie(y_data,labels=x_data,shadow=True,radius=1.0,autopct="%.2f%%",startangle=0,explode=[0.03,0,0,0])
plt.legend("upper left")
plt.show()