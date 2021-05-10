from flask import Flask,redirect,url_for

app = Flask(__name__)
@app.route("/jar/<string:username>")
def jar(username):

    return "Hello %s" %username

@app.route("/home1")
def home1():
    # 打印路名名称 url_for可传函数名、变量
    print(url_for("home1"))
    # 重定向
    return redirect(url_for("jar",username = "老猫"))
if __name__ == '__main__':
    app.run(debug=True)