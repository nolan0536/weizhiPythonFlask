import os

class Config():
    # 密钥
    SECRET_KEY = "JDK123"
    # 信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 额外初始化
    @staticmethod
    def init_app(app):
        pass

class DeveConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/mart?charset=utf8"

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/mart?charset=utf8"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/mart?charset=utf8"

config = {
    "deve":DeveConfig,
    "testing":TestingConfig,
    "production":ProductionConfig,
    "default":DeveConfig
}