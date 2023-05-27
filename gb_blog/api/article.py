from flask_combo_jsonapi import ResourceList, ResourceDetail

from gb_blog.extensions import db
from gb_blog.models import Article
from gb_blog.schemas import ArticleSchema


class ArticleList(ResourceList):
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }


class ArticleDetail(ResourceDetail):
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }
