import os

class Config:

    # 密钥
    SECRET_KEY = "GDK1889"
    # 信号
    SQLALCHEMY_TARCK_MODIFICATIONS = False
    # 禁止自动提交数据处理 sqlalchemy_commit_on_teardown
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    # 额外的初始化
    @staticmethod
    def init_app(app):
        pass

# 开发环境
class DeveplomentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/web_01?charset=utf8"

# 测试环境
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/web_01?charset=utf8"

# 生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/web_01?charset=utf8"

config = {
    "deveploment":DeveplomentConfig,
    "testing":TestingConfig,
    "production":ProductionConfig,
    "default":DeveplomentConfig
}