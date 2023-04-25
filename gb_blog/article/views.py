from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {
    1: {
        'title': 'Web Python',
        'text': 'Курс Web Python поможет Вам осовоить язык программирования Python, а также разобраться с его основными аспектами, такими как: модули, парсеры, регулярные выражения.',
        'author': {
            'name': 'Нуцубидзе Альфред',
            'id': '1',
        }
    },
    2: {
        'title': 'Web JavaScript',
        'text': 'Вы погрузитесь в динамичный мир современного JS-разработки, который станет интересным и увлекательным. ',
        'author': {
            'name': 'Дмитрий Кокшаров',
            'id': '2',
        }
    },
    3: {
        'title': 'Python AI',
        'text': 'На курсе Python AI Вы изучите создание простых нейросетей для задач машинного зрения. А также научитесь создавать и развивать более сложные нейросети.',
        'author': {
            'name': 'Алиева Бронислава',
            'id': '3',
        },
    }
}


@article.route('/')
def article_list():
    from gb_blog.models import Article
    articles = Article.query.all()
    return render_template(
        'articles/list.html',
        articles=articles,
    )


@article.route('/<int:pk>')
def get_article(pk: int):
    from gb_blog.models import Article
    _article = Article.query.filter_by(id=pk).one_or_none()
    if _article is None:
        raise NotFound(f'Article id:{pk} not found')
    return render_template(
        'articles/details.html',
        article=_article,
    )

