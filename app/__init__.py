from flask_bootstrap import Bootstrap
# from flask_login import LoginManager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from config import config
db = SQLAlchemy()


# login_manager = LoginManager()
# login_manager.session_protection = 'strong'
# login_manager.login_view = 'auth.login'

csrf = CSRFProtect()
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    csrf.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    # login_manager.init_app(app)

    # TODO: organize the blueprints, rename
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    return app

