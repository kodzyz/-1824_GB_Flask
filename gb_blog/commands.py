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

    admin = User(
        name='admin',
        about='admin',
        email='admin@admin.com',
        age=23,
        password=generate_password_hash('admin'),
        is_staff=True)

    with app.app_context():
        db.session.add(admin)

        db.session.add(
            User(
                name='Нуцубидзе Альфред',
                about='Россия, г.Волгоград, 38 лет',
                email='name1@email.com',
                age=23,
                password=generate_password_hash('123'),
                is_staff=False)
        )
        db.session.add(
            User(
                name='Дмитрий Кокшаров',
                about='Доктор технических наук, доцент, главный научный сотрудник Института проблем управления Российской Академии наук',
                email='name2@email.com',
                age=23,
                password=generate_password_hash('123'),
                is_staff=False)
        )
        db.session.add(
            User(
                name='Алиева Бронислава',
                about='Senior Python Developer в Б-152',
                email='name3@email.com',
                age=23,
                password=generate_password_hash('123'),
                is_staff=False)
        )
        db.session.commit()


@click.command('create-articles', help="create articles")
def create_articles():
    from gb_blog.models import Article
    from wsgi import app

    with app.app_context():
        db.session.add(
            Article(
                title='Web Python',
                text='Курс Web Python поможет Вам осовоить язык программирования Python, а также разобраться с его основными аспектами, такими как: модули, парсеры, регулярные выражения.',
                author='Нуцубидзе Альфред'
            )
        )
        db.session.add(
            Article(
                title='Web JavaScript',
                text='Вы погрузитесь в динамичный мир современного JS-разработки, который станет интересным и увлекательным.',
                author='Дмитрий Кокшаров'
            )
        )
        db.session.add(
            Article(
                title='Python AI',
                text='На курсе Python AI Вы изучите создание простых нейросетей для задач машинного зрения. А также научитесь создавать и развивать более сложные нейросети.',
                author='Алиева Бронислава'
            )
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
