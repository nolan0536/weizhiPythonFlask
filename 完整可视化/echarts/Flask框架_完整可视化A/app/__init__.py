from flask import Flask
from app.config import config
from app.extensions import config_extensions
from app.views import config_blueprint


def create_app(config_name):
    # 创建应用实例
    app = Flask(__name__)
    # 初始化配置
    app.config.from_object(config.get(config_name) or config["default"])
    # 调用初始化函数
    config[config_name].init_app(app)
    # 配置扩展
    config_extensions(app)
    # 配置蓝图
    config_blueprint(app)
    return app