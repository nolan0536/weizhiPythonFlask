from flask import Flask,render_template

app = Flask(__name__)
@app.route("/Text")
def Text():
    user = "Admin"
    tap = ['laowang',21,1988,"zhongguo"]
    lit = {"name":"猫哥","password":1236789}
    # 接收参数
    return render_template("timg1.html",user = user,tap = tap,lit = lit)

if __name__ == '__main__':
    app.run(debug=True)