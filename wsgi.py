from werkzeug.security import generate_password_hash
from gb_blog.app import create_app, db

app = create_app()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True
    )


@app.cli.command('init-db', help="create all db")
def init_db():
    # создать все таблицы
    db.create_all()


@app.cli.command('create-users', help="create users")
def create_users():
    from gb_blog.models import User
    db.session.add(
        User(
            name='Нуцубидзе Альфред',
            about='Россия, г.Волгоград, 38 лет',
            email='name1@email.com',
            password=generate_password_hash('123'))
    )
    db.session.add(
        User(
            name='Дмитрий Кокшаров',
            about='Доктор технических наук, доцент, главный научный сотрудник Института проблем управления Российской Академии наук',
            email='name2@email.com',
            password=generate_password_hash('123'))
    )
    db.session.add(
        User(
            name='Алиева Бронислава',
            about='Senior Python Developer в Б-152',
            email='name3@email.com',
            password=generate_password_hash('123'))
    )
    db.session.commit()


@app.cli.command('create-articles', help="create articles")
def create_articles():
    from gb_blog.models import Article
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
