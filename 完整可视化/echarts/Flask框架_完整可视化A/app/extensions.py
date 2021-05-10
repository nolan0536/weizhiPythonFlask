
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_migrate import Migrate

bootstrap = Bootstrap()
db = SQLAlchemy()
moment = Moment()
migrate = Migrate(db=db)

def config_extensions(app):
    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)
    migrate.init_app(app)