from flask_migrate import Migrate
from flask_moment import Moment
from flask_bootstrap import Bootstrap

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# 创建对象
moment = Moment()
bootstrap = Bootstrap()
migrate = Migrate()

# 创建引擎
engine = create_engine("mysql+pymysql://root:123456@localhost:3306/mart?charset=utf8")
# 创建基类
Base = declarative_base()
# 创建Session对象
Session = sessionmaker(bind=engine)
# 产生会话
session = Session()

# 初始化
def config_setting(app):
    moment.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app)