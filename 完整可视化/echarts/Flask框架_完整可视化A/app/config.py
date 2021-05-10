import os


# 设置配置
class Config:
    # 密钥
    SECRET_KEY = "KPL1186"
    # 信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 自动提交配置
    # 额外的初始化
    @staticmethod
    def init_app(app):
        pass

# 设置环境
class DeveplotmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/restaurant"
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/restaurant"
class PromomentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/restaurant"
# 配置字典
config = {
    "deveplotment":DeveplotmentConfig,
    "testingConfig":TestingConfig,
    "promoment":PromomentConfig,
    "default":DeveplotmentConfig
}