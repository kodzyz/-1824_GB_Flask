from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')


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
