from flask import Flask

from gb_blog.extensions import db, login_manager, migrate, csrf
from gb_blog import commands
from gb_blog.models import User
from gb_blog.auth.views import auth
from gb_blog.user.views import user
from gb_blog.article.views import article

VIEWS = [
    user,
    article,
    auth
]


def create_app() -> Flask:
    ''' точка входа приложения '''
    # создаем экземпляр приложения
    app = Flask(__name__)
    app.config.from_object('gb_blog.config')
    # вызов функции
    register_extensions(app)
    register_blueprint(app)
    register_commands(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    csrf.init_app(app)
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


def register_commands(app: Flask):
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_users)
    app.cli.add_command(commands.create_articles)
