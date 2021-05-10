import os


class Config:
    # 密钥
    SECRET_KEY = "IOT952"
    # 连接数据库信息
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True    # sqlalchemy_commit_on_teardown
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # sqlalchemy_track_modifications
    # 额外的初始化
    @staticmethod
    def init_app(app):
        pass


class DeveplomentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/dataName"


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://takeout:takeout@168.159.11.20:3306/takeout"

class ProdumentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://takeout:takeout@168.159.11.20:3306/takeout"


config = {
    "deveploment":DeveplomentConfig,
    "testing":TestingConfig,
    "produment":ProdumentConfig,
    "default":DeveplomentConfig
}