from .main import index

BLUE_PRINT_CONFIG = (
    (index,""),
)

def config_blueprint(app):
    for blueName,Conf in BLUE_PRINT_CONFIG:
        app.register_blueprint(blueName,url_prefix=Conf)