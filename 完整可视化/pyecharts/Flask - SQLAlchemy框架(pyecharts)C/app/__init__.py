from flask import Flask
from app.config import config
from app.settings import config_setting
from app.views import config_blueprint

def create_app(config_name):
    # Flask实例化
    app = Flask(__name__)
    # 初始化配置信息
    app.config.from_object(config.get(config_name))
    # 调用初始化函数
    config[config_name].init_app(app)
    # 配置扩展
    config_setting(app)
    # 配置蓝图
    config_blueprint(app)

    return app