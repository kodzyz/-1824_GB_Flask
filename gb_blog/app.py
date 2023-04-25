from os import getenv, path
from flask import Flask
from json import load

from gb_blog.extension import db, login_manager

from gb_blog.models import User
from gb_blog.auth.views import auth
from gb_blog.user.views import user
from gb_blog.article.views import article


CONFIG_PATH = getenv("CONFIG_PATH", path.join("../dev_config.json"))

VIEWS = [
    user,
    article,
    auth
]


def create_app() -> Flask:
    ''' точка входа приложения '''
    # создаем экземпляр приложения
    app = Flask(__name__)
    app.config.from_file(CONFIG_PATH, load)
    # вызов функции
    register_extensions(app)
    register_blueprint(app)
    return app


def register_extensions(app):
    db.init_app(app)
    # какая страница является логином
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_blueprint(app: Flask):
    ''' регистрация Blueprint в приложении app'''
    for view in VIEWS:
        app.register_blueprint(view)
