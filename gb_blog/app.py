from combojsonapi.spec import ApiSpecPlugin
from combojsonapi.event import EventPlugin
from combojsonapi.permission import PermissionPlugin
from flask import Flask

from gb_blog.extensions import db, login_manager, migrate, csrf, admin, api
from gb_blog import commands
from gb_blog.models import User


def create_app() -> Flask:
    ''' точка входа приложения '''
    # создаем экземпляр приложения
    app = Flask(__name__)
    app.config.from_object('gb_blog.config')
    # вызов функции
    register_extensions(app)
    register_blueprint(app)
    register_commands(app)
    register_api(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    csrf.init_app(app)
    admin.init_app(app)

    api.plugins = [
        EventPlugin(),
        PermissionPlugin(),
        ApiSpecPlugin(
            app=app,
            tags={
                'Tag': 'Tag API',
                'User': 'User API',
                'Author': 'Author API',
                'Article': 'Article API',
            }
        ),
    ]
    api.init_app(app)

    # какая страница является логином
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


def register_api(app: Flask):
    from gb_blog.api.tag import TagList, TagDetail
    from gb_blog.api.article import ArticleList, ArticleDetail
    from gb_blog.api.author import AuthorList, AuthorDetail
    from gb_blog.api.user import UserList, UserDetail

    api.route(TagList, 'tag_list', '/api/tags/', tag='Tag')
    api.route(TagDetail, 'tag_detail', '/api/tags/<int:id>', tag='Tag')

    api.route(UserList, 'user_list', '/api/users/', tag='User')
    api.route(UserDetail, 'user_detail', '/api/users/<int:id>', tag='User')

    api.route(AuthorList, 'author_list', '/api/authors/', tag='Author')
    api.route(AuthorDetail, 'author_detail', '/api/authors/<int:id>', tag='Author')

    api.route(ArticleList, 'article_list', '/api/articles/', tag='Article')
    api.route(ArticleDetail, 'article_detail', '/api/articles/<int:id>', tag='Article')


def register_blueprint(app: Flask):
    ''' регистрация Blueprint в приложении app'''
    from gb_blog.auth.views import auth
    from gb_blog.user.views import user
    from gb_blog.articles.views import article
    from gb_blog.author.views import author
    from gb_blog import admin

    app.register_blueprint(user)
    app.register_blueprint(auth)
    app.register_blueprint(article)
    app.register_blueprint(author)

    admin.register_views()


def register_commands(app: Flask):
    app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_users)
    # app.cli.add_command(commands.create_articles)
    app.cli.add_command(commands.create_init_tags)
