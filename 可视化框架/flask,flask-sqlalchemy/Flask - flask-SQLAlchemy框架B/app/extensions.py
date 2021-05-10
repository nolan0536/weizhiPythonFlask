from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


# 创建对象
bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()
migrate = Migrate(db=db)

# 初始化
def config_extensions(app):
    bootstrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)