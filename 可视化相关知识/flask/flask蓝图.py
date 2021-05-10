from flask import Flask
from admin.admin import admin as Admin_blue
from front.front import front as Front_blue

app = Flask(__name__)
# 注册
app.register_blueprint(Admin_blue)
app.register_blueprint(Front_blue)

if __name__ == '__main__':
    app.run(debug=True)