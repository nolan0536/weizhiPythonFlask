from flask import Flask

app = Flask(__name__)

# 添加多个路由
@app.route("/index") # 路由名称:index
@app.route("/") # 添加路由
def index():
    return "<h1>index page</h1>"

# 接收数据类型
# String 默认类型, int, float, path(路径),uuid

@app.route("/home/<path:username>") # 路由名称:home
def home(username):
    print(username,type(username))
    return "home page"

# 接收多个参数
@app.route("/user/<float:userkd>/<int:userid>")
def user(userkd,userid):
    print(userkd)
    print(userid,type(userid))
    return "<h1 style='color:purple;'> user page</h1>"

# 添加路由第二种方式
def spark(fakname):
    return "spark page %s"%fakname
app.add_url_rule(rule="/spark/<string:fakname>",view_func=spark)

if __name__ == '__main__':
    app.run(debug=True)