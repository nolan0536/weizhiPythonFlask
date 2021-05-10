from flask import Flask,render_template

# render_template 渲染模板
app = Flask(__name__,template_folder="templates") # template_folder 调用静态文件.

@app.route("/")
def index():
    return render_template("timg.html")

if __name__ == '__main__':
    app.run(debug=True)