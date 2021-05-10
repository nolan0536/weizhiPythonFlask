from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)
# 配置连接数据库的参数
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:123123@localhost:3306/mysql7"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config.from_object(config) # 先指定配置类
dp = SQLAlchemy(app) # 再创建数据库链接

class Demo1(dp.Model):
    # 设置表名称
    __tablename__ = "jaront"
    # 设置对应字段
    id = dp.Column(dp.Integer(),primary_key = True,autoincrement=True)
    name = dp.Column(dp.String(16))
    gender = dp.Column(dp.String(8))

#dp.drop_all() #删除数据表
dp.create_all() # 创建数据表

# flask实例化,将数据库中的数据传送至前端
@app.route("/index",methods = ["GET","POST"])
def index():
    test1 = Demo1() # 返回一个列表
    # print(test1)
    test2 = test1.query.all() #列表中的元素为字典
    # print(test2)
    return render_template("demo1.html",test2 = test2)

if __name__ == '__main__':
    app.run(debug=True)