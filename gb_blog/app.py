from flask import Flask

from gb_blog.article.views import article
from gb_blog.user.views import user


def create_app() -> Flask:
    ''' точка входа приложения '''
    # создаем экземпляр приложения
    app = Flask(__name__)
    # вызов функции
    register_blueprint(app)
    return app


def register_blueprint(app: Flask):
    ''' регистрация Blueprint в приложении app'''
    app.register_blueprint(user)
    app.register_blueprint(article)
