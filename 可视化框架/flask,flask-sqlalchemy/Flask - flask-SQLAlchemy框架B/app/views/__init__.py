from .main import index

DEFAULT_BLUEPRINT = (
    (index,""),
)


def config_blueprint(app):
    for bluename,prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(bluename,url_prefix=prefix)