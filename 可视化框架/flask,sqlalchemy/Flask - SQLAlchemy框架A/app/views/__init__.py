from .main import index

BLUE_PRINT = (
    (index,""),
)

def config_blueprint(app):
    for BlueName,Conf in BLUE_PRINT:
        app.register_blueprint(BlueName,url_prefix=Conf)