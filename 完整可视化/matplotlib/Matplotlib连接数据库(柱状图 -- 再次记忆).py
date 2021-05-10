import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pymysql

db = pymysql.connect(host="localhost",user="root",password="123456",port=3306,db="mart",charset="utf8")
cursor = db.cursor()
sql = "select * from cardsum"
cursor.execute(sql)
datas = cursor.fetchall()

test1 = []
test2 = []
test3 = []
for tmp in datas:
    test1.append(tmp[1])
    test2.append(int(tmp[2]))
    test3.append(float(tmp[3]))

text1 = pd.DataFrame(test1)
text2 = pd.DataFrame(test2)
text3 = pd.DataFrame(test3)

x_data = text1[0]
y_data1 = text2[0]
y_data2 = text3[0]
print(y_data2)

index = np.arange(len(x_data))

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

plt.figure(figsize=(6.48,4.8),dpi=120,facecolor="white")
plt.title("sum和percent")
plt.xlabel("grade")
plt.bar(x_data,y_data1,width=0.4,align="center",label="sum")
plt.bar(index+0.4,y_data2,width=0.4,align="center",label="percent")
plt.legend(loc="best")
plt.show()
