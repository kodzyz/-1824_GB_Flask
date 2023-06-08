import click
from werkzeug.security import generate_password_hash
import click
from gb_blog.extensions import db


@click.command('init-db', help="create all db")
def init_db():
    # создать все таблицы
    db.create_all()


@click.command('create-users', help="create users")
def create_users():
    from gb_blog.models import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(email='name@example.com', password=generate_password_hash('123'))
                       )
        db.session.commit()


@click.command('create-init-tags', help="create tags")
def create_init_tags():
    from gb_blog.models import Tag
    from wsgi import app

    with app.app_context():
        tags = ('flask', 'django', 'python', 'gb', 'sqlite')
        for item in tags:
            db.session.add(Tag(name=item))
        db.session.commit()
    click.echo(f'Created tags: {", ".join(tags)}')
